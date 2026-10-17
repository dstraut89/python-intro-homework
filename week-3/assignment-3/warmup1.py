score = 86.7

if score >= 90 and score <= 100:
    Grade = "A"
    print(f"Your Score is {score}. \n Your Grade is {Grade}.")
elif score >= 80 and score < 90:
    Grade = "B"
    print(f"Your Score is {score}. \n Your Grade is {Grade}.")
elif score >= 70 and score < 80:
    Grade = "C"
    print(f"Your Score is {score}. \n Your Grade is {Grade}.")
elif score >= 60 and score < 70:
    Grade = "D"
    print(f"Your Score is {score}. \n Your Grade is {Grade}.")
elif score < 60:
    Grade = "F"
    print(f"Your Score is {score}. \n Your Grade is {Grade}.")
else:
    print("Invalid score")