# 🎓 Career Counseling Assistant using Multi-Agent Architecture

This is an AI-powered career counseling app built using **Google's Agent Development Kit (ADK)**, deployed with **Streamlit**, and enhanced with multi-agent architecture for a complete interactive experience.

🔗 **Live Demo**: [career-counseling-adk.streamlit.app](https://career-counseling-adk.streamlit.app/)

---

## 🧠 Features

- 🔍 Personalized career recommendations based on interest, strength, and GPA.
- 🤖 Multi-agent architecture: InputAgent, CareerRecommenderAgent, ExplainerAgent, RoadmapAgent.
- 📄 CSV-based data-driven decision logic (no ML used).
- 🧭 Career explanation and roadmap guidance using LLMs.
- 🌐 Hosted publicly via Streamlit Cloud.

---

## 🏗️ Architecture

![Architecture](./Architecture.png)

---

## 🚀 How It Works

1. User enters details: Name, Interests, Strengths, GPA.
2. `InputAgent` collects and validates data.
3. `CareerRecommenderAgent` matches CSV-based careers.
4. `ExplainerAgent` provides reasoning using Gemini / LLM.
5. `RoadmapAgent` outlines the path forward.

---

## 💡 Technologies Used

- Python
- Google ADK
- Streamlit
- CSV (Data Store)


---

## 🙋 Author

- **Name**: Mamidala Aravind  
- **GitHub**: [@Aravind-Mamidala](https://github.com/Aravind-Mamidala)

---

## 📢 Submission Info

- 🔧 Hackathon: [Agent Development Kit Hackathon with Google Cloud](https://devpost.com/)
- 💡 Category: Career Counseling using Multi-Agent Systems

- Gemini Pro (via Explainer/Roadmap Agents)

---

## 📁 Directory Structure

