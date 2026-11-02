def Minbutton(lst):
    srttd = Sortbutton(lst)
    for index, value in enumerate(lst):
        if index == 0:
            return value

def Maxbutton(lst):
    srttd = Sortbutton(lst)
    for index, value in enumerate(srttd):
        if index == 19:
            return value         

def Searchbutton(lst, trgt):
    for index, value in enumerate(lst):
        if trgt != value:
            index += 1
        elif trgt == value:
            return index

    return -1

def Sortbutton(lst):
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorting = True
    return lst

print(" ======== NUMBER CRUNCHER ======== \n1. Find Minimum Number in the List\n2. Find Maximum Number in the List\n3. Search for a Number in the List\n4. Sort the list in numerical order\n5. Quit")
Option = int(input("Choose an option (1-5): "))
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    if Option == 1:
        min = Minbutton(numbers)
        print(f"The Minimum number in the list is {min}!")
        break
    elif Option == 2:
        max = Maxbutton(numbers)
        print(f"The Maximum number in the list is {max}!")
        break
    elif Option == 3:
        num = int(input("What number would you like to search for?: "))
        found = Searchbutton(numbers, num)
        if found == -1:
            print(f"Unfortunately your number, {num} is not found in the list")
        else:
            fnd_num = found + 1
            print(f"Hey, your number, {num} has been found. It is in position {fnd_num} in the list.")
            break
    elif Option == 4:
        sortedlist = Sortbutton(numbers)
        print(f"When the list is sorted from least to greatest value it looks like this:\n{sortedlist}")
        break
    elif Option == 5:
        print("Okay, see you later alligator!")
        break
    else:
        print("please choose a valid option!")
        break
quit()
