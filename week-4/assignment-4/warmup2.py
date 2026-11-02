# Creating a hardcoded dictionary representing a student with key values of "name", "grade", and "subjects"

student = {"name": "Daniel", "grade": "Senior", "subj-grade": {"Math": "A+", "Science": "A-", "History": "B+", "English": "B", "Art": "A", "Computer Science": "A+"}}

# Printing each key-value pair using ".items()" in a "for" loop.
for key, value in list(student.items())[:2]:
        print(f"{key}: {value}")
for key, value in student["subj-grade"].items():
    print(f"{key}: {value}")

print("")

# Adding a new key-value pair to dictionary and removing sub dictionary
student["Graduated"] = False
classes = student.pop("subj-grade")
for key, value in list(student.items()):
    print(f"{key}: {value}")

print("")
# printing sub dictionary separately
for key, value in classes.items():
    print(f"{key}: {value}")