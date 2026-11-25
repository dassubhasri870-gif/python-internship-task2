# Python Programming Internship - Task 2
# Expense Tracker (Command-Line Application)
# Name: Subhasri Das

import csv
import os

FILE_NAME = "expenses.csv"


def setup_file():
    """Create the CSV file with a header row if it does not exist yet."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])
            

def add_expense():
    """Ask for description and amount, then save them to the CSV file."""
    print("\n--- Add Expense ---")
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])

    print("Expense saved successfully!")
    
    
def view_expenses():
    """Read the CSV file and display all saved expenses."""
    print("\n--- All Expenses ---")
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if len(rows) == 0:
        print("No expenses recorded yet.")
        return

    print(f"{'No.':<5}{'Description':<25}{'Amount':>10}")
    print("-" * 40)
    for number, row in enumerate(rows, start=1):
        print(f"{number:<5}{row['Description']:<25}{float(row['Amount']):>10.2f}")
        
        
def total_expenses():
    """Add up all amounts in the CSV file and display the total."""
    total = 0
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total = total + float(row["Amount"])

    print(f"\nTotal amount spent: {total:.2f}")
    
    
def main():
    setup_file()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye! Your expenses are saved in", FILE_NAME)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()