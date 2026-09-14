class PromptBuilder:

    @staticmethod
    def build_prompt(question, retrieved_chunks):

        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
You are an educational assistant.

Answer ONLY using the provided context.

If mathematical expressions are present,
explain them in simple student-friendly language.

If the answer is not present in the context, say:
"I could not find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

        return prompt