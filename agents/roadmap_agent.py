from google.adk.agent import Agent

class RoadmapAgent(Agent):
    def run(self, career=None, **kwargs):
        if not career:
            return {"roadmap": "No roadmap available."}
        
        # Simple mock roadmaps
        roadmaps = {
            "Software Developer": "1. Learn Python/Java → 2. Build Projects → 3. Master DSA → 4. Apply for Internships → 5. Contribute to Open Source → 6. Land a Job.",
            "Data Analyst": "1. Learn Excel & SQL → 2. Master Python for Data → 3. Learn Pandas/Matplotlib → 4. Take real datasets → 5. Apply for Analyst roles.",
            "AI Engineer": "1. Learn Python → 2. Learn ML basics → 3. Master TensorFlow/PyTorch → 4. Build models → 5. Learn deployment → 6. Join AI teams."
        }

        return {
            "roadmap": roadmaps.get(career, "Work on building strong foundational skills and real-world projects to progress in this career.")
        }
