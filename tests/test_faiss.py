from backend.services.loader import load_pdf
from backend.services.splitter import split_text
from backend.services.embedding import EmbeddingModel
from backend.services.vector_store import VectorStore


def main():
    # 1. 加载 PDF
    text = load_pdf("data/pdf/test.pdf")

    # 2. 切分
    chunks = split_text(text)

    print(f"Chunks: {len(chunks)}")

    # 3. Embedding
    embedding_model = EmbeddingModel()

    embeddings = embedding_model.encode(chunks)

    # 4. 建立索引
    store = VectorStore()

    store.build_index(chunks, embeddings)

    # 5. 保存
    store.save_index()

    # 6. 加载
    store.load_index()

    # 7. 查询
    question = "介绍一下这份PDF"

    query_embedding = embedding_model.encode([question])[0]

    results = store.search(query_embedding)

    print("\n===== Search Result =====")

    for i, chunk in enumerate(results, start=1):
        print(f"\nTop {i}")
        print(chunk)


if __name__ == "__main__":
    main()
