from backend.services.embedding import EmbeddingModel
from backend.services.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()
        self.vector_store.load_index()

    def retrieve(self, question: str, top_k: int = 3):
        """
        根据用户问题检索最相关的文本块
        """

        query_embedding = self.embedding_model.encode([question])[0]

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return results
