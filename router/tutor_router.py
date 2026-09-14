from fastapi import APIRouter
from schema.tutor_schema import TutorRequest
from rag.llm.gemini import GeminiClient

router = APIRouter(
    prefix="/tutor",
    tags=["Global Tutor"]
)

gemini = GeminiClient()
@router.post("/ask")
async def ask_global_tutor(request: TutorRequest):

    answer = gemini.generate_answer(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }