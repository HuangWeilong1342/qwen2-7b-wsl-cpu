# Tests

本目录包含项目各模块的功能验证脚本。

## 测试内容

- test_loader.py：PDF 加载测试
- test_splitter.py：文本切分测试
- test_embedding.py：Embedding 向量生成测试
- test_vector_store.py：FAISS 向量库测试
- test_retriever.py：向量检索测试
- test_rag.py：RAG Prompt 构建测试
- test_chat.py：LLM 对话测试

运行示例：

```bash
python tests/test_loader.py
python tests/test_chat.py
