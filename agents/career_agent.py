import csv
from config import get_gemini_model

class CareerRecommenderAgent:
    def __init__(self):
        self.model = get_gemini_model()
    
    def run(self, name=None, interest=None, strength=None, gpa=None, **kwargs):
        if isinstance(gpa, str):
            gpa = gpa.strip()
        try:
            score = int(float(gpa))
        except Exception as e:
            print("ERROR converting GPA:", e)
            score = 0

        # First, try to find a match in CSV
        with open('data/career_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row['interest'].lower() == interest.lower() and
                    row['strength'].lower() == strength.lower() and
                    score >= int(row['min_score'])):

                    recommended = row['careers'].split('|')  # handle multiple careers
                    return {
                        "name": name,
                        "recommended_career": recommended[0],  # pick first one as default
                        "score": score,
                        "alternatives": recommended,
                        "source": "csv_match"
                    }

        # If no CSV match, use Gemini to suggest relevant careers
        try:
            prompt = f"""
Based on the following student profile, suggest 3-5 relevant career paths:

Student Profile:
- Interest: {interest}
- Strength: {strength}
- GPA/Score: {score}

Please provide:
1. A primary recommended career that best matches their interests and strengths
2. 3-4 alternative career options
3. Brief reasoning for the primary recommendation

Format your response as:
PRIMARY: [career name]
REASONING: [2-3 sentences explaining why this career fits]
ALTERNATIVES: [career1, career2, career3, career4]

Make sure the careers are realistic and achievable given their background.
"""

            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Parse the response
            lines = response_text.split('\n')
            primary_career = "Career Advisor"  # default
            alternatives = []
            
            for line in lines:
                if line.startswith('PRIMARY:'):
                    primary_career = line.replace('PRIMARY:', '').strip()
                elif line.startswith('ALTERNATIVES:'):
                    alt_text = line.replace('ALTERNATIVES:', '').strip()
                    alternatives = [alt.strip() for alt in alt_text.split(',')]
            
            return {
                "name": name,
                "recommended_career": primary_career,
                "score": score,
                "alternatives": alternatives,
                "source": "gemini_suggestion"
            }
            
        except Exception as e:
            print(f"Error getting Gemini suggestion: {e}")
            # Fallback to a generic suggestion
            return {
                "name": name,
                "recommended_career": "Career Development Specialist",
                "score": score,
                "alternatives": ["Human Resources Specialist", "Training Coordinator", "Student Advisor"],
                "source": "fallback"
            }
