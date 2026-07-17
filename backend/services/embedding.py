from sentence_transformers import SentenceTransformer

from backend.utils.logger import logger


class EmbeddingModel:
    def __init__(self):
        logger.info("Loading embedding model...")

        self.model = SentenceTransformer(
         "/home/yebai/llm_lab/models/bge-small-zh-v1.5"
        )

        logger.info("Embedding model loaded.")

    def encode(self, texts):
        """
        将文本编码为向量
        """
        return self.model.encode(
            texts,
            normalize_embeddings=True
        )
