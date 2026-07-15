# 08 FastAPI 开发

## 项目目的

为了方便浏览器或其他客户端调用本地部署的大模型，需要在 `llama-server` 之上增加一层后端服务。

FastAPI 负责：

- 提供统一 REST API
- 管理请求参数
- 后续接入 RAG
- 后续连接 Vue 前端

整体架构如下：

```
Browser

↓

FastAPI

↓

llama-server

↓

Qwen2-7B
```

---

## 创建 backend

项目新增：

```
backend/

main.py
config.py
requirements.txt

routers/
services/
utils/
```

---

## 创建虚拟环境

```
python3 -m venv venv
```

激活：

```
source venv/bin/activate
```

安装：

```
pip install fastapi uvicorn requests
```

导出：

```
pip freeze > requirements.txt
```

---

## 编写 FastAPI

创建：

```
main.py
```

实现：

```
GET /
```

用于测试服务是否正常。

启动：

```
uvicorn main:app --reload
```

浏览器访问：

```
http://127.0.0.1:8000
```

返回：

```json
{
    "message":"FastAPI is running!"
}
```

说明：

FastAPI 已正常运行。

---

## Swagger

FastAPI 自动生成接口文档：

```
http://127.0.0.1:8000/docs
```

方便后续测试所有接口。

---

## 创建 Chat API

新增：

```
POST /chat
```

请求：

```json
{
    "message":"你好"
}
```

返回：

```json
{
    "question":"你好",
    "answer":"模型回答"
}
```

目前已完成 FastAPI 基础开发，为后续调用大模型做好准备。
