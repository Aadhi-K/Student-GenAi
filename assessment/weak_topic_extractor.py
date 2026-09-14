import json

from rag.llm.gemini import GeminiClient


class WeakTopicExtractor:

    def __init__(self):

        self.gemini = GeminiClient()

    def extract(self, wrong_questions):

        if not wrong_questions:
            return []

        prompt = f"""
You are an educational expert.

Analyze the student's incorrect answers.

Wrong Questions:

{wrong_questions}

Identify the concepts/topics that the student is weak in.

Return ONLY valid JSON.

Example:

[
    "Quantum Entanglement",
    "Wave Functions",
    "Schrodinger Equation"
]
"""

        response = self.gemini.generate_answer(
            prompt
        )

        try:
            return json.loads(response)

        except Exception:
            return []