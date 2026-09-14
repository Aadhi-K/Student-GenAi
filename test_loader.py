from rag.ingestion.pdf_loader import PDFLoader
from rag.ingestion.text_extraction import extract_text
from rag.ingestion.table_extraction import TableExtractor
from rag.process.chunk import TextChunker
from rag.embeding.embeding import EmbeddingGenerator
from rag.vectorDB.vector_store import ChromaStore


PDF_PATH = "quantum.pdf"


# 1. Load
loader = PDFLoader(PDF_PATH)
loaded_pdf = loader.load()


# 2. Extract normal text
text_pages = extract_text(loaded_pdf)


# 3. Extract tables
table_extractor = TableExtractor(PDF_PATH)
tables = table_extractor.extract_tables()


# 4. Chunk
chunker = TextChunker()

chunks = chunker.create_chunks(text_pages,loaded_pdf["filename"])


# 5. Check
print("Total chunks:", len(chunks))
print("Source :",chunks[0]["source"])

for i, chunk in enumerate(chunks[:5], start=1):
    print("\n" + "=" * 60)
    print("CHUNK:", i)
    print("PAGE:", chunk["page_number"])
    print("=" * 60)
    print("Source :",chunk["source"])
    print(chunk["text"][:500])

embedder = EmbeddingGenerator()

embeddings = embedder.generate_embeddings(chunks)

print("Chunks:", len(chunks))
print("Embeddings:", len(embeddings))
print("Vector size:", len(embeddings[0]))

# 6. Store in ChromaDB

store = ChromaStore()

store.store_chunks(
    chunks,
    embeddings
)

# 6. Close PDF
loaded_pdf["pdf"].close()