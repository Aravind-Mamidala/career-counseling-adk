from config import get_gemini_model

class RoadmapAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def run(self, career=None, **kwargs):
        if not career:
            return {"roadmap": "No roadmap available."}

        prompt = f"""
Give a 5–7 step career roadmap for becoming a successful {career}. Include skills, projects, certifications, and job prep. Format with bullet points.
"""

        response = self.model.generate_content(prompt)
        return {"roadmap": response.text.strip()}
