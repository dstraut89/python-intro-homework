with open('week-7/data/notes.txt', 'r') as file:
    for x, line in enumerate(file):\
        print(f"Line {x}: " + line.strip())
