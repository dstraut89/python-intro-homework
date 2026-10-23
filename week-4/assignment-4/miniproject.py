# Copied list from "roster.py" that was given under the "data" directory.
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
# Variable for Top score and scorer
TopScore = 0
TopScorer = {}
# For loop to determine who has top score
for student in students:
    if student["score"] > TopScore:
        TopScore = student["score"]
        TopScorer = student["name"]
# print top scorer with their score
print(f"Top Scorer: {TopScorer}, {TopScore}")

# varible for sum of class scores
classTotal = 0
# For loop to total up all scores
for student in students:
    classTotal += student["score"]
# average is sum of scores divided by the number of student scores    
ClassAve = classTotal / len(students)
# printing the class average
print(f"Class average: {ClassAve}")

subjects = set()

for student in students:
    subjects.add(student["subject"])

print(f"Subjects offered: {subjects}")

HScorers = []

for student in students:
    if student["score"] > 75:
        HScorers.append(student["name"])

print(f"High scorers: {HScorers}")