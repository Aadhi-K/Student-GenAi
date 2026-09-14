from pydantic import BaseModel
from typing import List


class TestSubmission(BaseModel):
    test_id: str
    student_id: str
    answers: List[str]