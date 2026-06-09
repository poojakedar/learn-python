"""Day 14 exercises.

Goal: Practice core built-in libraries.
Save final work as solutions/day14_solution.py
"""

import json
import math
import random
from datetime import datetime
from pathlib import Path

print("=== Day 14 Exercises: Built-in Libraries ===")

# TODO 1: Create a file day14_tasks.txt and write 3 lines.
file_path = Path("day14_tasks.txt")
file_path.write_text("Task 1\nTask 2\nTask 3\n", encoding="utf-8")
print("File created:", file_path)

# TODO 2: Read and print the file content using pathlib.
content = file_path.read_text(encoding="utf-8")
print("\nFile content:")
print(content)

# TODO 3: Use math library for sqrt, ceil, floor examples.
print("sqrt(49):", math.sqrt(49))
print("ceil(2.1):", math.ceil(2.1))
print("floor(9.9):", math.floor(9.9))

# TODO 4: Use random library to create one random number and one random choice.
print("Random number 1-100:", random.randint(1, 100))
print("Random fruit:", random.choice(["apple", "banana", "mango"]))

# TODO 5: Convert dictionary to JSON and save to day14_data.json.
data = {
    "name": "Pooja",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "completed": True
}

json_file = Path("day14_data.json")
json_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("Saved JSON to:", json_file)

# TODO 6: Read day14_data.json and print parsed dictionary.
loaded_data = json.loads(json_file.read_text(encoding="utf-8"))
print("Loaded data:", loaded_data)

print("\nGreat work! Save this as solutions/day14_solution.py")
