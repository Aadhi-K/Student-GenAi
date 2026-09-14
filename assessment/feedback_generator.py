from assessment.performance import PerformanceAnalyzer
from assessment.weak_topics import WeakTopicsAnalyzer

from rag.llm.gemini import GeminiClient


class FeedbackGenerator:

    def __init__(self):

        self.performance = PerformanceAnalyzer()
        self.weak_topics = WeakTopicsAnalyzer()
        self.gemini = GeminiClient()

    def generate_feedback(self, student_id):

        performance = self.performance.get_student_performance(
            student_id
        )

        if "message" in performance:
            return performance

        weak_topics = self.weak_topics.get_weak_topics(
            student_id
        )

        prompt = f"""
You are an experienced academic mentor.

Student Performance:

Average Score:
{performance["average_score"]}

Best Score:
{performance["best_score"]}

Lowest Score:
{performance["lowest_score"]}

Tests Taken:
{performance["tests_taken"]}

Weak Topics:
{weak_topics["weak_topics"]}

Generate:

1. Performance Summary
2. Strengths
3. Weak Areas
4. Improvement Advice
5. Motivation Message

Keep response under 200 words.
"""

        feedback = self.gemini.generate_answer(
            prompt
        )

        return {
            "student_id": student_id,
            "average_score": performance["average_score"],
            "feedback": feedback
        }