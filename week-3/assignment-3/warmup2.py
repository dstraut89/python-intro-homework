age = int(input("Please enter your age: "))

if age <= 12:
    Cat = "Child"
    print(f"You said you are {age} years old. You are in the {Cat} category.")
<<<<<<< HEAD
if age > 12 and age <=17:
    Cat = "Teen"
    print(f"You said you are {age} years old. You are in the {Cat} category.")
if age > 17 and age <= 64:
=======
elif age > 12 and age <=17:
    Cat = "Teen"
    print(f"You said you are {age} years old. You are in the {Cat} category.")
elif age > 17 and age <= 64:
>>>>>>> 0759bbc3c20c139b2264812302dca2accf9cdd5b
    Cat = "Adult"
    print(f"You said you are {age} years old. You are in the {Cat} category.")
else:
    Cat = "Senior"
    print(f"You said you are {age} years old. You are in the {Cat} category.")