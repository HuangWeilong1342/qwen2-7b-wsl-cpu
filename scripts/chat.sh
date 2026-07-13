#!/bin/bash

LLAMA_DIR="$HOME/qwen_lab/llama.cpp"
MODEL="$HOME/qwen_lab/models/qwen2-7b-instruct-q4_k_m.gguf"

cd "$LLAMA_DIR" || exit 1

export LD_LIBRARY_PATH="$LLAMA_DIR/build/bin:$LD_LIBRARY_PATH"

./build/bin/llama-cli \
    -m "$MODEL" \
    -cnv \
    -t 8
