# 基于 llama.cpp 构建本地 RAG 知识库问答系统

> 基于 **llama.cpp**、**Qwen2-7B-Instruct GGUF**、**FastAPI**、**Sentence Transformers** 和 **FAISS** 构建的本地 RAG（Retrieval-Augmented Generation）知识库问答系统，支持 PDF 知识库管理、向量检索以及本地大模型问答，全程离线运行，无需依赖第三方大模型 API。

---

# 项目简介

本项目从零开始完成了本地大模型部署，并在此基础上构建了一个完整的 RAG（检索增强生成）知识库问答系统。

整个系统包括：

- 本地部署 Qwen2-7B-Instruct GGUF
- llama.cpp CPU 推理
- OpenAI Compatible API
- FastAPI 后端服务
- Prompt Template
- 多轮对话（Conversation History）
- PDF 知识库管理
- Embedding 向量化
- FAISS 向量数据库
- Retriever 检索
- RAG 问答
- PDF 上传与删除
- 自动重建向量索引

项目主要用于：

- 大模型本地部署实践
- RAG 系统开发学习
- AI 工程化实践
- 考研（计算机 / 人工智能）项目展示

---

# 系统架构

```text
                 FastAPI API
                      │
         Conversation History
                      │
               RAG Pipeline
                      │
              FAISS Retriever
                      │
       BGE Embedding Model
                      │
          PDF Knowledge Base
                      │
     llama-server(OpenAI API)
                      │
      Qwen2-7B-Instruct GGUF
                      │
                llama.cpp
                      │
              WSL2 Ubuntu
```

---

# 项目功能

目前已经实现：

- ✅ Qwen2-7B 本地部署（GGUF）
- ✅ CPU 推理
- ✅ llama-server 服务
- ✅ OpenAI Compatible API
- ✅ FastAPI 后端
- ✅ Prompt Template
- ✅ 多轮对话（Conversation History）
- ✅ PDF Loader
- ✅ Text Splitter
- ✅ Embedding（BGE-small-zh-v1.5）
- ✅ FAISS 向量数据库
- ✅ Retriever 检索
- ✅ RAG 问答
- ✅ PDF 上传
- ✅ PDF 删除
- ✅ 查看知识库
- ✅ 自动重建向量索引
- ✅ Swagger API 文档

---

# 技术栈

| 模块 | 技术 |
|------|------|
| 操作系统 | WSL2 Ubuntu 24.04 |
| 推理框架 | llama.cpp |
| 大语言模型 | Qwen2-7B-Instruct GGUF |
| 后端框架 | FastAPI |
| Embedding | BAAI/bge-small-zh-v1.5 |
| 向量数据库 | FAISS |
| 文本处理 | LangChain |
| PDF 解析 | PyMuPDF |
| 开发语言 | Python / C++ / Shell |

---

# 项目目录

```text
local-rag-qa-system
│
├── backend
│   ├── routers
│   ├── schemas
│   ├── services
│   ├── prompts
│   ├── utils
│   ├── config.py
│   └── main.py
│
├── data
│   ├── pdf
│   └── faiss
│
├── scripts
├── tests
├── docs
├── screenshots
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 快速开始

## 1. 启动 llama-server

```bash
bash scripts/server.sh
```

## 2. 启动 FastAPI

```bash
uvicorn backend.main:app --reload
```

## 3. 打开 Swagger

浏览器访问：

```text
http://127.0.0.1:8000/docs
```

---

# API 接口

| 方法 | 接口 | 说明 |
|------|------|------|
| POST | /chat | RAG 问答 |
| POST | /upload | 上传 PDF |
| GET | /documents | 查看知识库 |
| DELETE | /documents/{filename} | 删除 PDF |

---

# 系统流程

上传知识库：

```text
PDF
 │
Loader
 │
Text Splitter
 │
Embedding
 │
FAISS
 │
保存索引
```

问答流程：

```text
用户问题
      │
Embedding
      │
FAISS 检索
      │
Retriever
      │
Prompt Template
      │
Qwen2-7B
      │
返回答案
```

---

# 项目截图

后续补充：

- 系统架构
- llama.cpp 推理
- Swagger API
- PDF 上传
- 知识库管理
- RAG 问答

---

# 第三方开源项目

- **llama.cpp**（MIT License）
- **Qwen**（Apache License 2.0）
- **LangChain**（MIT License）
- **Sentence Transformers**（Apache License 2.0）
- **FAISS**（MIT License）

---

# License

本项目采用 **MIT License** 开源协议。