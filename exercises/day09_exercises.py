"""Day 9 exercises.

Instructions:
1) Complete each TODO using classes and objects.
2) Save final work as solutions/day09_solution.py
"""

print("=== Day 9 Exercises ===")


# TODO 1: Create a class Book with title and author.
# TODO 2: Add method show_details() to print title and author.
# TODO 3: Create 2 book objects and show details.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}")


book1 = Book("Python Basics", "Alice")
book2 = Book("Learn Coding", "Bob")
book1.show_details()
book2.show_details()


# TODO 4: Create class BankAccount with owner and balance.
# Add methods deposit(amount), withdraw(amount), and show_balance().
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.owner} balance: {self.balance}")


account = BankAccount("Pooja", 1000)
account.deposit(500)
account.withdraw(300)
account.show_balance()

print("\nGreat work! Save this as solutions/day09_solution.py")
