import csv
import os

purchase_date = input("What was the date of purchase? DD/MM/YYYY ")
expense = input("What was the item purchased? ")
price = input("How much did it cost? £")
category = input("Is there a category? E.g. food, transport: ")

price = round(float(price), 2)

file_exists = os.path.isfile("expenses.csv")

with open("expenses.csv", mode="a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["purchase_date", "expense", "amount", "category"])

    writer.writerow([purchase_date, expense, price, category])