from rag import ask
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_methods=["*"],
allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question:str


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask(request.question)
    return {"answer": answer}