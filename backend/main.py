import tempfile

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File
from typing import List

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


async def process_txt_file(file_content: bytes):
    # Create a temporary file and write the content to it
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file_content)

        # Use the langchain library to load the text from the temporary file
        text_loader = TextLoader(temp_file.name)
        document_text = text_loader.load()
        print(document_text)


async def file_type_handling(file_type: str, file: bytes):
    match file_type:
        case "pdf":
            print("PDF detected")
        case "txt":
            print("txt detected")
            await process_txt_file(file)
        case "md":
            print("md detected")
        case "docx":
            print("docx detected")
        case _:
            print("File type not recognized")


@app.post("/files_upload")
async def files_upload(files: List[UploadFile] = File(...)):
    for file in files:
        name_split = file.filename.split(".")  # Split the file name using the dot separator
        file_type = name_split[1]  # Determine the file type
        print(file_type)

        file_content = await file.read()  # Read the file content

        await file_type_handling(file_type, file_content)



