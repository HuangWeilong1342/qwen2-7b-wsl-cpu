# 06 llama.cpp Server 部署

## 1. 文档说明

本文档介绍如何使用 `llama.cpp` 提供的 `llama-server` 将本地大语言模型部署为 HTTP 服务，并提供 **OpenAI Compatible API**，为后续 FastAPI 后端开发和 RAG 系统构建提供模型服务。

---

## 2. llama-server 简介

`llama-server` 是 `llama.cpp` 提供的服务端程序，可将本地 GGUF 模型封装为 HTTP API，支持 OpenAI Chat Completions 接口规范。

在本项目中的位置如下：

```text
Browser / Swagger
        │
        ▼
    FastAPI
        │
        ▼
  llama-server
        │
        ▼
Qwen2-7B GGUF
```

后续所有聊天请求都将通过 `llama-server` 调用本地模型。

---

## 3. 启动服务

进入 `llama.cpp` 目录：

```bash
cd ~/llm_lab/llama.cpp
```

启动服务：

```bash
./build/bin/llama-server \
    -m ../models/qwen2-7b-instruct-q4_k_m.gguf \
    -t 8 \
    --host 127.0.0.1 \
    --port 8080
```

---

## 4. 参数说明

| 参数 | 说明 |
|------|------|
| `-m` | 指定 GGUF 模型路径 |
| `-t` | CPU 推理线程数 |
| `--host` | 服务监听地址 |
| `--port` | 服务监听端口 |

本项目默认配置：

- Host：`127.0.0.1`
- Port：`8080`
- Threads：`8`

---

## 5. 验证服务

启动成功后，终端会输出类似信息：

```text
HTTP server listening

...

127.0.0.1:8080
```

浏览器访问：

```text
http://127.0.0.1:8080
```

能够打开页面说明 `llama-server` 已正常启动。

> **说明：**
>
> 浏览器首页仅用于确认服务已启动，真正的模型调用将在下一章节通过 OpenAI Compatible API 进行验证。

---

## 6. 注意事项

- 启动前请确认模型路径正确。
- 若端口 `8080` 已被占用，可修改 `--port` 参数。
- 若无法访问服务，请检查防火墙、WSL 网络配置及 `llama-server` 是否正常运行。

---

## 7. 本章总结

本章完成了 `llama-server` 的部署，实现了本地模型的 HTTP 服务化。

主要完成内容：

- 启动 `llama-server`
- 配置模型与线程参数
- 部署本地 HTTP 服务
- 提供 OpenAI Compatible API 运行环境

下一章节将验证 **OpenAI Compatible API**，通过 `/v1/chat/completions` 接口调用本地模型。