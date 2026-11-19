day = str(input("What day is it? ")).strip().lower()
time = str(input("What is the time of day?(morning/afternoon/evening) ")).strip().lower()

if day == "monday":
    if time == "morning":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat a couple sunnyside up eggs on toast with avocado slices for breakfast and start coding on your laptop!")
    elif time == "afternoon":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat a turkey wrap for lunch and so you can hurry back to coding on your laptop!")
    elif time == "evening":
        print(f"Good {time}! It's a beautiful {day} {time}! Do you want Meatloaf burgers with baked beans and sweetpotatoe fries for dinner and start coding on your laptop!")
    else :
        print(f"Hey, it's a beautiful {day}! No matter the time of day, it's always a great time to start coding on your laptop!")

elif day == "tuesday":
    if time == "morning":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat scrambled eggs with mozzarella on toast for breakfast and start coding on your laptop!")
    elif time == "afternoon":
        print(f"Good {time}! It's a beautiful {day} {time}! It's taco tuesday, do you want hard tacos or soft tacos for lunch and start coding on your laptop on your back porch!")
    elif time == "evening":
        print(f"Good {time}! It's a beautiful {day} {time}! let's eat a bowl of shrimp alfredo for dinner and start coding on your laptop!")
    else :
        print(f"Hey, it's a beautiful {day}! No matter the time of day, it's always a great time to start coding on your laptop!")

elif day == "wednesday":
    if time == "morning":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat quick yogurt parfait with fruit and granola for breakfast and start coding on your laptop!")
    elif time == "afternoon":
        print(f"Good {time}! It's a beautiful {day} {time}! Want some Arby's for lunch, they have the meat, so you get your protein and back to coding you go!")
    elif time == "evening":
        print(f"Good {time}! It's a beautiful {day} {time}! Yum, Yum, Yum! Shepherd's pie here we come. time for dinner and start coding on your laptop!")
    else :
        print(f"Hey, it's a beautiful {day}! No matter the time of day, it's always a great time to start coding on your laptop!")

elif day == "thursday":
    if time == "morning":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat a your favorite cerel along with a small bowl of fruitfor breakfast and start coding on your laptop!")
    elif time == "afternoon":
        print(f"Good {time}! It's a beautiful {day} {time}! Time to reminisce some childhood moments with hotdogs and mac and cheese for lunch and start coding on your laptop on your back porch!")
    elif time == "evening":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat a stuffed shells smoothered in meat sauce for dinner and start coding on your laptop!")
    else :
        print(f"Hey, it's a beautiful {day}! No matter the time of day, it's always a great time to start coding on your laptop!")

elif day == "friday":
    if time == "morning":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to drink a protein smoothie for breakfast and start coding on your laptop!")
    elif time == "afternoon":
        print(f"Good {time}! It's a beautiful {day} {time}! Who is going to do the McDonald's run, we are having Chicken nuggets and fries for lunch today!")
    elif time == "evening":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat baked salmon on a bed of rice with a side of steamed vege and start coding on your laptop!")
    else :
        print(f"Hey, it's a beautiful {day}! No matter the time of day, it's always a great time to start coding on your laptop!")

elif day == "saturday":
    if time == "morning":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat a muffin and banana for breakfast and start coding on your laptop!")
    elif time == "afternoon":
        print(f"Good {time}! It's a beautiful {day} {time}! Pizza, Pizza, Pizza! Stuffed crust, thin crust, deep dish, you name it! It's a great time to eat pizza for lunch! If only Python can automate a pizza into my stomach!")
    elif time == "evening":
        print(f"Good {time}! It's a beautiful {day} {time}! Who like lasagna? We have vegetable lasagna with cheesy garlic bread and a garden salad! Great time to eat for dinner and start coding on your laptop!")
    else :
        print(f"Hey, it's a beautiful {day}! No matter the time of day, it's always a great time to start coding on your laptop!")

elif day == "sunday":
    if time == "morning":
        print(f"Good {time}! It's a beautiful {day} {time}! Great time to eat sausage egg and cheese on a bagel with a nice hot coffee for breakfastand start coding on your laptop!")
    elif time == "afternoon":
        print(f"Good {time}! It's a beautiful {day} {time}! Congrats you have been randomly selected to bring me to an all you can eat sushi buffet for lunch!")
    elif time == "evening":
        print(f"Good {time}! It's a beautiful {day} {time}! Good for you, you have studied and coded all week long, you earned a nice suff and turf dinner for yourserlf. When you are done eating, just netflix and chill!")
    else :
        print(f"Hey, it's a beautiful {day}! No matter the time of day, it's always a great time to start coding on your laptop!")
else: 
    print("I am so sorry, I do not recognize that day of the week. Please try again and make sure to spell the day correctly (Monday, Tuesday, Wednesday....).")