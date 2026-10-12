# The error that I hit this week was this:
# mup4.py", line 19, in <module>
#    result = num1 + num2
#             ~~~~~^~~~~~
# TypeError: can only concatenate str (not "float") to str
# 
# It was caused by not telling the system what date type was being input by the user. By default, the input is seen as a string.
# I fixed it by converting the input to a float in line 14 when doing the math "result = float(num1) + num2". I also had to convert the first input to a float as well.


name = input("What is your name? ")
num1 = input("Enter a number: ")
num2 = float(input("Enter another number: "))
result = float(num1) + num2
print(f"Hello, {name}! The sum of {num1} and {num2} is {result}.")
