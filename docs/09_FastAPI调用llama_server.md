# 09 FastAPI 调用 llama-server

## 目标

通过 FastAPI 调用本地部署的 `llama-server`，实现统一的大模型访问接口。

整体流程：

```
Browser

↓

FastAPI

↓

requests

↓

llama-server

↓

Qwen2
```

---

## llama-server

启动：

```
./scripts/server.sh
```

启动成功后：

```
http://127.0.0.1:8080
```

开放：

```
/v1/models

/v1/chat/completions
```

OpenAI Compatible API。

---

## 调用接口

FastAPI 使用：

```
requests.post()
```

请求：

```
http://127.0.0.1:8080/v1/chat/completions
```

请求体：

```json
{
    "messages":[
        {
            "role":"user",
            "content":"你好"
        }
    ]
}
```

---

## 返回结果

llama-server 返回：

```json
{
    "choices":[
        {
            "message":{
                "content":"你好！很高兴为你提供帮助。"
            }
        }
    ]
}
```

FastAPI 提取：

```
choices[0].message.content
```

统一返回：

```json
{
    "question":"你好",
    "answer":"你好！很高兴为你提供帮助。"
}
```

---

## 调试过程

开发过程中出现：

```
Connection refused
```

原因：

```
llama-server
```

未启动，8080 无监听。

通过：

```
ss -ltnp | grep 8080
```

确认问题。

重新启动：

```
./scripts/server.sh
```

问题解决。

---

## 最终效果

浏览器访问：

```
http://127.0.0.1:8000/docs
```

调用：

```
POST /chat
```

即可得到 Qwen2-7B 的真实回答。

说明：

FastAPI 与 llama-server 联调成功。
