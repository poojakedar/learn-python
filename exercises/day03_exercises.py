"""Day 3 exercises.

Instructions:
1) Complete each TODO.
2) Use if, elif, else.
3) Save final work as solutions/day03_solution.py
"""

print("=== Day 3 Exercises ===")

# TODO 1: Ask for age and print Adult/Minor.
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# TODO 2: Ask for a number and print Positive/Negative/Zero.
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# TODO 3: Ask for marks and print grade:
# 90+ A, 75-89 B, 60-74 C, below 60 D
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# TODO 4: Ask for a password and check if it matches "python123".
password = input("Enter password: ")
if password == "python123":
    print("Access granted")
else:
    print("Access denied")

print("\nGreat work! Save this as solutions/day03_solution.py")
