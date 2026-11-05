# Creating a hardcoded dictionary representing a student with key values of "name", "grade", and "subjects"
Course_grades = {"Math": "A+", "Science": "A-", "History": "B+", "English": "B", "Art": "A", "Computer Science": "A+"}
student = {"name": "Daniel", "grade": "Junior", "Final-grades":Course_grades}

# Printing each key-value pair using ".items()" in a "for" loop.
for key, value in student.items():
    if key == "Final-grades":
        continue
    else:print(f"{key}: {value}")
print("Final Grades:")
for key, value in Course_grades.items():
    print(f"{key}: {value}")

print("")

# Adding a new key-value pair to dictionary and removing sub dictionary
student["Graduated"] = False
classes = student.pop("Final-grades")
for key, value in student.items():
    print(f"{key}: {value}")

print("")
# printing sub dictionary separately
print("Final Grades:")
for key, value in classes.items():
    print(f"{key}: {value}")
