"""Day 12 exercises.

Goal: Practice common Python built-in functions.
Save final work as solutions/day12_solution.py
"""

print("=== Day 12 Exercises: Built-in Functions ===")

# TODO 1: Create a list of 6 numbers and print len, max, min, sum.
numbers = [12, 5, 8, 19, 3, 10]
print("len:", len(numbers))
print("max:", max(numbers))
print("min:", min(numbers))
print("sum:", sum(numbers))

# TODO 2: Ask user for a word and print upper, lower, capitalize.
word = input("Enter a word: ")
print("upper:", word.upper())
print("lower:", word.lower())
print("capitalize:", word.capitalize())

# TODO 3: Ask user for a number as text and convert to int.
text_value = input("Enter a whole number: ")
try:
    number = int(text_value)
    print("Converted int:", number)
except ValueError:
    print("Invalid integer text")

# TODO 4: Use sorted on a list and print original + sorted.
values = [9, 2, 11, 4, 1]
print("original:", values)
print("sorted:", sorted(values))

# TODO 5: Print absolute value and rounded value examples.
print("abs(-45):", abs(-45))
print("round(7.856, 1):", round(7.856, 1))

print("\nGreat work! Save this as solutions/day12_solution.py")
