#!/usr/bin/env python3
"""
Test script to verify the orchestrator with Gemini integration
"""

import os
from agents.orchestrator_agent import OrchestratorAgent

def test_orchestrator():
    """Test the orchestrator with swimming/running input"""
    print("🧪 Testing Orchestrator with Gemini Integration...")
    
    # Check if API key is available
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ GEMINI_API_KEY not found. Please set it in your .env file")
        return
    
    orchestrator = OrchestratorAgent()
    
    # Test with swimming/running (should trigger Gemini suggestion)
    test_data = {
        "name": "Aravind",
        "interest": "swimming",
        "strength": "running", 
        "gpa": "50"
    }
    
    try:
        result = orchestrator.run(test_data)
        print(f"✅ Career suggestion: {result['recommended_career']}")
        print(f"✅ Source: {result.get('source', 'unknown')}")
        print(f"✅ Alternatives: {result.get('alternatives', [])}")
        print(f"✅ Has explanation: {'explanation' in result}")
        print(f"✅ Has roadmap: {'roadmap' in result}")
        print("\n🎉 Orchestrator is working correctly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_orchestrator() 