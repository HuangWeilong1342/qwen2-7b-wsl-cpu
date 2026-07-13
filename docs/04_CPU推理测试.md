# 04 CPU 推理测试

## 启动模型

进入项目目录：

```bash
cd ~/qwen_lab/llama.cpp
```

运行：

```bash
./build/bin/llama-cli \
-m ../models/qwen2-7b-instruct-q4_k_m.gguf \
-cnv \
-t 8
```

## 参数说明

| 参数 | 说明 |
|------|------|
| -m | 模型路径 |
| -cnv | 聊天模式 |
| -t | CPU 线程数 |

## 推理测试

输入：

```
你好
```

模型成功返回回答，说明本地 CPU 推理成功。

## 本章总结

成功完成 Qwen2-7B 的本地 CPU 推理。
