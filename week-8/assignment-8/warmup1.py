while True:
    num = input("Please enter any number.: ")
    try:
        num = float(num)
        print(f"The number you entered is {num}")
        break
    except ValueError as e:
        print(f"Number Collection failed: {e}. {num} is not a valid number. Please Try again.")