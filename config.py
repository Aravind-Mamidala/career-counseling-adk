import os
import google.generativeai as genai

def get_gemini_model():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    return genai.GenerativeModel("gemini-pro")
