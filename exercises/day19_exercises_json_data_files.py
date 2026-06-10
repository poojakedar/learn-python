"""Day 19 exercises.

Goal: Practice saving and loading JSON data.
Save final work as solutions/day19_solution.py
"""

import json
from pathlib import Path

print("=== Day 19 Exercises: JSON Files ===")

# TODO 1: Create a list of 3 students and save to students.json.
students = [
    {"name": "Pooja", "marks": 90},
    {"name": "Asha", "marks": 85},
    {"name": "Ravi", "marks": 78},
    {"name": "Suresh", "marks": 88}
]

students_file = Path("students.json")
students_file.write_text(json.dumps(students, indent=2), encoding="utf-8")
print("Saved students.json")

# TODO 2: Load students.json and print each student.
loaded_students = json.loads(students_file.read_text(encoding="utf-8"))
print("\nLoaded students:")
for student in loaded_students:
    print(student["name"], student["marks"])

# TODO 3: Add a new student and save again.
loaded_students.append({"name": "Neha", "marks": 92})
students_file.write_text(json.dumps(loaded_students, indent=2), encoding="utf-8")
print("Added one more student.")

# TODO 4: Read back the updated file and count students.
updated_students = json.loads(students_file.read_text(encoding="utf-8"))
print("Total students:", len(updated_students))

# TODO 5: Find and print highest marks.
highest = max(student["marks"] for student in updated_students)
print("Highest marks:", highest)

print("\nGreat work! Save this as solutions/day19_solution.py")
