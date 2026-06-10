"""Day 20: Capstone app combining classes, JSON, logging, and CLI commands.

Run without arguments to see a built-in demo.
Run with arguments, for example:
python lessons/day20_capstone_app.py add "Learn JSON"
python lessons/day20_capstone_app.py list
"""

import argparse
import json
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

DATA_FILE = Path("day20_tasks.json")


class TaskApp:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = []
        self.load()

    def load(self):
        if self.file_path.exists():
            self.tasks = json.loads(self.file_path.read_text(encoding="utf-8"))
            logging.info("Loaded %s tasks", len(self.tasks))
        else:
            self.tasks = []
            logging.info("No task file found. Starting fresh.")

    def save(self):
        self.file_path.write_text(json.dumps(self.tasks, indent=2), encoding="utf-8")
        logging.info("Saved %s tasks", len(self.tasks))

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})
        logging.info("Added task: %s", title)
        self.save()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            logging.info("Completed task: %s", self.tasks[index]["title"])
            self.save()
            return True
        logging.warning("Invalid task number: %s", index + 1)
        return False

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{idx}. {task['title']} [{status}]")


def build_parser():
    parser = argparse.ArgumentParser(description="Day 20 task manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    subparsers.add_parser("list", help="Show all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task complete")
    done_parser.add_argument("number", type=int, help="Task number starting from 1")

    return parser


def run_demo(app):
    print("=== Day 20: Capstone Demo ===")
    if app.file_path.exists():
        app.file_path.unlink()
    app.tasks = []
    app.add_task("Practice CLI")
    app.add_task("Practice JSON")
    app.complete_task(0)
    app.show_tasks()
    print("\nDone! Now open exercises/day20_exercises_capstone_app.py")


def main():
    app = TaskApp(DATA_FILE)
    parser = build_parser()

    if len(sys.argv) == 1:
        run_demo(app)
        return

    args = parser.parse_args()

    if args.command == "add":
        app.add_task(args.title)
    elif args.command == "list":
        app.show_tasks()
    elif args.command == "done":
        app.complete_task(args.number - 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
