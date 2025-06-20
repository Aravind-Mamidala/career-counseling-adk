from agents.orchestrator_agent import OrchestratorAgent

if __name__ == "__main__":
    agent = OrchestratorAgent()
    request = {}  # not used, since inputs are taken interactively
    response = agent.run(request)

    print("\n🎯 Career Match Result:")
    print(response)
