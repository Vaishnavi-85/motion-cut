import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_data()

    def add_expense(self, amount, category, description):
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_data()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("\nAll Expenses:")
            for idx, expense in enumerate(self.expenses, start=1):
                print(f"{idx}. {expense['date']} | {expense['category']} | {expense['amount']} | {expense['description']}")

    def view_summary(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("\nExpense Summary:")
            summary = {}
            for expense in self.expenses:
                summary[expense["category"]] = summary.get(expense["category"], 0) + expense["amount"]

            for category, total in summary.items():
                print(f"{category}: {total}")

    def save_data(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

    def load_data(self):
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def error_handling_example(self, func, *args):
        try:
            func(*args)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (e.g., Food, Transport): ")
                description = input("Enter description: ")
                tracker.error_handling_example(tracker.add_expense, amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a valid number for the amount.")
        elif choice == "2":
            tracker.error_handling_example(tracker.view_expenses)
        elif choice == "3":
            tracker.error_handling_example(tracker.view_summary)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

