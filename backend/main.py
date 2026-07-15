from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.post("/chat")
def chat(request: ChatRequest):

    url = "http://127.0.0.1:8080/v1/chat/completions"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": request.message
            }
        ]
    }

    response = requests.post(url, json=payload)

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    return {
        "question": request.message,
        "answer": answer
    }
