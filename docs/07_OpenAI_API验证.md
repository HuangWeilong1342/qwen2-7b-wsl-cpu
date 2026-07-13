# 07 OpenAI Compatible API 验证

## 1. 获取模型列表

请求：

```

GET /v1/models

```

PowerShell：

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8080/v1/models"
```

返回：

```

StatusCode : 200

```

说明模型服务正常。

---

## 2. Chat API

请求：

```

POST /v1/chat/completions

```

PowerShell：

```powershell
$body = @{
messages=@(
@{
role="user"
content="你好，请介绍一下你自己。"
}
)
} | ConvertTo-Json -Depth 3

Invoke-RestMethod `
-Uri "http://127.0.0.1:8080/v1/chat/completions" `
-Method Post `
-ContentType "application/json" `
-Body $body
```

返回：

```

object : chat.completion

```

说明 OpenAI Compatible API 调用成功。

---

## 3. 项目架构

```

Browser

↓

FastAPI

↓

OpenAI API

↓

llama-server

↓

Qwen2-7B GGUF

```

---

## 4. 本章总结

完成 OpenAI Compatible API 验证，为后续 FastAPI 和 RAG 系统开发提供接口基础。
