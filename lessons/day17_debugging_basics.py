"""Day 17: Debugging basics.

Topics:
1) Read traceback
2) Use logging
3) Add debug prints
4) Handle errors clearly
"""

import logging

print("=== Day 17: Debugging Basics ===")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def divide_numbers(a, b):
    logging.info("divide_numbers called with a=%s, b=%s", a, b)
    return a / b


def process_values(values):
    logging.info("process_values called with %s", values)
    total = 0
    for value in values:
        logging.info("Adding value=%s", value)
        total += value
    return total


numbers = [10, 20, 30]
print("Total:", process_values(numbers))

try:
    print("Divide 10 by 2:", divide_numbers(10, 2))
    print("Divide 10 by 0:", divide_numbers(10, 0))
except ZeroDivisionError as error:
    print("Caught error:", error)

print("\nDebugging tip:")
print("In VS Code, set a breakpoint beside a line number and press F5.")
print("Use Step Over (F10) and inspect variables while code runs.")

print("\nDone! Now open exercises/day17_exercises_debugging.py")
