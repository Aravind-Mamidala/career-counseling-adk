import google.generativeai as genai

def get_gemini_model():
    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel("gemini-pro")
    return model
