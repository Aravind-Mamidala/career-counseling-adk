import csv

class CareerRecommenderAgent:
    def run(self, name=None, interest=None, strength=None, gpa=None, **kwargs):
        if isinstance(gpa, str):
            gpa = gpa.strip()
        try:
            score = int(float(gpa))
        except Exception as e:
            print("ERROR converting GPA:", e)
            score = 0

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
                        "alternatives": recommended
                    }

        return {
            "name": name,
            "recommended_career": "Generalist Career Advisor",
            "score": score,
            "alternatives": []
        }
