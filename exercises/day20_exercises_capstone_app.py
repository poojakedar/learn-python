"""Day 20 exercises.

Goal: Build a small capstone app using classes, JSON, logging, and argparse.
Save final work as solutions/day20_solution.py

Examples:
python exercises/day20_exercises_capstone_app.py add "Buy milk"
python exercises/day20_exercises_capstone_app.py list
python exercises/day20_exercises_capstone_app.py done 1
"""

import argparse
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

DATA_FILE = Path("day20_expenses.json")


class ExpenseTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.expenses = []
        self.load()

    def load(self):
        if self.file_path.exists():
            self.expenses = json.loads(self.file_path.read_text(encoding="utf-8"))
            logging.info("Loaded %s expenses", len(self.expenses))
        else:
            self.expenses = []
            logging.info("No expense file found. Starting fresh.")

    def save(self):
        self.file_path.write_text(json.dumps(self.expenses, indent=2), encoding="utf-8")
        logging.info("Saved %s expenses", len(self.expenses))

    def add_expense(self, title, amount):
        self.expenses.append({"title": title, "amount": amount})
        self.save()

    def show_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        total = 0
        for idx, item in enumerate(self.expenses, start=1):
            print(f"{idx}. {item['title']} -> {item['amount']}")
            total += item["amount"]
        print("Total:", total)


# TODO 1: Add a subcommand parser with add and list commands.
# TODO 2: For add, take title and amount from command line.
# TODO 3: For list, print all saved expenses.
# TODO 4: Keep logging messages useful and readable.

def build_parser():
    parser = argparse.ArgumentParser(description="Day 20 expense tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add expense")
    add_parser.add_argument("title", help="Expense title")
    add_parser.add_argument("amount", type=float, help="Expense amount")

    subparsers.add_parser("list", help="Show expenses")
    return parser


def main():
    tracker = ExpenseTracker(DATA_FILE)
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        tracker.add_expense(args.title, args.amount)
        print("Expense added.")
    elif args.command == "list":
        tracker.show_expenses()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
