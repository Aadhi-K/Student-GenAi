from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("gemini_key")

if not api_key:
    raise ValueError("gemini_key not found in .env")

client = genai.Client(
    api_key=api_key
)