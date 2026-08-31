import csv
from datetime import datetime

FILE_NAME = "expenses.csv"
CURRENCY = "Rs."


def add_expense():
    category = input("Enter category (Food/Travel/Study/etc): ")
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, name, amount])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\nDate\t\tCategory\tExpense\t\tAmount")
            print("-" * 70)

            for row in reader:
                if len(row) < 4:
                    continue

                print(
                    f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{CURRENCY} {row[3]}"
                )

    except FileNotFoundError:
        print("No expenses found.")


def view_total():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 4:
                    continue

                total += float(row[3])

        print(f"\nTotal Spending: {CURRENCY} {total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")


def category_summary():
    categories = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 4:
                    continue

                category = row[1]
                amount = float(row[3])

                categories[category] = categories.get(category, 0) + amount

        print("\nCategory Summary")
        print("-" * 30)

        for category, amount in categories.items():
            print(f"{category}: {CURRENCY} {amount:.2f}")

    except FileNotFoundError:
        print("No expenses found.")


def delete_expense():
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 4:
                    expenses.append(row)

        if not expenses:
            print("No expenses found.")
            return

        print("\nExpenses:")
        print("-" * 70)

        for i, row in enumerate(expenses, start=1):
            print(
                f"{i}. {row[0]} | {row[1]} | {row[2]} | {CURRENCY} {row[3]}"
            )

        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(expenses):

            deleted = expenses.pop(choice - 1)

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(expenses)

            print(f"Deleted: {deleted[2]}")

        else:
            print("Invalid expense number.")

    except FileNotFoundError:
        print("No expenses found.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
