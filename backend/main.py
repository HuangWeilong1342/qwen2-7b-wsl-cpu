from fastapi import FastAPI

from backend.routers.chat import router

app = FastAPI(
    title="Qwen2 Local API"
)

app.include_router(router)
