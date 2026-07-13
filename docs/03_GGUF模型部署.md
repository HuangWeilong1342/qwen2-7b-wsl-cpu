# 03 Qwen2 GGUF 模型部署

## 模型下载

官方模型地址：

https://huggingface.co/Qwen/Qwen2-7B-Instruct-GGUF

推荐下载：

```
qwen2-7b-instruct-q4_k_m.gguf
```

## 模型目录

下载完成后放入：

```text
~/qwen_lab/models/
```

目录结构：

```text
~/qwen_lab/
├── llama.cpp/
└── models/
    └── qwen2-7b-instruct-q4_k_m.gguf
```

## 加载模型

```bash
cd ~/qwen_lab/llama.cpp

./build/bin/llama-cli \
-m ../models/qwen2-7b-instruct-q4_k_m.gguf
```

## 本章总结

完成 Qwen2 GGUF 模型部署，为本地推理做好准备。
