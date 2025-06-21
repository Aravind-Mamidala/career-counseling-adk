from google.adk.agent import Agent
from config import get_gemini_model

class RoadmapAgent(Agent):
    def __init__(self):
        super().__init__()
        self.model = get_gemini_model()

    def run(self, career=None, **kwargs):
        if not career:
            return {"roadmap": "No roadmap available."}

        prompt = f"""
You are a career roadmap planner bot.

Give a step-by-step roadmap (in 5–7 points) for becoming a successful {career}.
Include skills to learn, projects to build, certifications or degrees, and job preparation advice.
Format the steps with bullet points.
"""

        response = self.model.generate_content(prompt)
        return {"roadmap": response.text.strip()}
