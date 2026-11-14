num = int(input("Please enter a number: "))

if num > 0:
    print(f"Your number {num} is positive.")
elif num < 0:
    print(f"Your number {num} is negative.")
else:
    print(f"Your number {num} is zero.")

if num % 2 == 0:
    print(f"Your number {num} is even.")
else:
    print(f"Your number {num} is odd.")