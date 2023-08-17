import os
import credentials

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader


import pinecone

path = "../kb/"
index_name = "flourishing-humanity"


def docs_to_vector_db():
    docs = prep_txt_documents(path)  # Prepare the documents
    vector_db = embed_documents(docs, index_name)  # Upload the documents to Pinecone vector DB
    return vector_db


def prep_txt_documents(file_path: str):
    loader = DirectoryLoader(file_path,
                             glob="**/*.txt",
                             loader_cls=TextLoader,
                             show_progress=True)  # Directory uploader for txt documents
    documents = loader.load()  # Load documents

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  # Specify document character splitter
    docs = text_splitter.split_documents(documents)  # Split document into chunks
    return docs


def embed_documents(docs, index_name: str):
    embeddings = OpenAIEmbeddings(openai_api_key='OPENAI KEY')  # Initialize OpenAI embeddings process (chunks to vector model)

    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),  # Initialize pinecone link
        environment=os.getenv("PINECONE_ENV"),
    )

    create_index(index_name)  # Create the specified Index

    vectordb = Pinecone.from_documents(docs, embeddings, index_name=index_name)  # Create the vector DB

    return vectordb


def create_index(index_name: str):
    if index_name not in pinecone.list_indexes():  # If the index doesn't exist
        pinecone.create_index(
            name=index_name,
            metric='cosine',
            dimension=1536
)


if __name__ == "__main__":
    credentials.set_credentials()
    vector_db = docs_to_vector_db()
    print("Upload Complete")
