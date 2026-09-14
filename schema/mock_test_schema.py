from pydantic import BaseModel


class MockTestRequest(BaseModel):

    student_id: str
    subject: str
    difficulty: str
    num_questions: int