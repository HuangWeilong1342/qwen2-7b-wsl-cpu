#!/bin/bash

set -e

export LD_LIBRARY_PATH=$HOME/qwen_lab/llama.cpp/build/bin:$LD_LIBRARY_PATH

LLAMA_DIR="$HOME/qwen_lab/llama.cpp"
MODEL="../models/qwen2-7b-instruct-q4_k_m.gguf"

echo "========================================"
echo "Running Benchmark..."
echo "Model: $MODEL"
echo "========================================"

cd "$LLAMA_DIR"

./build/bin/llama-bench \
    -m "$MODEL" \
    -t 8

echo
echo "========================================"
echo "Benchmark Finished!"
echo "========================================"
