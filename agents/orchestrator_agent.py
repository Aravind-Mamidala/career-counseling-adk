from agents.input_agent import InputCollectorAgent
from agents.career_agent import CareerRecommenderAgent
from agents.explainer_agent import ExplainerAgent
from agents.roadmap_agent import RoadmapAgent

class OrchestratorAgent:
    def __init__(self):
        self.input_agent = InputCollectorAgent()
        self.career_agent = CareerRecommenderAgent()
        self.explainer_agent = ExplainerAgent()
        self.roadmap_agent = RoadmapAgent()

    def run(self, input_data):
        # Step 1: Input collection
        user_data = self.input_agent.run(input_data)

        # Step 2: Get career recommendation
        career_response = self.career_agent.run(
            name=user_data["name"],
            interest=user_data["interest"],
            strength=user_data["strength"],
            gpa=user_data["gpa"]
        )

        # Step 3: Explanation
        explanation_response = self.explainer_agent.run(
            name=user_data["name"],
            interest=user_data["interest"],
            strength=user_data["strength"],
            gpa=user_data["gpa"],
            career=career_response["recommended_career"]
        )

        # Step 4: Roadmap
        roadmap_response = self.roadmap_agent.run(
            career=career_response["recommended_career"]
        )

        # Merge everything into final response
        return {
            **career_response,
            "explanation": explanation_response.get("explanation", "No explanation available."),
            "roadmap": roadmap_response.get("roadmap", "No roadmap available.")
        }
