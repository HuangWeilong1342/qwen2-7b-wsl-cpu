from backend.services.prompt import build_prompt
from backend.services.retriever import Retriever


class RAGService:

    def __init__(self):
        self.retriever = Retriever()

    def build_prompt(self, question: str) -> str:
        """
        根据用户问题生成 RAG Prompt
        """

        chunks = self.retriever.retrieve(question)

        context = "\n\n".join(chunks)

        return build_prompt(
            question=question,
            context=context
        )

