from fastapi import APIRouter, HTTPException
from bson import ObjectId

from schema.mock_test_schema import MockTestRequest
from schema.test_submit_schema import TestSubmission

from rag.mock_test.test_generator import MockTestGenerator
from assessment.evaluator import TestEvaluator

from database.mock_test_collection import mock_test_collection
from database.test_result_collection import test_result_collection

from assessment.weak_topic_extractor import WeakTopicExtractor

router = APIRouter(
    prefix="/mock-test",
    tags=["Mock Test"]
)

generator = MockTestGenerator()
evaluator = TestEvaluator()
extractor = WeakTopicExtractor()


# =========================
# Generate Mock Test
# =========================

@router.post("/generate")
async def generate_mock_test(
    request: MockTestRequest
):

    questions = generator.generate_test(
        request.student_id,
        request.subject,
        request.difficulty,
        request.num_questions
    )

    if not isinstance(questions, list) or not questions:
        raise HTTPException(
            status_code=502,
            detail="The question generator returned an invalid test."
        )

    test_data = {
        "student_id": request.student_id,
        "subject": request.subject,
        "difficulty": request.difficulty,
        "questions": questions,
        "total_questions": len(questions)
    }

    result = mock_test_collection.insert_one(
        test_data
    )

    return {
        "test_id": str(result.inserted_id),
        "student_id": request.student_id,
        "subject": request.subject,
        "difficulty": request.difficulty,
        "questions": questions
    }


# =========================
# Submit Test
# =========================

@router.post("/submit")
async def submit_test(
    request: TestSubmission
):

    result = evaluator.evaluate(
        request.test_id,
        request.answers
    )

    if not result:
        return {
            "message": "Test not found"
        }

    weak_topics = extractor.extract(
        result["wrong_questions"]
    )

    # Prevent duplicate submissions
    existing = test_result_collection.find_one({
        "student_id": request.student_id,
        "test_id": request.test_id
    })

    if existing:
        return {
            "message": "Test already submitted"
        }

    # Fetch original test details
    test = mock_test_collection.find_one(
        {"_id": ObjectId(request.test_id)}
    )

    test_result_collection.insert_one({

    "student_id": request.student_id,

    "test_id": request.test_id,

    "subject": result["subject"],

    "score": result["score"],

    "total": result["total"],

    "percentage": result["percentage"],

    "wrong_questions": result["wrong_questions"],

    "weak_topics": weak_topics
})

    return {
    "score": result["score"],
    "total": result["total"],
    "percentage": result["percentage"],
    "weak_topics": weak_topics
}


# =========================
# Test History
# =========================

@router.get("/history/{student_id}")
async def get_test_history(
    student_id: str
):

    history = list(
        test_result_collection.find(
            {"student_id": student_id},
            {"_id": 0}
        )
    )

    return history