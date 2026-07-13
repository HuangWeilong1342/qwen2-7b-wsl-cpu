# 06 llama-server 部署

## 1. 简介

llama-server 可以将本地模型部署为 HTTP 服务，并提供 OpenAI Compatible API。

项目架构：

```

Browser

↓

FastAPI

↓

llama-server

↓

Qwen2 GGUF

```

---

## 2. 启动

```bash
./build/bin/llama-server \
-m models/qwen2-7b-instruct-q4_k_m.gguf \
-t 8 \
--host 127.0.0.1 \
--port 8080
```

---

## 3. 成功启动

浏览器访问：

```

http://127.0.0.1:8080

```

服务器正常运行。

---

## 4. 本章总结

成功完成本地 AI 服务部署。
