from fastapi import APIRouter

from backend.schemas.chat import ChatRequest, ChatResponse
from backend.services.llm import chat
from backend.services.history import clear_history

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_api(request: ChatRequest):

    answer = chat(request.message)

    return ChatResponse(response=answer)


@router.post("/clear_history")
def clear_history_api():

    clear_history()

    return {
        "message": "History cleared."
    }
