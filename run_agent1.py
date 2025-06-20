from agents.input_agent import InputCollectorAgent
from agents.recommend_agent import RecommendAgent

if __name__ == "__main__":
    input_agent = InputCollectorAgent()
    user_data = input_agent.run()

    match_agent = RecommendAgent()
    result = match_agent.run(**user_data)

    print("\n🎯 Career Match Result:")
    print(result)
