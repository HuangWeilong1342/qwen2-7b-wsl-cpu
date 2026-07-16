from backend.services.loader import load_pdf
from backend.services.splitter import split_text

text = load_pdf("data/pdf/test.pdf")

chunks = split_text(text)

print(f"共切分出 {len(chunks)} 个 Chunk")

print("=" * 50)

print(chunks[0])

print("=" * 50)

print(len(chunks[0]))
