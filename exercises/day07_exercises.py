"""Day 7 exercises.

Instructions:
1) Complete each TODO using file handling and exceptions.
2) Save final work as solutions/day07_solution.py
"""

print("=== Day 7 Exercises ===")

# TODO 1: Create a file named notes.txt and write 3 lines in it.
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

print("Created notes.txt")

# TODO 2: Read and print the full content of notes.txt.
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\nnotes.txt content:")
print(content)

# TODO 3: Append one more line to notes.txt and print updated content.
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Line 4 (appended)\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    updated_content = file.read()

print("Updated content:")
print(updated_content)

# TODO 4: Ask user for a number and handle invalid input with try/except.
user_text = input("Enter a whole number: ")
try:
    user_number = int(user_text)
    print("You entered:", user_number)
except ValueError:
    print("Invalid number. Please enter only digits.")

# TODO 5: Try reading a missing file and handle FileNotFoundError.
try:
    with open("not_exists.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found handled successfully.")

print("\nGreat work! Save this as solutions/day07_solution.py")
