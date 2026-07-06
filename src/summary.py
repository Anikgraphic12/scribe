from groq import Groq
from src.config import GROQ_API_KEY, GROQ_MODEL_LLM

client = Groq(api_key=GROQ_API_KEY)


def generate_summary(transcription: str, system_prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL_LLM,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": transcription}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        raise RuntimeError(f"Erreur LLM: {e}")