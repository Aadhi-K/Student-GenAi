import chromadb
import uuid


class ChromaStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="education_copilot"
        )

    def store_chunks(
        self,
        chunks,
        embeddings,
        student_id
    ):

        ids = []
        documents = []
        metadatas = []

        upload_id = str(uuid.uuid4())[:8]

        for index, chunk in enumerate(chunks):

            source_name = (
                chunk["source"]
                .replace(".pdf", "")
                .replace(" ", "_")
            )

            chunk_id = (
                f"{upload_id}_"
                f"{source_name}_"
                f"page_{chunk['page_number']}_"
                f"chunk_{index}"
            )

            ids.append(chunk_id)

            documents.append(
                chunk["text"]
            )

            metadatas.append(
                {
                    "student_id": student_id,
                    "page_number": chunk["page_number"],
                    "source": chunk["source"]
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

        print(
            f"{len(chunks)} chunks stored successfully in ChromaDB."
        )