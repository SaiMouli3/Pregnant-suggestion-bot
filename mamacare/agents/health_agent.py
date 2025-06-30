# config.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")
 

def health_agent(state: dict) -> dict:
    trimester = state.get("trimester", "2nd")
    diet = state.get("diet", "vegetarian")

    prompt = f"""
You are a pregnancy-safe health assistant. Based on:

Trimester: {trimester}
Diet: {diet}
Give:
- 1 Nutrition tip 🥗
- 1 Safe exercise tip 🧘
"""
    response = model.generate_content(prompt)
    return {"daily_tip": response.text}
