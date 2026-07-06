from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def transcribe_audio(file_path: str) -> str:
    """
    Transcrit un fichier audio en texte via Groq STT
    """

    try:
        with open(file_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                language="fr"
            )

        return response.text

    except FileNotFoundError:
        raise FileNotFoundError("Fichier audio introuvable")

    except Exception as e:
        raise RuntimeError(f"Erreur API transcription: {e}")