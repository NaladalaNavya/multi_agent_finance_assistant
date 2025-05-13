from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrieverAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # 384 for MiniLM
        self.docs = []

    def index_documents(self, docs):
        embeddings = self.model.encode(docs)
        self.index.add(np.array(embeddings))
        self.docs = docs

    def retrieve(self, query, top_k=3):
        embedding = self.model.encode([query])
        D, I = self.index.search(np.array(embedding), top_k)
        return [self.docs[i] for i in I[0]]
