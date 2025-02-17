from langchain import hub
from langchain.prompts import PromptTemplate

from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph
from langchain_milvus import Milvus
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os
from AIModels import AIModel

from schemas.schemas import State

class RAG:
    def __init__(self):
        ai_model = AIModel()

        self.llm = ai_model.get_llm()
        embeddings = ai_model.get_embedding_model()

        self.vector_store = Milvus(
            embedding_function=embeddings,
            collection_name = "ResearchPapers",
            connection_args={
                'uri':os.environ["ZILLIZ_ENDPOINT"],
                'token':os.environ["ZILLIZ_TOKEN"]
            },
        )

        
        template = """
        You are a personal assistant that is expert at reading and understanding research papers and then answering questions about the research paper from the given context. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know.

        Question: {question}

        Context: {context}

        Answer: 
        """

        self.prompt = PromptTemplate(
                                    input_variables = ["question", "context"], 
                                    template = template
                                )

        graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        graph_builder.add_edge(START, "retrieve")
        self.graph = graph_builder.compile()

    def __call__(self, user_query):
        result = self.graph.invoke({"question": user_query})
        return result
    
    def retrieve(self, state: State):
        retrieved_docs = self.vector_store.similarity_search(state["question"], k=3)
        return {"context": retrieved_docs}

    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.prompt.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)
        return {"answer": response.content}


if __name__ == "__main__":
    rag = RAG()
    result = rag("What is MiT Cheetah?")

    print(result)