# 03 Qwen2 GGUF 模型部署

## 1. 文档说明

本文档介绍 Qwen2-7B-Instruct GGUF 模型的下载、目录组织及加载方式，为后续本地推理和 API 服务部署做好准备。

---

## 2. 模型介绍

本项目使用 **Qwen2-7B-Instruct** 指令微调模型。

模型特点：

- 参数规模：7B
- 支持中英文对话
- 支持 GGUF 格式
- 可通过 `llama.cpp` 在 CPU 上运行

为了兼顾推理速度和模型效果，本项目采用 **Q4_K_M** 量化版本。

推荐模型：

```text
qwen2-7b-instruct-q4_k_m.gguf
```

---

## 3. 下载模型

模型官方发布地址：

> https://huggingface.co/Qwen/Qwen2-7B-Instruct-GGUF

根据实际需求下载对应量化版本。

本项目推荐：

```text
qwen2-7b-instruct-q4_k_m.gguf
```

> **说明：**
>
> 不同量化版本在模型大小、推理速度和回答质量之间存在差异。
>
> `Q4_K_M` 在 CPU 推理场景下具有较好的综合表现，因此选择该版本。

---

## 4. 模型目录

建议将模型统一放在项目根目录下的 `models` 文件夹：

```text
~/llm_lab/
├── llama.cpp/
└── models/
    └── qwen2-7b-instruct-q4_k_m.gguf
```

其中：

| 目录 | 作用 |
|------|------|
| `llama.cpp` | 推理框架源码 |
| `models` | 存放所有 GGUF 模型 |

> **说明：**
>
> 模型文件通常较大（数 GB），建议不要上传至 GitHub，可通过 `.gitignore` 忽略 `models/` 目录。

---

## 5. 加载模型

进入 `llama.cpp` 目录：

```bash
cd ~/llm_lab/llama.cpp
```

加载模型：

```bash
./build/bin/llama-cli \
    -m ../models/qwen2-7b-instruct-q4_k_m.gguf
```

如果希望进入交互式聊天模式，可添加 `-cnv` 参数：

```bash
./build/bin/llama-cli \
    -m ../models/qwen2-7b-instruct-q4_k_m.gguf \
    -cnv
```

如果需要指定 CPU 线程数，例如使用 8 个线程：

```bash
./build/bin/llama-cli \
    -m ../models/qwen2-7b-instruct-q4_k_m.gguf \
    -cnv \
    -t 8
```

---

## 6. 验证模型加载

模型加载成功后，终端会输出类似信息：

```text
load model

...

system_info

...

>
```

随后即可输入问题进行测试，例如：

```text
你好，请介绍一下你自己。
```

如果模型能够正常回答，则说明部署成功。

---

## 7. 本章总结

本章完成了 Qwen2 GGUF 模型的部署，包括：

- 下载官方 GGUF 模型
- 建立模型目录
- 使用 `llama-cli` 加载模型
- 验证模型能够正常运行

至此，本地大语言模型已经成功部署。下一章节将进行 **CPU 推理测试**，验证模型的实际运行效果和性能。