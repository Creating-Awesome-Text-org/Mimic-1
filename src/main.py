from fastapi import FastAPI
from pydantic import BaseModel
import CredentialsEnvironment

app = FastAPI()


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
    return {"message": "Environmental credentials setup"}

