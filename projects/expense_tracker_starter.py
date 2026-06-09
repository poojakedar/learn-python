"""Project Starter: Expense Tracker

Challenge:
1) Add menu to add/show/delete expenses
2) Show total and category-wise totals
3) Save and load from file
"""


def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for i, item in enumerate(expenses, start=1):
        print(f"{i}. {item['category']} -> {item['amount']}")


def total_expenses(expenses):
    return sum(item["amount"] for item in expenses)

# write Total amount: 60.0 to file day08_total.txt
def save_total(total, file_name="day08_total.txt"):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Total amount: {total}\n")

def main():
    expenses = []
    print("Expense Tracker Starter")
    print("Build the full menu as your project practice.")

    # Quick demo entries
    add_expense(expenses, 120.0, "food")
    add_expense(expenses, 50.0, "travel")

    show_expenses(expenses)
    print("Total:", total_expenses(expenses))
    save_total(total_expenses(expenses))

if __name__ == "__main__":
    main()
