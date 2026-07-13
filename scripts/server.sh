#!/bin/bash

# 项目根目录
LLAMA_DIR="$HOME/qwen_lab/llama.cpp"

# 模型路径
MODEL="$HOME/qwen_lab/models/qwen2-7b-instruct-q4_k_m.gguf"

# 进入项目目录
cd "$LLAMA_DIR" || exit 1

# 设置动态库路径（新版 llama.cpp 需要）
export LD_LIBRARY_PATH="$LLAMA_DIR/build/bin:$LD_LIBRARY_PATH"

echo "========================================"
echo "Starting llama-server..."
echo "Model: $MODEL"
echo "Host : 127.0.0.1"
echo "Port : 8080"
echo "========================================"

./build/bin/llama-server \
    -m "$MODEL" \
    -t 8 \
    --host 127.0.0.1 \
    --port 8080
