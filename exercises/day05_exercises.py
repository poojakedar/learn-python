"""Day 5 exercises.

Instructions:
1) Complete each TODO using functions.
2) Save final work as solutions/day05_solution.py
"""

print("=== Day 5 Exercises ===")


# TODO 1: Write a function greet_user(name) that prints "Hello <name>"
def greet_user(name):
    print("Hello", name)


greet_user("Pooja")


# TODO 2: Write a function square(n) that returns square of n
def square(n):
    return n * n


print("Square of 6:", square(6))


# TODO 3: Write a function max_of_two(a, b) that returns larger value
def max_of_two(a, b):
    if a > b:
        return a
    return b


print("Max of 10 and 25:", max_of_two(10, 25))


# TODO 4: Write a function check_pass(mark) returning "Pass" if mark >= 35 else "Fail"
def check_pass(mark):
    if mark >= 35:
        return "Pass"
    return "Fail"


print("Result for 72:", check_pass(72))
print("Result for 20:", check_pass(20))


# TODO 5: Ask user for two numbers and print sum using add function

def add(a, b):
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", add(num1, num2))

print("\nGreat work! Save this as solutions/day05_solution.py")
