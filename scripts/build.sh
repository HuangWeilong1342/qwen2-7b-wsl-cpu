#!/bin/bash

set -e

echo "========================================"
echo "Building llama.cpp..."
echo "========================================"

LLAMA_DIR="$HOME/llm_lab/llama.cpp"

cd "$LLAMA_DIR"

cmake -B build

cmake --build build -j$(nproc)

echo
echo "========================================"
echo "Build completed successfully!"
echo "========================================"
