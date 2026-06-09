"""Day 10: Beginner capstone (class + functions + files).

This lesson demonstrates a tiny Task Manager app structure.
"""

import json

print("=== Day 10: Capstone Lesson ===")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            return True
        return False

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['title']} [{status}]")

    def save(self, file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=2)

    def load(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []


manager = TaskManager()
manager.add_task("Learn Python")
manager.add_task("Practice loops")
manager.complete_task(0)

print("Current tasks:")
manager.list_tasks()

manager.save("day10_tasks.json")
print("Saved tasks to day10_tasks.json")

# Show loading works
new_manager = TaskManager()
new_manager.load("day10_tasks.json")
print("\nLoaded tasks:")
new_manager.list_tasks()

print("\nDone! Now open exercises/day10_exercises.py")
