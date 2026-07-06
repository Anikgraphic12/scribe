from groq import Groq
from src.config import GROQ_API_KEY, GROQ_MODEL_STT

client = Groq(api_key=GROQ_API_KEY)


def transcribe_audio(file_path: str) -> str:
    try:
        with open(file_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                file=audio_file,
                model=GROQ_MODEL_STT
            )

        return response.text

    except FileNotFoundError:
        raise FileNotFoundError("Fichier audio introuvable")

    except Exception as e:
        raise RuntimeError(f"Erreur transcription: {e}")