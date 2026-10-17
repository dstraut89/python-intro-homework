age = int(input("Please enter your age: "))

if age <= 12:
    Cat = "Child"
    print(f"You said you are {age} years old. You are in the {Cat} category.")
if age > 12 and age <=17:
    Cat = "Teen"
    print(f"You said you are {age} years old. You are in the {Cat} category.")
if age > 17 and age <= 64:
    Cat = "Adult"
    print(f"You said you are {age} years old. You are in the {Cat} category.")
else:
    Cat = "Senior"
    print(f"You said you are {age} years old. You are in the {Cat} category.")