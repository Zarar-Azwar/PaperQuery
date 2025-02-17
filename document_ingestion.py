from dotenv import load_dotenv
load_dotenv()



from langchain_community.document_loaders import TextLoader
from langchain_milvus import Milvus

from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader, PDFMinerLoader
import os

from AIModels import AIModel

from langchain_community.document_loaders import UnstructuredFileLoader, DirectoryLoader

loader = DirectoryLoader("Papers",  glob="*.pdf", show_progress=True, loader_cls=PDFMinerLoader)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500)
all_splits = text_splitter.split_documents(docs)
for doc in all_splits:
    doc.metadata = {key.replace(".", "_"): value for key, value in doc.metadata.items()}


print("Total Splits:", len(all_splits))

ai_model = AIModel()

embeddings = ai_model.get_embedding_model()
# embeddings = OllamaEmbeddings(
#     model="llama3:8b"
# )

# embeddings = GoogleGenerativeAIEmbeddings(
#     model='text-embedding-004'
# )

vector_db = Milvus.from_documents(
    all_splits,
    embeddings,
    collection_name = "ResearchPapers",
    connection_args={
         'uri':os.environ["ZILLIZ_ENDPOINT"],
         'token':os.environ["ZILLIZ_TOKEN"]
    },
)