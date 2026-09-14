from shared.shared_gemini import client


class GeminiClient:

    def __init__(self):
        self.client = client
        self.model = "gemini-flash-lite-latest"

    def generate_answer(self, prompt):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text