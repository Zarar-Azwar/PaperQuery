from langchain_ollama import OllamaEmbeddings, ChatOllama


def get_embedding_model(model_name = "llama3:8b"):
    embeddings = OllamaEmbeddings(model="llama3:8b")
    return embeddings

def get_llm(model_name = "llama3:8b"):
    llm = ChatOllama(model = model_name)
    return llm