"""Day 6: Lists and dictionaries."""

print("=== Day 6: Lists and Dictionaries ===")

# Lists store ordered items
fruits = ["apple", "banana", "mango"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add and remove items
fruits.append("grapes")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

# Loop through a list
print("\nLoop through fruits:")
for fruit in fruits:
    print(fruit)

# Dictionaries store key-value pairs
student = {
    "name": "Pooja",
    "age": 21,
    "city": "Pune"
}

print("\nStudent dictionary:")
print(student)
print("Name:", student["name"])
print("Age:", student["age"])

# Update dictionary
student["age"] = 22
student["grade"] = "A"
print("Updated student:", student)

# Loop through dictionary keys and values
print("\nDictionary items:")
for key, value in student.items():
    print(key, "=", value)

print("\nDone! Now open exercises/day06_exercises.py")
