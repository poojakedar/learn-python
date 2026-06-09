"""Day 8 exercises.

Goal: Build one complete mini project from start to finish.
Save final work as solutions/day08_solution.py
"""

print("=== Day 8 Exercise: Expense Tracker Mini Project ===")


def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


def show_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    print("\nAll expenses:")
    for index, item in enumerate(expenses, start=1):
        print(f"{index}. {item['category']} -> {item['amount']}")


def total_expense(expenses):
    return sum(item["amount"] for item in expenses)


def save_report(expenses, file_name="day08_expenses_report.txt"):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Expense Report\n")
        file.write("==============\n")
        for item in expenses:
            file.write(f"{item['category']}: {item['amount']}\n")
        file.write(f"Total: {total_expense(expenses)}\n")


# TODO 1: Keep menu running until user chooses Exit.
# TODO 2: Add expense using amount + category input.
# TODO 3: Show all expenses.
# TODO 4: Show total expense.
# TODO 5: Save report to file.

def main():
    expenses = []

    while True:
        print("\nMenu")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Save report")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                add_expense(expenses, amount, category)
                print("Expense added.")
            except ValueError:
                print("Invalid amount. Enter a number.")
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print("Total:", total_expense(expenses))
        elif choice == "4":
            save_report(expenses)
            print("Report saved to day08_expenses_report.txt")
        elif choice == "5":
            print("Good job. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


main()

print("\nGreat work! Save this as solutions/day08_solution.py")
