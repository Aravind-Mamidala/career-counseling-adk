from google.adk.agent import Agent

class RoadmapAgent(Agent):
    def __init__(self):
        super().__init__(enable_llm=True)

    def run(self, career=None, **kwargs):
        if not career:
            return {"roadmap": "No roadmap available."}

        prompt = f"""
You are a career roadmap planner bot.

Give a step-by-step roadmap (in 5-7 points) for becoming a successful {career}.
Include skills to learn, projects to build, certifications or degrees, and job preparation advice.
Format the steps with bullet points.
"""

        roadmap = self.llm(prompt)
        return {
            "roadmap": roadmap
        }
