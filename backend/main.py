from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File, HTTPException
from typing import Annotated

from backend import CredentialsEnvironment

from langchain.document_loaders import TextLoader

app = FastAPI()

# CORS HANDLING: Local host allows for all origins as there will be no hosted info
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])


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


async def process_uploaded_file(file_content: bytes):
    # Use the langchain library, for example using TextLoader
    text_loader = TextLoader(file_content)
    document_text = text_loader.load()
    return document_text


@app.post("/files_upload")
async def files_upload(files: Annotated[list[UploadFile], File(description="Multiple files as UploadFile")]):
    for file in files:
        file_content = await file.read()

        document_text = await process_uploaded_file(file_content)
        print(document_text)

