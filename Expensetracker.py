


   

import csv
import os

FILE_NAME = "expenses.csv"


# Ensure CSV file exists with headers
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])


# Add a new expense
def add_expense():
    description = input("Enter expense description: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])

    print("✅ Expense added successfully!")


# View all expenses
def view_expenses():
    print("\n📄 All Expenses:")
    print("-" * 30)

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                print(f"{row[0]} - ₹{row[1]}")
    except FileNotFoundError:
        print("No expenses found.")


# Calculate total spent
def total_expenses():
    total = 0

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                total += float(row[1])

        print(f"\n💰 Total Spent: ₹{total}")
    except FileNotFoundError:
        print("No expenses found.")


# Menu system
def menu():
    initialize_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
