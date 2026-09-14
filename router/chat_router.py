from fastapi import APIRouter

from schema.chat_schema import ChatRequest

from rag.retrival.retrival import Retriever
from rag.llm.prompt_builder import PromptBuilder
from rag.llm.gemini import GeminiClient


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

retriever = Retriever()
prompt_builder = PromptBuilder()
gemini = GeminiClient()


@router.post("/local")
async def local_chat(request: ChatRequest):

    retrieved_docs = retriever.search(
        request.question,
        request.student_id,
        top_k=3
    )

    # No matching PDF content found
    if not retrieved_docs["documents"][0]:
        return {
            "question": request.question,
            "answer": "No relevant content found in your uploaded PDFs."
        }

    context = retrieved_docs["documents"][0][0]

    prompt = prompt_builder.build_prompt(
        request.question,
        context
    )

    answer = gemini.generate_answer(
        prompt
    )

    return {
        "question": request.question,
        "answer": answer
    }