from pathlib import Path

from backend.services.loader import load_pdf
from backend.services.splitter import split_text
from backend.services.embedding import EmbeddingModel
from backend.services.vector_store import VectorStore

PDF_DIR = Path("data/pdf")

def build_index():
    all_chunks = []

    # 遍历 data/pdf 下所有 PDF
    for pdf in PDF_DIR.glob("*.pdf"):
        print(f"Loading {pdf.name}")

        text = load_pdf(str(pdf))

        chunks = split_text(text)

        all_chunks.extend(chunks)

    # 如果没有 PDF
    if not all_chunks:
        print("No PDF files found.")
        return

    # Embedding
    embedding_model = EmbeddingModel()
    embeddings = embedding_model.encode(all_chunks)

    # 建立索引
    vector_store = VectorStore()
    vector_store.build_index(all_chunks, embeddings)
    vector_store.save_index()

    print("Index build successfully!")
    print(f"Total Chunks: {len(all_chunks)}")


if __name__ == "__main__":
    build_index()
