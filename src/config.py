import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY manquante dans .env")

STT_MODEL = os.getenv("GROQ_MODEL_STT", "whisper-large-v3")
LLM_MODEL = os.getenv("GROQ_MODEL_LLM", "llama-3.1-70b-versatile")