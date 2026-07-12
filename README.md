# 基于 llama.cpp 在 WSL2 上部署 Qwen2-7B-Instruct GGUF（CPU 推理）

## 项目简介

本项目基于 **llama.cpp** 推理框架，在 **WSL2 Ubuntu** 环境下部署 **Qwen2-7B-Instruct GGUF** 模型，实现本地 CPU 推理。

项目目标不仅是完成模型部署，还将逐步扩展为一个基于 **RAG（Retrieval-Augmented Generation）** 的本地知识库问答系统，并最终提供可访问的 Web 服务。

本项目主要用于：

- 学习大语言模型（LLM）本地部署流程
- 学习 GGUF 模型格式及 llama.cpp 推理框架
- 理解 CPU 推理流程及性能优化
- 学习 Linux 环境下的大模型部署
- 为后续 RAG 系统开发提供基础

---

## 项目目标

- [x] 搭建 WSL2 Ubuntu 开发环境
- [ ] 编译 llama.cpp
- [ ] 部署 Qwen2-7B-Instruct GGUF
- [ ] 实现本地 CPU 推理
- [ ] 使用 llama-server 提供 OpenAI Compatible API
- [ ] 构建 RAG 检索增强问答系统
- [ ] 部署 Web 服务

---

## 技术栈

| 模块 | 技术 |
|------|------|
| 操作系统 | WSL2 Ubuntu |
| 推理框架 | llama.cpp |
| 大语言模型 | Qwen2-7B-Instruct GGUF |
| 编程语言 | C++ / Python |
| Web 框架（计划） | FastAPI |
| 向量数据库（计划） | FAISS |
| 前端（计划） | Vue3 |

---

## 项目目录

```text
qwen2-7b-wsl-cpu/

├── README.md
├── docs/
├── scripts/
├── benchmark/
├── screenshots/
└── .gitignore
```

---

## 开发环境

| 项目 | 配置 |
|------|------|
| Windows | Windows 11 |
| WSL | WSL2 |
| Ubuntu | Ubuntu 24.04 LTS |
| 编译工具 | CMake、GCC |
| 推理框架 | llama.cpp |
| 模型 | Qwen2-7B-Instruct GGUF |

---

## 当前进度

目前已完成：

- 创建 GitHub 项目
- 配置 Git 开发环境
- 搭建 WSL2 Ubuntu 环境
- 下载并配置 llama.cpp 源码

正在进行：

- 编译 llama.cpp
- 部署 Qwen2-7B-Instruct GGUF

---

## 后续计划

### 第一阶段：本地推理

- 编译 llama.cpp
- 下载 GGUF 模型
- CPU 推理测试
- Benchmark 测试

### 第二阶段：API 服务

- 部署 llama-server
- OpenAI Compatible API
- FastAPI 后端

### 第三阶段：RAG 系统

- PDF 文档解析
- 文本切分
- Embedding
- FAISS 向量检索
- Prompt 构建
- 问答系统

### 第四阶段：Web 部署

- Vue3 前端
- 在线聊天
- 文件上传
- 知识库管理

---

## 项目截图

后续补充：

- 编译过程
- 推理结果
- Benchmark
- Web 页面

---

## 第三方开源项目声明
1. llama.cpp
项目地址：https://github.com/ggerganov/llama.cpp
开源协议：MIT License
本项目仅通过Shell脚本调用外部独立llama.cpp，未内置、分发其源码。

2. Qwen2 大模型
项目地址：https://github.com/QwenLM/Qwen3
使用前请阅读阿里官方Qwen开源许可证，遵守模型使用规范。

## License

MIT