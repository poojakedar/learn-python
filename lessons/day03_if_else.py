"""Day 3: if, elif, else conditions."""

print("=== Day 3: if / elif / else ===")

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

marks = 76

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Marks:", marks)
print("Grade:", grade)

number = -3
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# Try interactive input by uncommenting:
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

print("\nDone! Now open exercises/day03_exercises.py")
