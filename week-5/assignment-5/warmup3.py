def name_search(nmlst,target):
    for i in range(len(nmlst)):
        if nmlst[i] == target:
            return i + 1
        
    return -1

# Only used AI to develop this long list of names so that I can start with it. my prompt was "Create an A–Z name list with exactly 5 male names and 5 female names for every letter of the English alphabet. For each letter, list the 5 male names first, followed by the 5 female names. Output only the names as a single comma-separated line. Enclose every name in double quotation marks. Do not include letter headings, numbering, categories, explanations, code fences, line breaks, or any text other than the quoted names. Order all names alphabetically by letter from A through Z."
names = ["Aaron", "Aiden", "Adrian", "Andrew", "Alexander", "Abigail", "Ava", "Amelia", "Aria", "Audrey", "Benjamin", "Blake", "Brandon", "Brody", "Bryce", "Brianna", "Bella", "Brooklyn", "Bailey", "Bethany", "Caleb", "Charles", "Cameron", "Christopher", "Carter", "Chloe", "Charlotte", "Claire", "Camila", "Caroline", "Daniel", "Dylan", "David", "Dominic", "Declan", "Delilah", "Diana", "Daisy", "Dakota", "Daphne", "Ethan", "Elijah", "Ezra", "Evan", "Easton", "Emma", "Evelyn", "Ella", "Eleanor", "Elizabeth", "Finn", "Frederick", "Felix", "Frank", "Fernando", "Faith", "Fiona", "Freya", "Felicity", "Francesca", "Gavin", "Gabriel", "Grayson", "George", "Garrett", "Grace", "Gabriella", "Gianna", "Genevieve", "Georgia", "Hudson", "Henry", "Hayden", "Hunter", "Harrison", "Harper", "Hannah", "Hazel", "Hailey", "Hope", "Isaac", "Isaiah", "Ian", "Ivan", "Imran", "Isabella", "Iris", "Ivy", "Isla", "Ingrid", "Jacob", "James", "Jackson", "Joseph", "Joshua", "Jasmine", "Julia", "Jade", "Jocelyn", "Joanna", "Kai", "Kevin", "Kenneth", "Kyle", "Kaden", "Kayla", "Katherine", "Kylie", "Kiara", "Kate", "Liam", "Lucas", "Levi", "Logan", "Landon", "Lily", "Luna", "Leah", "Lucy", "Layla", "Mason", "Michael", "Matthew", "Miles", "Marcus", "Mia", "Madison", "Maya", "Melanie", "Morgan", "Noah", "Nathan", "Nicholas", "Nolan", "Nathaniel", "Nora", "Natalie", "Naomi", "Nicole", "Nina", "Owen", "Oliver", "Oscar", "Omar", "Oakley", "Olivia", "Ophelia", "Olivia-Rose", "Octavia", "Oaklyn", "Parker", "Patrick", "Preston", "Peter", "Paxton", "Penelope", "Paige", "Piper", "Payton", "Phoebe", "Quentin", "Quincy", "Quinton", "Queen", "Quest", "Quinn", "Queenie", "Quinnlyn", "Quiana", "Quetzali", "Ryan", "Robert", "Riley", "Roman", "Ryder", "Rachel", "Rebecca", "Rose", "Ruby", "Reagan", "Sebastian", "Samuel", "Silas", "Sawyer", "Simon", "Sophia", "Scarlett", "Stella", "Savannah", "Sadie", "Thomas", "Tyler", "Theodore", "Tristan", "Tucker", "Tessa", "Taylor", "Trinity", "Teagan", "Thea", "Uriel", "Ulysses", "Umar", "Uriah", "Urban", "Uma", "Unity", "Unique", "Ursula", "Ulani", "Victor", "Vincent", "Vincentius", "Vaughn", "Valentino", "Violet", "Victoria", "Valeria", "Vanessa", "Vera", "Wyatt", "William", "Wesley", "Walter", "Warren", "Willow", "Wendy", "Winter", "Wren", "Whitney", "Xavier", "Xander", "Xerxes", "Xavian", "Xayden", "Xiomara", "Xena", "Xia", "Ximena", "Xylia", "Yosef", "Yusuf", "Yahya", "Yahir", "York", "Yasmin", "Yvonne", "Yaretzi", "Yesenia", "Yara", "Zachary", "Zane", "Zion", "Zayden", "Zander", "Zara", "Zoe", "Zuri", "Zelda", "Zoey"
]

target = str(input("Enter your first name: "))
found = False


for name in names:
    if name == target:
        found = True
        break

if found == True:
    result = name_search(names, target)
    print(f"Congraulations, your name {target} is in postion {result} in our database!")
else:
    addname = bool(input("Wow, what a beautiful name! Unfortunately, it isn't in our database, would you like to add it(True or False): "))
    if addname == True:
        newname = target
        names.append(newname)
        print(f"Congraulations, You have successfully added your name {target} to our database!")
        position = bool(input("Would you like to know your place in the database?(True or False): "))
        if position == True:
            result = linear_search(names, newname)
            print(result) 
        else:
            print(f"Thank you for adding your name {target} to our database, have a good day.")
    else:
        print(f"Thank you for checking our database for your name {target}, have a good day.")

