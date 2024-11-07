import faiss
import openai
import numpy as np

class EmbeddingsFAISS:
    def __init__(self, dim=1536):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)  # Flat L2 index for CPU
        self.embeddings = []
        self.ids = []

    def add_document(self, doc_id, content):
        embedding = self.get_embedding(content)
        self.index.add(np.array([embedding], dtype=np.float32))
        self.embeddings.append(embedding)
        self.ids.append(doc_id)
        
    def get_embedding(self, content):
        response = openai.Embedding.create(input=content, model="text-embedding-ada-002")
        return np.array(response["data"][0]["embedding"], dtype=np.float32)

    def search(self, query, top_k=5):
        query_embedding = self.get_embedding(query)
        D, I = self.index.search(np.array([query_embedding]), top_k)
        
        results = [{"doc_id": self.ids[idx], "score": D[0][i]} for i, idx in enumerate(I[0]) if idx != -1]
        return results

# Singleton instance
embeddings_faiss = EmbeddingsFAISS()

def search_with_embeddings(query):
    return embeddings_faiss.search(query)