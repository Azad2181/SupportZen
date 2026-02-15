from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

def load_vector_store():
    loader = TextLoader("data/policies.txt")
    docs = loader.load()

    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)