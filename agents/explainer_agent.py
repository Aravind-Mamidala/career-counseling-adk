from config import get_gemini_model

class ExplainerAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def run(self, career=None, interest=None, strength=None, gpa=None, name=None, **kwargs):
        if not all([career, interest, strength, gpa]):
            return {
                "explanation": "Insufficient information to generate an explanation."
            }

        prompt = f"""
A student named {name} is interested in {interest} and strong in {strength}, with a GPA of {gpa}.
You have recommended the career path: {career}.

Write a specific, encouraging explanation (3–5 sentences) about why this career is a good match for them.
Avoid generic or repeated lines.
"""

        response = self.model.generate_content(prompt)
        return {"explanation": response.text.strip()}








# from google.adk.agent import Agent

# class ExplainerAgent(Agent):
#     def run(self, input_data):
#         name = input_data.get("name", "User")
#         interest = input_data.get("interest", "your interest")
#         strength = input_data.get("strength", "your strength")
#         score = input_data.get("score", "your score")
#         career = input_data.get("recommended_career", "a suitable career")

#         explanation = (
#             f"Based on your interest in **{interest}** and strength in **{strength}**, "
#             f"along with a score of **{score}**, the career path **{career}** is recommended "
#             f"because it aligns with both your passion and capabilities."
#         )

#         return explanation
