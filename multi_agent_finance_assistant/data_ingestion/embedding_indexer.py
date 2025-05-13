from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class EmbeddingIndexer:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.doc_store = []

    def add_documents(self, docs: list):
        embeddings = self.model.encode(docs)
        self.index.add(np.array(embeddings))
        self.doc_store.extend(docs)

    def search(self, query: str, top_k: int = 3) -> list:
        query_emb = self.model.encode([query])
        D, I = self.index.search(np.array(query_emb), top_k)
        return [self.doc_store[i] for i in I[0]]
