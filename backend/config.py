# backend/config.py

LLM_HOST = "127.0.0.1"
LLM_PORT = 8080

LLM_API_URL = f"http://{LLM_HOST}:{LLM_PORT}/v1/chat/completions"

MODEL_NAME = "qwen2-7b"

TIMEOUT = 300

TEMPERATURE = 0.7

MAX_TOKENS = 1024
