numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(lst):
    smallnum = lst[0]
    for n in lst:
        if n < smallnum:
            smallnum = n

    return smallnum

def find_max(lst):
    bignum = lst[0]
    for n in lst:
        if n > bignum:
            bignum = n

    return bignum   

def search(lst, trgt):
    for index, value in enumerate(lst):
        if trgt == value:
            return index

    return -1

def bubble_sort(lst):
    newlist = lst.copy()
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(newlist)-1):
            if newlist[i] > newlist[i + 1]:
                newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                sorting = True

    return newlist

def show_menu():
    print(
        "\n ======== NUMBER CRUNCHER ======== \n"
        "1. Find Minimum Number in the List\n"
        "2. Find Maximum Number in the List\n"
        "3. Search for a Number in the List\n"
        "4. Sort the list in numerical order\n"
        "5. Quit"
    )

    return input("Choose an option (1-5): ")

def main():
    while True:
        option = show_menu()

        if option == "1":
            minnum = find_min(numbers)
            print(f"The Minimum number in the list is {minnum}!")

        elif option == "2":
            maxnum = find_max(numbers)
            print(f"The Maximum number in the list is {maxnum}!")
        elif option == "3":
            num = int(input("What number would you like to search for?: "))
            found = search(numbers, num)
            if found == -1:
                print(f"Unfortunately your number, {num} is not found in the list")
            else:
                print(f"Hey, your number, {num} has been found at index {found}")
        elif option == "4":
            sortedlist = bubble_sort(numbers)
            print(f"When the list is sorted from least to greatest value it looks like this:\n{sortedlist}")
        elif option == "5":
            print("Okay, see you later alligator!")
            break
        else:
            print("please choose a valid option!")


main()
