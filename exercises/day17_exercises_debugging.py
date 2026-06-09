"""Day 17 exercises.

Goal: Practice debugging and fixing bugs.
Save final work as solutions/day17_solution.py
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

print("=== Day 17 Exercises: Debugging ===")


# TODO 1: Fix the bug: function should return average, not sum.
def average(numbers):
    logging.info("average() input: %s", numbers)
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# TODO 2: Fix possible crash for division by zero.
def safe_divide(a, b):
    logging.info("safe_divide() called with a=%s, b=%s", a, b)
    if b == 0:
        return None
    return a / b


# TODO 3: Add helpful debug logs in find_item.
def find_item(items, target):
    logging.info("find_item() target=%s", target)
    for index, item in enumerate(items):
        logging.info("Checking index=%s item=%s", index, item)
        if item == target:
            return index
    return -1


values = [5, 10, 15, 20]
print("Average:", average(values))

print("Divide 12 by 3:", safe_divide(12, 3))
print("Divide 12 by 0:", safe_divide(12, 0))

fruits = ["apple", "banana", "mango"]
print("Index of mango:", find_item(fruits, "mango"))
print("Index of orange:", find_item(fruits, "orange"))

print("\nGreat work! Save this as solutions/day17_solution.py")
