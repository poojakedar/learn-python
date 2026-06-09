"""Day 2: Input, type conversion, and operators."""

print("=== Day 2: Input and Operators ===")

# In real programs, input() returns text (string).
# We use fixed values first so this file can run without stopping for typing.
name = "Pooja"
age_text = "21"

print("Name:", name)
print("Age text:", age_text, "Type:", type(age_text))

# Convert string to number
age = int(age_text)
print("Age number:", age, "Type:", type(age))

# Arithmetic operators
a = 10
b = 3
print("\nArithmetic:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Comparison operators
print("\nComparison:")
print("a > b:", a > b)
print("a == b:", a == b)
print("a != b:", a != b)

# Try interactive input by uncommenting these lines:
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print("Hello", user_name, "next year you will be", user_age + 1)

print("\nDone! Now open exercises/day02_exercises.py")
