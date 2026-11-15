import os
import csv
from datetime import datetime


def bool_workfile(X):
    if X == "y":
        return True
    else:
        return False

def file_path(file):
    filepath = (f"week-7/data/{file}")
    return filepath

search = input("What file would you like to look for?: ")
path = file_path(search)

if os.path.exists(f'{path}'):
    print("expenses.csv found.")

    workfile = input("Would you like to the food report within the file?: Y/N ").strip().lower()
    workfile = bool_workfile(workfile)


    if workfile == True:
        with open('week-7/data/expenses.csv', 'r') as file:
            expense = list(csv.DictReader(file))
            for item in expense:
                item['amount'] = float(item['amount'])
            
            foodcollector = [item for item in expense if item['category'] == 'Food']
            foodcollector_body = []
            for row in foodcollector:
                foodcollector_body += [f"{row['date']}: ${row['amount']:.2f}"]
                body = "\n".join(foodcollector_body)

            total = sum(item['amount'] for item in foodcollector)
            
            now = datetime.now()
            
            with open('Food_report.txt', 'w') as file:
                file.write(f"Food Expense Report - generated {now.strftime('%B %d, %Y')}\n{body}\n     Total: ${total}")
                print('Food_report.txt')

else:
    print("expenses.csv not found.")



'''
##### 1) Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
##### 2) Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
3) Convert the amount field to float for each row.
4) Filter the list to only rows where category is "Food".
5) Calculate the total amount spent on Food.
6) Write a report to food_report.txt with this structure:
        - First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
        - One line per food expense: [date]: $[amount]
        - Last line: Total: $[total to 2 decimal places]
'''