from backend.services.rag import RAGService


def main():
    rag = RAGService()

    question = "什么是人工智能？"

    prompt = rag.build_prompt(question)

    print(prompt)


if __name__ == "__main__":
    main()
