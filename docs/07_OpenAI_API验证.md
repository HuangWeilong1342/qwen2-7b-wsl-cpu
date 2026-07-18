# 07 OpenAI Compatible API 验证

## 1. 文档说明

本文档用于验证 `llama-server` 提供的 **OpenAI Compatible API** 是否能够正常工作，并通过 HTTP 请求调用本地部署的 Qwen2-7B-Instruct 模型，为后续 FastAPI 后端开发和 RAG 系统构建提供接口基础。

---

## 2. OpenAI Compatible API 简介

`llama-server` 实现了与 OpenAI Chat Completions API 兼容的接口，因此可以像调用 OpenAI 官方 API 一样调用本地部署的大语言模型，无需修改业务逻辑。

本项目默认服务地址：

```text
http://127.0.0.1:8080
```

主要接口如下：

| 请求方式 | 接口 | 说明 |
|----------|------|------|
| GET | `/v1/models` | 获取当前加载的模型 |
| POST | `/v1/chat/completions` | 调用模型进行对话 |

---

## 3. 获取模型列表

请求：

```http
GET /v1/models
```

PowerShell 示例：

```powershell
Invoke-RestMethod `
    -Uri "http://127.0.0.1:8080/v1/models"
```

返回结果示例：

```json
{
    "object": "list",
    "data": [
        {
            "id": "qwen2-7b-instruct-q4_k_m.gguf"
        }
    ]
}
```

若成功返回模型信息，则说明 `llama-server` 已正常运行。

---

## 4. 调用 Chat Completions API

请求：

```http
POST /v1/chat/completions
```

PowerShell 示例：

```powershell
$body = @{
    messages = @(
        @{
            role = "user"
            content = "你好，请介绍一下你自己。"
        }
    )
} | ConvertTo-Json -Depth 3

Invoke-RestMethod `
    -Uri "http://127.0.0.1:8080/v1/chat/completions" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

返回结果示例：

```json
{
    "object": "chat.completion",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "你好！我是 Qwen2，一个由阿里云开发的大语言模型……"
            }
        }
    ]
}
```

当返回结果包含：

```text
object: chat.completion
```

说明 OpenAI Compatible API 调用成功，模型能够正常生成回答。

---

## 5. 项目调用流程

本项目中，模型调用流程如下：

```text
Browser / Swagger
        │
        ▼
    FastAPI
        │
        ▼
OpenAI Compatible API
        │
        ▼
   llama-server
        │
        ▼
Qwen2-7B-Instruct GGUF
```

后续 FastAPI 后端将通过 OpenAI Compatible API 与本地模型通信，无需直接调用 `llama.cpp`。

---

## 6. 注意事项

- 调用接口前，请确保 `llama-server` 已正常启动。
- 默认服务地址：

```text
http://127.0.0.1:8080
```

- 若请求失败，请检查：
  - `llama-server` 是否正在运行；
  - 服务端口是否正确；
  - WSL 网络配置是否正常；
  - 模型是否成功加载。

---

## 7. 本章总结

本章完成了 OpenAI Compatible API 的验证，包括：

- 获取模型列表（`GET /v1/models`）
- 调用聊天接口（`POST /v1/chat/completions`）
- 验证本地模型能够正常响应 HTTP 请求

至此，本地模型已经具备 OpenAI API 兼容能力，为后续 **FastAPI 后端开发** 和 **RAG 问答系统构建** 提供了统一的模型调用接口。

下一章节将介绍 **FastAPI 后端开发**，构建统一的聊天接口、配置管理和业务逻辑。