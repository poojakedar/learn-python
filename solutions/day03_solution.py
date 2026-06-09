age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

password = input("Enter password: ")
if password == "python123":
    print("Access granted")
else:
    print("Access denied")

print("\nGreat work! Save this as solutions/day03_solution.py")
