from backend.services.loader import load_pdf

text = load_pdf("data/pdf/test.pdf")

print("=" * 50)
print("前500个字符：")
print(text[:500])
print("=" * 50)
print(f"总字符数：{len(text)}")

