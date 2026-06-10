"""Day 19: JSON data files.

Learn how to save and load structured data using JSON.
"""

import json
from pathlib import Path

print("=== Day 19: JSON Data Files ===")

contacts_file = Path("day19_contacts.json")

contacts = [
    {"name": "Pooja", "phone": "111-222-3333", "city": "Pune"},
    {"name": "Asha", "phone": "444-555-6666", "city": "Mumbai"},
]

# Save Python list/dict to JSON file
contacts_file.write_text(json.dumps(contacts, indent=2), encoding="utf-8")
print("Saved contacts to:", contacts_file)

# Load JSON file back into Python object
loaded_contacts = json.loads(contacts_file.read_text(encoding="utf-8"))
print("\nLoaded contacts:")
for contact in loaded_contacts:
    print(contact["name"], contact["phone"], contact["city"])

# Append a new contact in Python, then save again
loaded_contacts.append({"name": "Ravi", "phone": "777-888-9999", "city": "Delhi"})
contacts_file.write_text(json.dumps(loaded_contacts, indent=2), encoding="utf-8")
print("\nAdded one more contact and saved again.")

print("\nDone! Now open exercises/day19_exercises_json_data_files.py")
