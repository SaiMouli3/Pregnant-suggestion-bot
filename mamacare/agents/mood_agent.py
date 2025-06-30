# config.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


def mood_agent(state: dict) -> dict:
    mood = state.get("mood", "happy")

    prompt = f"""
You are a gentle emotional support assistant for pregnant women.

The user is feeling: {mood}

Give her kind, encouraging, medically-safe advice.
"""
    response = model.generate_content(prompt)
    return {"mood_response": response.text}
