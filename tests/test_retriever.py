from backend.services.retriever import Retriever


def main():
    retriever = Retriever()

    question = "什么是人工智能？"

    results = retriever.retrieve(question)

    print("\n===== Retriever Result =====")

    for i, text in enumerate(results, start=1):
        print(f"\nTop {i}")
        print(text)


if __name__ == "__main__":
    main()
