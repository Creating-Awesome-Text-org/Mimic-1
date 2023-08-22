# Generic imports
import os
import tempfile

# API imports
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
from starlette.middleware.cors import CORSMiddleware

# Langchain Imports
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone

# Document loaders
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import Docx2txtLoader

# Vector db
import pinecone

# Environmental variables credential setting
from backend import CredentialsEnvironment


app = FastAPI()

# CORS HANDLING: Local host allows for all origins as there will be no hosted info
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

# Document Upload preparation
index_name = "flourishing-humanity"
chunk_size = 1000
chunk_overlap = 0


class Credentials(BaseModel):
    openai_api_key: str
    pinecone_api_key: str
    pinecone_env: str


@app.get("/")
async def root():
    return {"message": "Welcome to Mimic"}


@app.post("/credentials")
async def mimic_credentials(credentials: Credentials):
    CredentialsEnvironment.set_credentials(credentials.openai_api_key,
                                           credentials.pinecone_api_key,
                                           credentials.pinecone_env)
    print("Credentials received")
    return {"message": "Environmental credentials setup"}


async def upload_documents(docs):
    embeddings = HuggingFaceEmbeddings()
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),  # Initialize pinecone link
        environment=os.getenv("PINECONE_ENV"),
    )

    if index_name not in pinecone.list_indexes():  # If the index doesn't exist
        pinecone.create_index(
            name=index_name,
            metric='cosine',
            dimension=768
        )

    Pinecone.from_documents(docs, embeddings, index_name=index_name)


async def process_txt_file(file: bytes, file_name: str):
    with tempfile.NamedTemporaryFile(delete=False, prefix=file_name + "_") as temp_file:
        temp_file.write(file)  # Create temporary file
        temp_file_path = temp_file.name  # Get file name

        loader = TextLoader(temp_file_path)  # Load the text into text loader
        document_text = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(document_text)
        return docs


async def process_pdf_file(file: bytes, file_name: str):
    with tempfile.NamedTemporaryFile(delete=False, prefix=file_name + "_") as temp_file:
        temp_file.write(file)  # Create temporary file
        temp_file_path = temp_file.name  # Get file name

        loader = PyPDFLoader(temp_file_path)
        docs = loader.load_and_split()

        print(docs)
        return docs


async def process_md_file(file: bytes, file_name: str):
    with tempfile.NamedTemporaryFile(delete=False, prefix=file_name + "_") as temp_file:
        temp_file.write(file)  # Create temporary file
        temp_file_path = temp_file.name  # Get file name

        loader = UnstructuredMarkdownLoader(temp_file_path)
        document_text = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(document_text)
        print(docs)
        return docs


async def file_type_handling(file_type: str, file: bytes, file_name: str):
    docs = []
    match file_type:
        case "pdf":
            print("PDF detected")
            docs = await process_pdf_file(file, file_name)
        case "txt":
            print("txt detected")
            docs = await process_txt_file(file, file_name)
        case "md":
            print("md detected")
            docs = await process_md_file(file, file_name)
        case "docx":
            print("docx detected")
        case _:
            print("File type not recognized")
    await upload_documents(docs)


@app.post("/files_upload")
async def files_upload(files: List[UploadFile] = File(...)):
    for file in files:
        name_split = file.filename.split(".")  # Split the file name using the dot separator
        file_type = name_split[1]  # Determine the file type
        file_name = name_split[0]

        file_content = await file.read()  # Read the file content
        await file_type_handling(file_type, file_content, file_name)  # File type specific upload to pinecone
