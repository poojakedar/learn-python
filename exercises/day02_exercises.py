"""Day 2 exercises.

Instructions:
1) Run this file and complete all TODOs.
2) Use input(), int(), and operators.
3) Save your final answer as solutions/day02_solution.py
"""

print("=== Day 2 Exercises ===")

# TODO 1: Ask for user name and print a greeting.
name = input("Enter your name: ")
print("Hello", name)

# TODO 2: Ask for two numbers and print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# TODO 3: Print difference, product, and division.
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

# TODO 4: Ask for your age and show next year age.
age = int(input("Enter your age: "))
print("Next year age:", age + 1)

# TODO 5: Check if first number is greater than second number.
print("Is first number greater?", num1 > num2)

print("\nGreat work! Save this as solutions/day02_solution.py")
