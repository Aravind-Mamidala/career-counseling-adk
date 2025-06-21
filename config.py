import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # ✅ Load .env variables

def get_gemini_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in environment variables. "
            "Please create a .env file with your Gemini API key: GEMINI_API_KEY=your_api_key_here"
        )
    
    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        raise ValueError(f"Failed to configure Gemini model: {e}. Please check your API key.")
