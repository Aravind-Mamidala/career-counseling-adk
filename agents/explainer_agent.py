from google.adk.agent import Agent

class ExplainerAgent(Agent):
    def run(self, career=None, interest=None, strength=None, gpa=None, **kwargs):
        if not all([career, interest, strength, gpa]):
            return {
                "explanation": "Insufficient information to generate an explanation."
            }

        explanation = (
            f"Based on your interest in {interest} and strength in {strength}, "
            f"along with a score of {gpa}, the career path '{career}' is recommended "
            f"because it aligns with both your passion and capabilities."
        )

        return {
            "explanation": explanation
        }









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
