"""Day 14: Important Python built-in libraries.

Covers: os, pathlib, math, random, json, datetime.
"""

import json
import math
import random
from datetime import date, datetime
from pathlib import Path

print("=== Day 14: Built-in Libraries ===")

# pathlib: file paths and file operations
base_path = Path(".")
notes_path = base_path / "day14_notes.txt"
notes_path.write_text("Learning built-in libraries\n", encoding="utf-8")
print("Created file:", notes_path)
print("File exists:", notes_path.exists())

# math: mathematical helpers
print("\nMath examples:")
print("sqrt(81):", math.sqrt(81))
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.9):", math.floor(4.9))
print("pi:", round(math.pi, 4))

# random: random values
print("\nRandom examples:")
print("random int 1-10:", random.randint(1, 10))
print("random choice:", random.choice(["red", "green", "blue"]))

# json: convert Python object to JSON and back
student = {"name": "Pooja", "score": 95, "passed": True}
json_text = json.dumps(student, indent=2)
print("\nJSON text:")
print(json_text)
restored = json.loads(json_text)
print("Restored object:", restored)

# datetime: date and time
print("\nDate/Time examples:")
print("Today:", date.today())
print("Now:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("\nDone! Now open exercises/day14_exercises_builtin_libraries.py")
