import re


def clean_response(text: str) -> str:

    # Remove bold / italic markdown
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*(?!\*)", "", text)

    # Remove markdown headings
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Remove markdown code fences
    text = re.sub(r"```(?:\w+)?", "", text)

    # Remove inline code backticks
    text = text.replace("`", "")

    return text.strip()