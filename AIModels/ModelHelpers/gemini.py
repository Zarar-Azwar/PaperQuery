from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# from langchain_google_vertexai import VertexAIEmbeddings, ChatVertexAI

def get_embedding_model(model_name = "models/text-embedding-004"):
    embeddings = GoogleGenerativeAIEmbeddings(model=model_name)
    return embeddings

def get_llm(model_name = "gemini-1.5-flash"):
    llm = ChatGoogleGenerativeAI(model=model_name)
    return llm