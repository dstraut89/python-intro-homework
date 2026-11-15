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


    if workfile:
        with open(f'{path}', 'r') as file:
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
            
            with open('food_report.txt', 'w') as file:
                file.write(f"Food Expense Report - generated {now.strftime('%B %d, %Y')}\n{body}\n     Total: ${total:.2f}")
                print('food_report.txt')

else:
    print("expenses.csv not found.")