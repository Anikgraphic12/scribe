import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# modèles centralisés (TP requirement)
GROQ_MODEL_STT = "whisper-large-v3"
GROQ_MODEL_LLM = "llama-3.1-70b-versatile"

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY manquante dans le fichier .env")