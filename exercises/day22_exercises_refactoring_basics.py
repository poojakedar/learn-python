"""Day 22 exercises.

Goal: Refactor repeated and messy code into cleaner functions.
Save final work as solutions/day22_solution.py
"""

print("=== Day 22 Exercises: Refactoring ===")

# Imagine this is old code with repeated logic.
# TODO 1: Refactor repeated grade logic into one function get_grade(mark).


def get_grade(mark):
    if mark >= 90:
        return "A"
    if mark >= 75:
        return "B"
    if mark >= 60:
        return "C"
    return "D"


students = [
    {"name": "Pooja", "mark": 92},
    {"name": "Asha", "mark": 76},
    {"name": "Ravi", "mark": 61},
    {"name": "Neha", "mark": 48},
]

# TODO 2: Use helper function to avoid duplicate grade conditions.
print("\nStudent grades:")
for student in students:
    grade = get_grade(student["mark"])
    print(student["name"], "->", grade)


# TODO 3: Extract average logic into function calculate_average(marks).
def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


marks = [student["mark"] for student in students]
average_mark = calculate_average(marks)
print("\nAverage mark:", round(average_mark, 2))


# TODO 4: Create function print_summary(students) for cleaner output.
def print_summary(students_data):
    print("\nSummary")
    print("-------")
    for student in students_data:
        print(student["name"], "mark:", student["mark"], "grade:", get_grade(student["mark"]))


print_summary(students)

print("\nGreat work! Save this as solutions/day22_solution.py")
