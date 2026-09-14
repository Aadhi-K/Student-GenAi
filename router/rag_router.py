from fastapi import APIRouter

from schema.rag_schema import RAGQuery

from rag.retrival.retrival import Retriever
from rag.llm.prompt_builder import PromptBuilder
from rag.llm.gemini import GeminiClient
from rag.llm.response_cleaner import clean_response


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


retriever = Retriever()
gemini = GeminiClient()


@router.post("/ask")
def ask_question(request: RAGQuery):

    question = request.question

    # 1. Retrieve relevant chunks
    results = retriever.search(
        question,
        request.student_id,
        top_k=3
    )

    chunks = results["documents"][0]

    # 2. Build prompt
    prompt = PromptBuilder.build_prompt(
        question,
        chunks
    )

    # 3. Generate answer
    answer = gemini.generate_answer(
        prompt
    )

    # 4. Clean response
    answer = clean_response(answer)

    return {
        "question": question,
        "answer": answer
    }