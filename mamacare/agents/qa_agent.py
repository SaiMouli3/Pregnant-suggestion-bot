# config.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


def qa_agent(state: dict) -> dict:
    question = state["user_input"]
    prompt = f"""
You are a pregnancy health assistant. Answer this question simply and medically:

Question: {question}
"""
    response = model.generate_content(prompt)
    return {"qa_answer": response.text}
