from fastapi import FastAPI

from backend.routers.chat import router as chat_router
from backend.routers.upload import router as upload_router
from backend.routers.documents import router as documents_router

app = FastAPI(
    title="Qwen2 Local API"
)

app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(documents_router)
