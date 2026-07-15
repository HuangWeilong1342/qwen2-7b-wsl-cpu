# Scripts

本目录存放项目开发过程中使用的自动化脚本，用于快速编译、运行和测试本地部署的大模型。

## 文件说明

| Script | 功能 |
|---------|------|
| build.sh | 编译最新版 llama.cpp |
| benchmark.sh | 测试 Qwen2-7B CPU 推理性能 |
| chat.sh | 启动 llama-cli 命令行聊天 |
| server.sh | 启动 OpenAI Compatible API 服务（llama-server） |
| run.sh | 项目启动入口（预留，后续支持一键启动） |

---

## 使用方法

### 编译 llama.cpp

```bash
./scripts/build.sh
```

---

### Benchmark

```bash
./scripts/benchmark.sh
```

---

### 命令行聊天

```bash
./scripts/chat.sh
```

---

### 启动 API 服务

```bash
./scripts/server.sh
```

默认监听：

```
http://127.0.0.1:8080
```

---

### FastAPI

目前需要手动启动：

```bash
cd backend

source venv/bin/activate

uvicorn main:app --reload
```

浏览器访问：

```
http://127.0.0.1:8000/docs
```

---

## 后续计划

后续将完善：

```
run.sh
```

实现：

- 自动启动 llama-server
- 自动启动 FastAPI
- （后续）自动启动 Vue 前端
- 一键运行整个本地 AI 系统
