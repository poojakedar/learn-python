"""Day 7: Files and exception handling."""

print("=== Day 7: Files and Exceptions ===")

file_name = "day07_demo.txt"

# Write text to a file
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python Day 7\n")
    file.write("Learning files and exceptions\n")

print("File written:", file_name)

# Read text from a file
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile content:")
print(content)

# Append text to the same file
with open(file_name, "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")

print("Appended one line to", file_name)

# Exception handling example
try:
    number = int("abc")
    print(number)
except ValueError:
    print("Caught ValueError: cannot convert text to int")

# File-not-found handling
try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Caught FileNotFoundError: file does not exist")

print("\nDone! Now open exercises/day07_exercises.py")
