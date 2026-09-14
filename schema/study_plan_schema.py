from pydantic import BaseModel


class StudyPlanRequest(BaseModel):
    student_id: str
    subject: str
    days: int