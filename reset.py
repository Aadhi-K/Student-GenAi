import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

client.delete_collection(
    name="education_copilot"
)

print("Collection deleted successfully.")