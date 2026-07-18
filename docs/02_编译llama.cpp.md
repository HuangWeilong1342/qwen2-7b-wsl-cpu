# 02 编译 llama.cpp

## 1. 文档说明

本文档介绍 `llama.cpp` 的源码获取、编译过程及常见问题处理，完成后即可获得本地推理所需的可执行程序。

---

## 2. 获取源码

首先创建项目工作目录：

```bash
mkdir -p ~/llm_lab

cd ~/llm_lab
```

克隆 `llama.cpp` 官方仓库：

```bash
git clone https://github.com/ggml-org/llama.cpp.git

cd llama.cpp
```

> **说明：**
>
> `llama.cpp` 是由 **ggml-org** 维护的开源大语言模型推理框架，支持 CPU、CUDA、Metal、OpenCL 等多种推理后端，并支持 GGUF 模型格式。

---

## 3. 编译项目

使用 CMake 生成构建目录：

```bash
cmake -B build
```

开始编译：

```bash
cmake --build build -j
```

其中：

- `-B build`：指定构建目录
- `-j`：使用多线程编译（默认使用所有 CPU 核心）

编译完成后，所有可执行程序都会生成到：

```text
build/bin/
```

---

## 4. 验证编译结果

查看生成的可执行文件：

```bash
ls build/bin
```

正常情况下，可以看到类似输出：

```text
llama-cli
llama-server
llama-bench
llama-quantize
...
```

其中常用工具如下：

| 工具 | 作用 |
|------|------|
| `llama-cli` | 命令行交互推理 |
| `llama-server` | 启动 OpenAI Compatible API 服务 |
| `llama-bench` | 模型性能测试 |
| `llama-quantize` | 模型量化工具 |

说明编译成功。

---

## 5. 常见问题

### 问题一：运行 `llama-cli` 提示找不到动态库

报错信息：

```text
./build/bin/llama-cli: error while loading shared libraries:
libllama-cli-impl.so: cannot open shared object file
```

#### 原因

新版 `llama.cpp` 将部分功能拆分为动态库（`.so` 文件），Linux 默认不会自动搜索 `build/bin` 目录，因此运行程序时无法找到相关动态库。

#### 临时解决方案

执行：

```bash
export LD_LIBRARY_PATH=$HOME/llm_lab/llama.cpp/build/bin:$LD_LIBRARY_PATH
```

重新运行：

```bash
./build/bin/llama-cli --help
```

若正常输出帮助信息，则问题已解决。

#### 永久生效

将环境变量写入 `~/.bashrc`：

```bash
echo 'export LD_LIBRARY_PATH=$HOME/llm_lab/llama.cpp/build/bin:$LD_LIBRARY_PATH' >> ~/.bashrc
```

刷新配置：

```bash
source ~/.bashrc
```

---

### 问题二：编译速度较慢

首次编译需要较长时间，属于正常现象。

建议：

- 保持默认多线程编译（`-j`）
- 确保 WSL2 分配足够的 CPU 和内存资源

---

## 6. 本章总结

本章完成了 `llama.cpp` 的源码下载与编译，成功生成了本地推理所需的核心工具，包括：

- `llama-cli`
- `llama-server`
- `llama-bench`
- `llama-quantize`

至此，`llama.cpp` 已成功编译完成。下一章节将介绍 **Qwen2 GGUF 模型的下载与部署**。