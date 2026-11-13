def fahrenheit_to_celsius(f):
    return(f - 32) * (5 / 9)

def celsius_to_fahrenheit(c):
    return(c * (9/5)) +  32

def degreeScaleConv(d):
    if d == "F":
        return "C"
    else:
        return "F"


scale = (input("What temperature scale do you use: Fahrenheit or Celsius (F/C)?:  ").strip().upper())
temp = float(input("What is the temperature outside today in your area?((Ex: 55.0) Note: No letter): "))

NewScale = degreeScaleConv(scale)

if scale == "F":
    rtrnd_temp = fahrenheit_to_celsius(temp)

else:
    rtrnd_temp = celsius_to_fahrenheit(temp)

print(f"Did you know that {temp}°{scale} = {rtrnd_temp:.2f}°{NewScale}")