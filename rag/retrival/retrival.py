import chromadb
from shared.shared_models import embedding_model

class Retriever:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_collection(
            name="education_copilot"
        )

        self.embedding_model = embedding_model

    def search(self,query,student_id,top_k=3):

        query_embedding = self.embedding_model.encode(
            query
        ).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where={"student_id": student_id})

        return results