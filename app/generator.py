import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set. Set it in your environment.")

if not GEMINI_MODEL:
    raise RuntimeError("GEMINI_MODEL not set. Set it in your environment.")
client = genai.Client(api_key=GEMINI_API_KEY)

def compose_prompt(title: str, details: str = "") -> str:
    template = (
        f"Write a well-structured, developer-focused blog article titled \"{title}\"."
        " The audience: intermediate software engineers."
        " Include a short introduction, 3–6 subsections with code examples where appropriate,"
        " a short conclusion, and a concise 2-line summary at the end."
    )
    if details:
        template += f" Use these details as constraints or focus areas: {details}."
    template += (
        " Use markdown formatting (headers, code fences, bullets) and keep length ~600–1200 words."
    )
    return template


def summarize_short(long_text: str) -> str:
    return (long_text[:300] + "...") if len(long_text) > 300 else long_text

def call_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config={
                "temperature": 0.3,
                "max_output_tokens": 2500,
            },
        )
        print("Full Gemini response:", response.__dict__)
    except Exception as e:
        print("Gemini API call failed:", e)
        return f"Gemini API call failed: {e}"

    if getattr(response, "text", None):
        return response.text.strip()

    candidates = getattr(response, "candidates", None)
    if candidates:
        for c in candidates:
            if getattr(c, "content", None):
                parts = getattr(c.content, "parts", [])
                if parts:
                    text = "".join([getattr(p, "text", "") for p in parts])
                    if text.strip():
                        return text.strip()

    return "Gemini returned no usable text."

