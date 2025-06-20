from google.adk.agent import Agent
import json  # Add this at the top if not already
class InputCollectorAgent:
    def run(self, input_data):  # Accept input_data from Streamlit
        return {
            "name": input_data.get("name"),
            "interest": input_data.get("interest"),
            "strength": input_data.get("strength"),
            "gpa": input_data.get("gpa")
        }
