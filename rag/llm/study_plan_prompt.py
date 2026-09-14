class StudyPlanPrompt:

    def build_prompt(
        self,
        subject,
        days,
        context
    ):

        prompt = f"""
You are an AI Study Planner.

Subject:
{subject}

Study Duration:
{days} days

Reference Material:
{context}

Create a {days}-day study plan.

Return ONLY valid JSON.

Example format:

[
    {{
        "day": 1,
        "topic": "Topic Name",
        "goal": "Goal Description"
    }},
    {{
        "day": 2,
        "topic": "Topic Name",
        "goal": "Goal Description"
    }}
]

Do not add explanations.
Do not add markdown.
Return only JSON.
"""

        return prompt