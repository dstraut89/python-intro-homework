def min_button(lst):
    smallnum = lst[0]
    for n in lst:
            if n < smallnum:
                smallnum = n

    return smallnum

def max_button(lst):
    bignum = lst[0]
    for n in lst:
            if n > bignum:
                bignum = n

    return bignum   

def search_button(lst, trgt):
    for index, value in enumerate(lst):
        if trgt == value:
            return index

    return -1

def sort_button(lst):
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorting = True
    return lst

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print(" ======== NUMBER CRUNCHER ======== \n1. Find Minimum Number in the List\n2. Find Maximum Number in the List\n3. Search for a Number in the List\n4. Sort the list in numerical order\n5. Quit")
    Option = int(input("Choose an option (1-5): "))
    if Option == 1:
        minnum = min_button(numbers)
        print(f"The Minimum number in the list is {minnum}!")

    elif Option == 2:
        maxnum = max_button(numbers)
        print(f"The Maximum number in the list is {maxnum}!")
    elif Option == 3:
        num = int(input("What number would you like to search for?: "))
        found = search_button(numbers, num)
        if found == -1:
            print(f"Unfortunately your number, {num} is not found in the list")
        else:
            print(f"Hey, your number, {num} has been found at index {found}")
    elif Option == 4:
        sortedlist = sort_button(numbers)
        print(f"When the list is sorted from least to greatest value it looks like this:\n{sortedlist}")
    elif Option == 5:
        print("Okay, see you later alligator!")
        break
    else:
        print("please choose a valid option!")
quit()
