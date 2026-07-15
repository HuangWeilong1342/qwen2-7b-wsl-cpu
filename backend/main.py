from fastapi import FastAPI

app = FastAPI(
    title="Qwen2 Local AI",
    version="1.0.0",
    description="FastAPI Backend for llama.cpp"
)


@app.get("/")
def root():
    return {
        "message": "FastAPI is running!"
    }
