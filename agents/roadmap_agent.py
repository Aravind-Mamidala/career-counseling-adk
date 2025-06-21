from google.adk.agent import Agent

class RoadmapAgent(Agent):

    @property
    def llm(self):
        if not hasattr(self, "_llm"):
            self._llm = self.get_tool("llm")
        return self._llm

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
