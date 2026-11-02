NumWrd = {
    "zero": 0, "one": 1, "two": 2, "three": 3,
    "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9
}
def NumWrdConvrtr(value):
    if value in NumWrd:
        return NumWrd[value]
    return value

while True:
    number = input("Enter a positive number higher than zero: ")
    number = NumWrdConvrtr(number.strip().lower())

    try:
        num = int(number)
        if num == 0:
            print("Nope, that is zero. Try again.")
        elif num < 0:
            print("Nope, that is a negative number. Try again.")
        else:
            print(f"Hey, you chose the positive number: {num}!")
            break
    except ValueError:
        print("Hey, That isn't even a number in word form. Try again.")