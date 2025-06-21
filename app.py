import streamlit as st
from agents.orchestrator_agent import OrchestratorAgent
import os

# Clear cache to ensure fresh code is loaded
st.cache_data.clear()
st.cache_resource.clear()

st.set_page_config(page_title="Career Counselor", page_icon="🎓")

st.title("🎓 Career Counseling Assistant")
st.markdown("Get career suggestions based on your interests, strengths, and GPA.")

# Check for API key
if not os.getenv("GEMINI_API_KEY"):
    st.error("""
    ⚠️ **Configuration Error**: Gemini API key not found!
    
    Please create a `.env` file in the project root with your Gemini API key:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```
    
    You can get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
    """)
    st.stop()

# Input fields
name = st.text_input("Enter your name")
interest = st.text_input("What are you interested in? (e.g., coding, art, biology, swimming)")
strength = st.text_input("What are you strong in? (e.g., math, writing, running)")
gpa = st.text_input("Enter your GPA or percentage")

if st.button("Get Career Recommendation"):
    if not all([name, interest, strength, gpa]):
        st.warning("Please fill in all the details.")
    else:
        # Create orchestrator and call run
        try:
            orchestrator = OrchestratorAgent()
            user_data = {
                "name": name,
                "interest": interest,
                "strength": strength,
                "gpa": gpa
            }
            
            with st.spinner("🤖 Analyzing your profile and generating personalized recommendations..."):
                response = orchestrator.run(user_data)

            st.success("🎯 Career Match Result")
            st.write(f"**Name:** {response['name']}")
            st.write(f"**Recommended Career:** {response['recommended_career']}")
            st.write(f"**Score:** {response['score']}")
            
            # Show source of recommendation
            source = response.get('source', 'unknown')
            if source == 'csv_match':
                st.info("📊 Recommendation based on our career database")
            elif source == 'gemini_suggestion':
                st.info("🤖 AI-powered recommendation based on your unique profile")
            elif source == 'fallback':
                st.warning("⚠️ Using fallback recommendation due to technical issues")
            
            if response.get('alternatives'):
                st.markdown("**🧭 Alternative Career Options:**")
                for career in response['alternatives']:
                    st.markdown(f"- {career}")

            if response.get("explanation"):
                st.markdown("**🧠 Why this career?**")
                st.info(response['explanation'])

            if response.get("roadmap"):
                st.markdown("**🗺️ Career Roadmap:**")
                st.info(response['roadmap'])

            # Debug section (can be removed later)
            with st.expander("🔧 Debug Info"):
                st.json(response)

        except ValueError as e:
            st.error(f"❌ Configuration Error: {e}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.info("💡 If you're seeing API errors, please check your Gemini API key and internet connection.")
