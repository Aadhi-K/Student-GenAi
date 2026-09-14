from fastapi import APIRouter
import json

from schema.study_plan_schema import StudyPlanRequest

from rag.retrival.retrival import Retriever
from rag.llm.study_plan_prompt import StudyPlanPrompt
from rag.llm.gemini import GeminiClient

router = APIRouter(
    prefix="/study-plan",
    tags=["Study Planner"]
)

@router.post("/generate")
async def generate_plan(
    request: StudyPlanRequest
):

    docs = retriever.search(
        request.subject,
        request.student_id,
        top_k=3
    )

    context = "\n".join(
        docs["documents"][0]
    )

    prompt = prompt_builder.build_prompt(
        request.subject,
        request.days,
        context
    )

    plan = gemini.generate_answer(
        prompt
    )

    try:

        study_plan = json.loads(plan)

    except:

        study_plan = plan

    return {
    "subject": request.subject,
    "days": request.days,
    "study_plan": study_plan
    }

retriever = Retriever()
prompt_builder = StudyPlanPrompt()
gemini = GeminiClient()