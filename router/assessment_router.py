from fastapi import APIRouter

from assessment.performance import (PerformanceAnalyzer)

from assessment.analytics import (Analytics)
from assessment.weak_topics import (WeakTopicsAnalyzer)
from assessment.feedback_generator import (FeedbackGenerator)
from assessment.dashboard_analytics import DashboardAnalytics

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"]
)

performance = PerformanceAnalyzer()
analytics = Analytics()
weak_topics = WeakTopicsAnalyzer()
feedback_generator = FeedbackGenerator()
dashboard = DashboardAnalytics()

@router.get("/performance/{student_id}")
async def get_performance(student_id: str):

    return performance.get_student_performance(
        student_id
    )

@router.get("/subjects/{student_id}")
async def get_subject_analytics(
    student_id: str
):

    return analytics.subject_wise_performance(
        student_id
    )
@router.get("/weak-topics/{student_id}")
async def get_weak_topics(
    student_id: str
):

    return weak_topics.get_weak_topics(
        student_id
    )
@router.get("/feedback/{student_id}")
async def get_feedback(
    student_id: str
):

    return feedback_generator.generate_feedback(
        student_id
    )
@router.get("/dashboard/{student_id}")
async def dashboard_data(student_id: str):

    return dashboard.get_dashboard_data(
        student_id
    )