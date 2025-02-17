# main.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Dict
from RAG import RAG
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize RAG
rag_interface = RAG()

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        result = rag_interface(request.message)
        
        # Format context
        context = ""
        for idx, doc in enumerate(result["context"], 1):
            context += f"## {idx}\n"
            context += f"### Page Context: \n {doc.page_content}\n"
            context += f"### *Source*: \n {doc.metadata['source']}\n\n\n"
        
        return {
            "context": context,
            "answer": result["answer"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))