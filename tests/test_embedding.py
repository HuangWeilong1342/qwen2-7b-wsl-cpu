from backend.services.loader import load_pdf
from backend.services.splitter import split_text
from backend.services.embedding import EmbeddingModel

# 读取 PDF
text = load_pdf("data/pdf/test.pdf")

# 切分
chunks = split_text(text)

# 加载模型
model = EmbeddingModel()

# 编码
embeddings = model.encode(chunks)

print(f"Chunk 数量：{len(chunks)}")
print(f"Embedding 数量：{len(embeddings)}")
print(f"单个向量维度：{len(embeddings[0])}")

print("\n第一个 Chunk：")
print(chunks[0][:100])

print("\n前10维向量：")
print(embeddings[0][:10])
