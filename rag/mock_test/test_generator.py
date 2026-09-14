import json

from rag.retrival.retrival import Retriever
from rag.llm.gemini import GeminiClient


class MockTestGenerator:

    def __init__(self):

        self.retriever = Retriever()
        self.gemini = GeminiClient()

    def generate_test(
        self,
        student_id,
        subject,
        difficulty,
        num_questions
    ):

        docs = self.retriever.search(
            query=subject,
            student_id=student_id,
            top_k=15
        )

        context = "\n".join(
            docs["documents"][0]
        )

        prompt = f"""
You are an expert university professor.

Generate exactly {num_questions} multiple-choice questions.

Subject:
{subject}

Difficulty:
{difficulty}

Study Material:
{context}

IMPORTANT RULES:

1. Questions MUST come ONLY from the study material.
2. Do NOT generate generic questions.
3. Each question must have 4 options.
4. Only ONE correct answer.
5. Cover different topics from the material.
6. Return ONLY valid JSON.
7. Do not include markdown.
8. Do not include explanations.

Output Format:

[
    {{
        "question": "Question text",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "correct_answer": "Option A"
    }}
]
"""

        response = self.gemini.generate_answer(
            prompt
        )

        try:
            return json.loads(response)

        except Exception:

            return {
                "error": "Failed to parse generated MCQs",
                "raw_response": response
            }