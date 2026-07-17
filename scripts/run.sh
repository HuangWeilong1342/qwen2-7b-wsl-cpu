#!/bin/bash

echo "========================================"
echo "Local RAG QA System"
echo "========================================"

echo
echo "[1] Start llama.cpp Server"

echo "    ./scripts/server.sh"

echo
echo "[2] Start FastAPI Backend"

echo "    source venv/bin/activate"

echo "    uvicorn backend.main:app --reload"

echo
echo "[3] Open Swagger API"

echo "    http://127.0.0.1:8000/docs"

echo
echo "[4] Start Web UI (Future)"

echo "    (Coming Soon)"

echo
echo "========================================"
echo "Project: Local RAG QA System"
echo "Model  : Qwen2-7B-Instruct GGUF"
echo "Backend: FastAPI"
echo "RAG    : LangChain + FAISS"
echo "========================================"