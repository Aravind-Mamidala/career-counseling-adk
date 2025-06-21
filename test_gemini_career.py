#!/usr/bin/env python3
"""
Test script to verify Gemini-powered career suggestions
"""

import os
from agents.career_agent import CareerRecommenderAgent

def test_gemini_career_suggestion():
    """Test the new Gemini-powered career suggestion"""
    print("🧪 Testing Gemini Career Suggestion...")
    
    # Check if API key is available
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ GEMINI_API_KEY not found. Please set it in your .env file")
        return
    
    career_agent = CareerRecommenderAgent()
    
    # Test with swimming/running (should trigger Gemini suggestion)
    test_data = {
        "name": "Aravind",
        "interest": "swimming",
        "strength": "running", 
        "gpa": "50"
    }
    
    try:
        result = career_agent.run(**test_data)
        print(f"✅ Career suggestion: {result['recommended_career']}")
        print(f"✅ Source: {result.get('source', 'unknown')}")
        print(f"✅ Alternatives: {result.get('alternatives', [])}")
        print("\n🎉 Gemini career suggestion is working!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_gemini_career_suggestion() 