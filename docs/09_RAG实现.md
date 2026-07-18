# 09 RAG 实现

## 1. 文档说明

本文档介绍本项目 RAG（Retrieval-Augmented Generation，检索增强生成）的整体实现流程，包括知识库构建、文本检索、Prompt 构建以及调用本地大语言模型生成回答。

RAG 的引入使模型能够结合外部知识库进行回答，减少幻觉（Hallucination），提高回答的准确性和专业性。

---

## 2. 什么是 RAG

传统大语言模型只能根据训练数据回答问题，无法获取新的知识。

RAG（Retrieval-Augmented Generation）的核心思想是：

> **先检索，再生成。**

即：

1. 从知识库中检索与问题最相关的内容；
2. 将检索结果作为上下文加入 Prompt；
3. 再交给大语言模型生成最终答案。

整体流程如下：

```text
用户问题
      │
      ▼
Embedding
      │
      ▼
FAISS 检索 Top-K
      │
      ▼
相关文档
      │
      ▼
Prompt 构建
      │
      ▼
Qwen2-7B
      │
      ▼
最终回答
```

---

## 3. 项目整体流程

本项目 RAG 流程如下：

```text
PDF 文档
      │
      ▼
PDF Loader
      │
      ▼
Text Splitter
      │
      ▼
Embedding Model
      │
      ▼
FAISS Index
      │
      ▼
Retriever
      │
      ▼
Prompt Template
      │
      ▼
llama-server
      │
      ▼
Qwen2-7B-Instruct
```

整个流程均在本地运行，无需联网。

---

## 4. 核心模块

本项目 RAG 主要由以下几个模块组成：

```text
backend/services/
├── loader.py
├── splitter.py
├── embedding.py
├── vector_store.py
├── retriever.py
└── rag.py
```

各模块作用如下：

| 模块 | 功能 |
|------|------|
| `loader.py` | 加载 PDF 文档 |
| `splitter.py` | 文本切分 |
| `embedding.py` | 文本向量化 |
| `vector_store.py` | 构建 FAISS 向量库 |
| `retriever.py` | 相似度检索 |
| `rag.py` | 组织 Prompt 并调用 LLM |

---

## 5. RAG 工作流程

### Step 1：加载 PDF

读取知识库中的 PDF 文件：

```text
data/pdf/
```

使用 PDF Loader 提取文本内容。

---

### Step 2：文本切分

由于大语言模型存在上下文长度限制，因此需要将长文本切分为多个较小的文本块。

例如：

```text
100 页 PDF

↓

Chunk 1

Chunk 2

Chunk 3

...
```

便于后续建立向量索引。

---

### Step 3：文本向量化

使用 Embedding 模型：

```text
BGE-small-zh-v1.5
```

将每个文本块转换为向量表示：

```text
文本

↓

Embedding

↓

768 维向量
```

向量能够表示文本的语义信息。

---

### Step 4：建立 FAISS 向量库

所有文本向量存入 FAISS：

```text
Chunk1

↓

Vector

↓

FAISS
```

建立完成后保存至：

```text
data/faiss/
```

便于后续快速加载。

---

### Step 5：相似度检索

用户输入问题：

```text
什么是 RAG？
```

首先进行向量化：

```text
问题

↓

Embedding
```

然后在 FAISS 中检索：

```text
Top-K
```

获得最相关的文档片段。

---

### Step 6：Prompt 构建

检索得到的内容与用户问题共同组成 Prompt：

```text
系统提示词

+

知识库内容

+

用户问题

↓

Prompt
```

随后发送给本地部署的 Qwen2 模型。

---

### Step 7：生成回答

最终调用：

```text
FastAPI

↓

llama-server

↓

Qwen2-7B
```

生成最终回答。

整个流程如下：

```text
Question

↓

Retriever

↓

Knowledge

↓

Prompt

↓

LLM

↓

Answer
```

---

## 6. 项目优势

相比直接调用大语言模型，本项目具有以下优势：

- 支持本地知识库问答
- 无需重新训练模型
- 回答更加准确
- 支持动态扩展知识库
- 数据完全本地存储
- 不依赖互联网

---

## 7. 本章总结

本章完成了 RAG 系统的整体实现，包括：

- PDF 文档加载
- 文本切分
- Embedding 向量化
- FAISS 向量数据库
- 相似度检索
- Prompt 构建
- 本地大语言模型生成回答

至此，本项目已经完成完整的 RAG 问答流程。

下一章节将介绍 **知识库构建**，包括 PDF 上传、索引重建以及知识库动态更新。