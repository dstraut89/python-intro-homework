print("Lets do some division today with a safety factor.")
while True:
    dividend = float(input("Please enter the dividend for the equation(the top number): "))
    divisor = float(input("Please enter the divisor for the equation(the bottom number): "))
    try:
        quotient = dividend / divisor
        print(f"{dividend} ÷ {divisor} = {quotient}")
        break
    except ZeroDivisionError:
        print("You can't divide by zero; please try again without using Zero.")
        