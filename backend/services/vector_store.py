import os
import pickle

import faiss
import numpy as np

from backend.utils.logger import logger


class VectorStore:
    """
    FAISS 向量数据库
    """

    def __init__(self):
        self.index = None
        self.chunks = []

    def build_index(self, chunks, embeddings):
        """
        构建 FAISS 索引

        Args:
            chunks (list[str]): 文本块
            embeddings (np.ndarray): 文本向量
        """

        logger.info("Building FAISS index...")

        self.chunks = chunks

        vectors = np.asarray(embeddings, dtype=np.float32)

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(vectors)

        logger.info(f"Vector dimension: {dimension}")
        logger.info(f"Total chunks: {len(chunks)}")
        logger.info("FAISS index built successfully.")

    def save_index(
        self,
        index_path="data/index.faiss",
        chunk_path="data/chunks.pkl",
    ):
        """
        保存索引和文本块
        """

        os.makedirs(os.path.dirname(index_path), exist_ok=True)

        faiss.write_index(self.index, index_path)

        with open(chunk_path, "wb") as f:
            pickle.dump(self.chunks, f)

        logger.info("FAISS index saved.")

    def load_index(
        self,
        index_path="data/index.faiss",
        chunk_path="data/chunks.pkl",
    ):
        """
        加载索引和文本块
        """

        self.index = faiss.read_index(index_path)

        with open(chunk_path, "rb") as f:
            self.chunks = pickle.load(f)

        logger.info("FAISS index loaded.")

    def search(self, query_embedding, top_k=3):
        """
        相似度搜索

        Args:
            query_embedding: 查询向量
            top_k (int): 返回数量

        Returns:
            list[str]
        """

        if self.index is None:
            raise RuntimeError("FAISS index has not been loaded.")

        query = np.asarray([query_embedding], dtype=np.float32)

        distances, indices = self.index.search(query, top_k)

        results = []

        for idx in indices[0]:
            if 0 <= idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results
