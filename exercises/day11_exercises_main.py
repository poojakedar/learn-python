"""Day 11 exercises.

Goal: Practice creating and importing modules.
Save final work as solutions/day11_solution.py
"""

from day11_helpers import celsius_to_fahrenheit, is_adult, percentage

print("=== Day 11 Exercises: Modules ===")

# TODO 1: Use imported celsius_to_fahrenheit for values 0, 25, 37.
print("0C ->", celsius_to_fahrenheit(0), "F")
print("25C ->", celsius_to_fahrenheit(25), "F")
print("37C ->", celsius_to_fahrenheit(37), "F")

# TODO 2: Ask user age and use imported is_adult.
age = int(input("Enter your age: "))
if is_adult(age):
    print("Adult")
else:
    print("Minor")

# TODO 3: Ask user marks and total marks, then show percentage.
marks = float(input("Enter marks obtained: "))
total = float(input("Enter total marks: "))

try:
    result = percentage(marks, total)
    print("Percentage:", result)
except ValueError as error:
    print("Error:", error)

print("\nGreat work! Save this as solutions/day11_solution.py")
