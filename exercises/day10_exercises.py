"""Day 10 exercises.

Goal: Build a complete menu-based Task Manager app.
Save final work as solutions/day10_solution.py
"""

import json

print("=== Day 10 Exercise: Task Manager Capstone ===")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nTasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['title']} [{status}]")

    def save_tasks(self, file_name="day10_tasks.json"):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=2)
        print(f"Saved to {file_name}")

    def load_tasks(self, file_name="day10_tasks.json"):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
            print(f"Loaded from {file_name}")
        except FileNotFoundError:
            print("No saved file found. Starting fresh.")


# TODO 1: Keep this menu loop running until user exits.
# TODO 2: Add new task from user input.
# TODO 3: Show task list.
# TODO 4: Complete task using task number.
# TODO 5: Save tasks and load tasks.
def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\nMenu")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Save tasks")
        print("5. Load tasks")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            title = input("Enter task title: ").strip()
            if title:
                manager.add_task(title)
                print("Task added.")
            else:
                print("Task title cannot be empty.")
        elif choice == "2":
            manager.show_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to complete: "))
                manager.complete_task(task_number - 1)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            manager.save_tasks()
        elif choice == "5":
            manager.load_tasks()
        elif choice == "6":
            print("Great job. Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


main()

print("\nGreat work! Save this as solutions/day10_solution.py")
