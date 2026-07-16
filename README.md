# 基于 llama.cpp 构建本地 RAG 问答系统（Qwen2-7B）

## 项目简介

本项目基于 **llama.cpp** 推理框架，在 **WSL2 Ubuntu** 环境下部署 **Qwen2-7B-Instruct GGUF**，并使用 **FastAPI** 构建本地 AI 服务，最终实现一个支持 **RAG（Retrieval-Augmented Generation）** 的本地知识库问答系统。

整个项目从模型部署开始，逐步完成：

- 本地大模型部署
- OpenAI Compatible API
- FastAPI 后端
- Prompt Template
- 多轮对话
- PDF 知识库
- Embedding
- FAISS 检索
- Web 前端

项目主要用于学习大模型部署、RAG 系统开发及工程化实践。

---

# 当前开发进度

## 第一阶段：本地部署（已完成）

- [x] WSL2 Ubuntu 环境搭建
- [x] 编译 llama.cpp
- [x] 下载 Qwen2-7B GGUF
- [x] CPU 推理
- [x] Benchmark 测试
- [x] llama-server 部署
- [x] OpenAI Compatible API

---

## 第二阶段：FastAPI 服务（已完成）

- [x] FastAPI 项目搭建
- [x] Chat API
- [x] 配置文件管理
- [x] Prompt Template
- [x] 多轮对话 History
- [x] 日志(Log)
- [x] 异常处理
- [x] Swagger API 文档

目前访问：

```
http://127.0.0.1:8000/docs
```

即可进行在线测试。

---

## 第三阶段：RAG（开发中）

目前完成：

- [x] PDF Loader
- [x] PDF 文本读取
- [x] Recursive Text Splitter
- [x] Embedding Model（BGE-small-zh-v1.5）
- [x] 文本向量生成

正在开发：

- [ ] FAISS 向量数据库
- [ ] Top-K 检索
- [ ] Prompt 拼接
- [ ] RAG 问答

---

## 第四阶段：Web 前端（计划）

- [ ] Vue3
- [ ] 在线聊天
- [ ] 文件上传
- [ ] PDF 管理
- [ ] 知识库管理

---

# 技术栈

| 模块 | 技术 |
|------|------|
| 操作系统 | WSL2 Ubuntu 24.04 |
| 推理框架 | llama.cpp |
| 模型 | Qwen2-7B-Instruct GGUF |
| Web | FastAPI |
| Prompt | Prompt Template |
| Embedding | BGE-small-zh-v1.5 |
| 文本处理 | LangChain |
| 向量数据库 | FAISS（开发中） |
| 前端 | Vue3（计划） |

---

# 项目目录

```text
qwen2-7b-wsl-cpu
│
├── backend
│   ├── routers
│   ├── services
│   ├── utils
│   ├── prompts
│   ├── config.py
│   └── main.py
│
├── data
│   └── pdf
│
├── tests
│
├── docs
│
├── scripts
│
├── benchmark
│
├── screenshots
│
└── README.md
```

---

# 项目功能

目前已经实现：

✅ 本地部署 Qwen2-7B

✅ CPU 推理

✅ OpenAI API

✅ FastAPI 后端

✅ Prompt Template

✅ 多轮上下文

✅ 日志系统

✅ 异常处理

✅ PDF 加载

✅ PDF 文本切分

✅ Embedding 向量生成

---

# 项目截图

后续补充：

- llama.cpp 推理
- Swagger API
- Prompt Template
- History
- PDF Loader
- Embedding
- FAISS 检索
- Web Chat

---

# 后续开发计划

## RAG

- FAISS 建库
- 文档索引
- Top-K 检索
- Prompt 拼接
- RAG Chat

## Web

- Vue3 前端
- 文件上传
- PDF 管理
- 知识库管理
- 在线聊天

---

# 第三方开源项目

### llama.cpp

https://github.com/ggml-org/llama.cpp

License：MIT

---

### Qwen2

https://github.com/QwenLM/Qwen3

License：Apache License 2.0

---

### LangChain

https://github.com/langchain-ai/langchain

License：MIT

---

### Sentence Transformers

https://github.com/UKPLab/sentence-transformers

License：Apache License 2.0

---

### FAISS

https://github.com/facebookresearch/faiss

License：MIT

---

# License

MIT License