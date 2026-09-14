import os

from datetime import datetime

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from rag.ingestion.pdf_loader import PDFLoader
from rag.ingestion.text_extraction import extract_text
from rag.process.chunk import TextChunker
from rag.embeding.embeding import EmbeddingGenerator
from rag.vectorDB.vector_store import ChromaStore

from database.pdf_collection import pdf_collection


router = APIRouter(
    prefix="/pdf",
    tags=["PDF"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.get("/history/{student_id}")
async def get_pdf_history(student_id: str):

    pdfs = list(
        pdf_collection.find(
            {"student_id": student_id},
            {"_id": 0}
        ).sort(
            "upload_date",
            -1
        )
    )

    return pdfs


@router.post("/upload")
async def upload_pdf(
    student_id: str = Form(...),
    file: UploadFile = File(...)
):

    # Save PDF with student id
    file_path = os.path.join(
        UPLOAD_FOLDER,
        f"{student_id}_{file.filename}"
    )

    with open(file_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    print(f"PDF Saved : {file_path}")

    # ==========================
    # PDF LOADING
    # ==========================

    loader = PDFLoader(file_path)

    loaded_pdf = loader.load()

    print("PDF Loaded Successfully")

    # ==========================
    # TEXT EXTRACTION
    # ==========================

    text_pages = extract_text(
        loaded_pdf
    )

    print(
        "Pages Extracted :",
        len(text_pages)
    )

    # ==========================
    # CHUNKING
    # ==========================

    chunker = TextChunker()

    chunks = chunker.create_chunks(
        text_pages,
        loaded_pdf["filename"]
    )

    print(
        "Chunks Created :",
        len(chunks)
    )

    # ==========================
    # EMBEDDINGS
    # ==========================

    embedder = EmbeddingGenerator()

    embeddings = embedder.generate_embeddings(
        chunks
    )

    print(
        "Embeddings Created :",
        len(embeddings)
    )

    # ==========================
    # CHROMADB STORAGE
    # ==========================

    chroma_store = ChromaStore()

    chroma_store.store_chunks(
        chunks,
        embeddings,
        student_id
    )

    print(
        "Stored in ChromaDB for",
        student_id
    )

    # ==========================
    # MONGODB STORAGE
    # ==========================

    pdf_collection.insert_one(
        {
            "student_id": student_id,
            "filename": file.filename,
            "upload_date": datetime.utcnow(),
            "total_chunks": len(chunks),
            "status": "indexed"
        }
    )

    print(
        "Stored in MongoDB"
    )

    # Close PDF
    loaded_pdf["pdf"].close()

    return {
        "message": "PDF Uploaded and Indexed Successfully",
        "student_id": student_id,
        "filename": file.filename,
        "chunks": len(chunks)
    }