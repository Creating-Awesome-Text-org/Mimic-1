import os


def set_credentials(openai_key: str, pinecone_key: str, pinecone_env: str):
    os.environ['OPENAI_API_KEY'] = openai_key
    os.environ["PINECONE_API_KEY"] = pinecone_key
    os.environ["PINECONE_ENV"] = pinecone_env
