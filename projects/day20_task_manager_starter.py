"""Day 20 starter project.

Expand this into a fuller app with edit/delete/search commands.
"""

import json
from pathlib import Path

DATA_FILE = Path("project_tasks.json")


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load()

    def load(self):
        if DATA_FILE.exists():
            self.tasks = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    def save(self):
        DATA_FILE.write_text(json.dumps(self.tasks, indent=2), encoding="utf-8")

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})
        self.save()

    def show_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task['title']} [{task['done']}]")


if __name__ == "__main__":
    app = TaskManager()
    app.add_task("Build project version")
    app.show_tasks()
