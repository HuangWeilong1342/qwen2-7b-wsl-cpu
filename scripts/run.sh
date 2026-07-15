#!/bin/bash

echo "========================================"
echo "Qwen2 Local AI Project"
echo "========================================"

echo
echo "[1] Start llama-server"

echo "    ./scripts/server.sh"

echo
echo "[2] Start FastAPI"

echo "    cd backend"

echo "    source venv/bin/activate"

echo "    uvicorn main:app --reload"

echo
echo "[3] Open Swagger"

echo "    http://127.0.0.1:8000/docs"

echo
echo "========================================"
echo "After the RAG module is completed,"
echo "this script will support one-click startup."
echo "========================================"
