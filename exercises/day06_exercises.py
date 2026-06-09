"""Day 6 exercises.

Instructions:
1) Complete each TODO using lists and dictionaries.
2) Save final work as solutions/day06_solution.py
"""

print("=== Day 6 Exercises ===")

# TODO 1: Create a list of 5 numbers and print the list.
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

# TODO 2: Print the first and last item.
print("First:", numbers[0])
print("Last:", numbers[-1])

# TODO 3: Add one more number to the list and print the updated list.
numbers.append(60)
print("Updated numbers:", numbers)

# TODO 4: Create a dictionary with your name, age, and city.
student = {
    "name": "Pooja",
    "age": 21,
    "city": "Pune"
}
print("Student:", student)

# TODO 5: Update age and add hobby.
student["age"] = 22
student["hobby"] = "reading"
print("Updated student:", student)

# TODO 6: Loop through dictionary items and print them.
for key, value in student.items():
    print(key, "=>", value)

print("\nGreat work! Save this as solutions/day06_solution.py")
