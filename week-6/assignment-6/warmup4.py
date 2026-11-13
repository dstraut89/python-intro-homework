def is_valid_score(score):
    if score >= 0 and score <= 100:
        return(True)
    else:
        return(False)

Result = int(input("What is the student's score?: "))

validity_check = is_valid_score(Result)

if validity_check:
    print("That is a valid score")
else:
    print("That is a invalid score, please input a score between 0 and 100")