class ExpenseTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.balance = 0

    def add_income(self, amount):
        self.income += amount
        self.balance += amount
        print(f"Income of ${amount} added successfully!\n")

    def add_expense(self, description, amount, category):
        expense = {
            "description": description,
            "amount": amount,
            "category": category
        }
        self.expenses.append(expense)
        self.balance -= amount
        print(f"Expense '{description}' of ${amount} in category '{category}' added successfully!\n")

    def view_balance(self):
        print(f"Your current balance is: ${self.balance}\n")

    def view_expenses_by_category(self, category):
        total = sum(expense["amount"] for expense in self.expenses if expense["category"].lower() == category.lower())
        print(f"Total spent in category '{category}': ${total}\n")

def main():
    tracker = ExpenseTracker()

    while True:
        print("Personal Expense Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Expenses by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            tracker.add_income(amount)

        elif choice == "2":
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_expense(description, amount, category)

        elif choice == "3":
            tracker.view_balance()

        elif choice == "4":
            category = input("Enter category to view expenses: ")
            tracker.view_expenses_by_category(category)

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
