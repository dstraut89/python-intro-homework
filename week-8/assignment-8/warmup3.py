def file_handling(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}. Could not find '{filepath}'. Check that you wrote file path correctly.")
        return ""

def file_path(file):
    return (f"../data/{file}")

search = input("What file would you like to read today?: ")
filepath = file_path(search)
read_file = file_handling(filepath)
print(read_file)