from rag.retrival.retrival import Retriever
from rag.llm.prompt_builder import PromptBuilder
from rag.llm.gemini import GeminiClient
from rag.llm.response_cleaner import clean_response


retriever = Retriever()
question = input("Question: ")
results = retriever.search(
    question,
    top_k=3
)

chunks = results["documents"][0]


prompt = PromptBuilder.build_prompt(
    question,
    chunks
)


gemini = GeminiClient()

answer = gemini.generate_answer(prompt)

answer = clean_response(answer)

print("\nAnswer:\n")
print(answer)