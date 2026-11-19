def salutation(name="Guest Player", greeting="Hello"):
    print(f"{greeting}, {name}!")

def greet_by_letter(name):
    if name[0].lower() <= "d":
        return("how are you?")
    elif "d" < name[0].lower() <= "h":
        return("What's up?")
    elif "h" < name[0].lower() <= "l":
        return("How have you been?")
    elif "l" < name[0].lower() <= "p":
        return("How's it hanging?")
    elif "p" < name[0].lower() <= "t":
        return("What's new?")
    elif "t" < name[0].lower() <= "x":
        return("What have you been up to?")
    elif "x" < name[0].lower() <= "z":
        return("How are things on your end?")
    else:
        return("Look who it is!")

while True:
    name = input("What is your name?: ")
    if name == "":
        salutation()
    else:
        salutation(name)
        salutation(name, greet_by_letter(name))
        salutation(name, greeting="Glad to connect")