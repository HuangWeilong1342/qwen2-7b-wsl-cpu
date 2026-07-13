# 02 编译 llama.cpp

## 获取源码

创建工作目录：

```bash
mkdir -p ~/qwen_lab

cd ~/qwen_lab
```

克隆官方仓库：

```bash
git clone https://github.com/ggml-org/llama.cpp.git

cd llama.cpp
```

## 编译项目

生成 build 目录：

```bash
cmake -B build
```

开始编译：

```bash
cmake --build build -j
```

## 编译结果

编译完成后：

```bash
ls build/bin
```

可看到：

```
llama-cli
llama-server
llama-bench
llama-quantize
```

## 常见问题

### 问题：运行 `llama-cli` 提示找不到动态库

```text
./build/bin/llama-cli: error while loading shared libraries:
libllama-cli-impl.so: cannot open shared object file
```

原因：

新版 `llama.cpp` 使用动态库，Linux 默认不会自动搜索 `build/bin` 目录。

解决方法：

```bash
export LD_LIBRARY_PATH=$HOME/qwen_lab/llama.cpp/build/bin:$LD_LIBRARY_PATH
```

为了永久生效，可将上述命令写入 `~/.bashrc`：

```bash
echo 'export LD_LIBRARY_PATH=$HOME/qwen_lab/llama.cpp/build/bin:$LD_LIBRARY_PATH' >> ~/.bashrc

source ~/.bashrc
```

## 本章总结

成功完成 llama.cpp 编译，并生成相关可执行程序。
