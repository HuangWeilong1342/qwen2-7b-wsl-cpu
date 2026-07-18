# 08 FastAPI 后端开发

## 1. 文档说明

本文档介绍本项目 FastAPI 后端的搭建过程，包括项目目录设计、虚拟环境配置、FastAPI 服务启动以及基础聊天接口的实现，为后续接入本地大语言模型和 RAG 系统奠定基础。

---

## 2. 为什么使用 FastAPI

虽然 `llama-server` 已经提供了 OpenAI Compatible API，但项目仍需要一层业务后端，负责统一管理模型调用和业务逻辑。

FastAPI 在本项目中主要承担以下职责：

- 提供统一 REST API
- 管理请求与响应
- 调用 `llama-server`
- 管理聊天历史
- 后续接入 RAG 检索
- 对接 Vue3 前端

整体架构如下：

```text
Browser / Swagger
        │
        ▼
    FastAPI Backend
        │
        ▼
   OpenAI API
        │
        ▼
   llama-server
        │
        ▼
Qwen2-7B-Instruct
```

---

## 3. 项目目录

新增后端目录：

```text
backend/
├── main.py
├── config.py
├── routers/
├── services/
├── utils/
└── requirements.txt
```

各模块作用如下：

| 文件/目录 | 作用 |
|-----------|------|
| `main.py` | FastAPI 应用入口 |
| `config.py` | 项目统一配置 |
| `routers/` | 路由管理 |
| `services/` | 核心业务逻辑 |
| `utils/` | 工具类（日志等） |
| `requirements.txt` | Python 依赖 |

---

## 4. 创建虚拟环境

创建 Python 虚拟环境：

```bash
python3 -m venv venv
```

激活虚拟环境：

```bash
source venv/bin/activate
```

安装依赖：

```bash
pip install fastapi uvicorn requests
```

导出依赖：

```bash
pip freeze > requirements.txt
```

---

## 5. 创建 FastAPI 应用

创建入口文件：

```text
backend/main.py
```

编写最简单的测试接口：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}
```

启动服务：

```bash
uvicorn backend.main:app --reload
```

默认监听：

```text
http://127.0.0.1:8000
```

浏览器访问：

```text
http://127.0.0.1:8000
```

返回：

```json
{
    "message": "FastAPI is running!"
}
```

说明 FastAPI 已正常启动。

---

## 6. Swagger 接口文档

FastAPI 会自动生成 Swagger 文档。

访问：

```text
http://127.0.0.1:8000/docs
```

即可查看和测试所有 API。

后续开发过程中，所有接口均通过 Swagger 进行调试。

---

## 7. 创建聊天接口

新增聊天接口：

```text
POST /chat
```

请求示例：

```json
{
    "message": "你好"
}
```

返回示例：

```json
{
    "question": "你好",
    "answer": "模型回答"
}
```

当前阶段接口仅完成基础框架，后续将接入 `llama-server` 实现真实的大模型对话。

---

## 8. 本章总结

本章完成了 FastAPI 后端的基础搭建，包括：

- 创建 FastAPI 项目
- 设计后端目录结构
- 配置 Python 虚拟环境
- 启动 FastAPI 服务
- 自动生成 Swagger 文档
- 创建基础聊天接口

至此，后端开发框架已搭建完成。下一章节将介绍 **FastAPI 调用 llama-server**，实现本地大语言模型的真实对话能力。