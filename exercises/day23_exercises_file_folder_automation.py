"""Day 23 exercises.

Goal: Automate file/folder tasks with pathlib and shutil.
Save final work as solutions/day23_solution.py
"""

from pathlib import Path
import shutil

print("=== Day 23 Exercises: File/Folder Automation ===")

workspace = Path("day23_exercise_workspace")
inbox = workspace / "inbox"
archive = workspace / "archive"

# TODO 1: Create workspace, inbox, archive folders.
inbox.mkdir(parents=True, exist_ok=True)
archive.mkdir(parents=True, exist_ok=True)
print("Folders ready.")

# TODO 2: Create 3 text files in inbox.
(inbox / "task1.txt").write_text("Task one\n", encoding="utf-8")
(inbox / "task2.txt").write_text("Task two\n", encoding="utf-8")
(inbox / "task3.txt").write_text("Task three\n", encoding="utf-8")
print("Created 3 files in inbox.")

# TODO 3: Copy all text files from inbox to archive.
for file in inbox.glob("*.txt"):
    shutil.copy2(file, archive / file.name)
print("Copied files to archive.")

# TODO 4: Rename task3.txt in archive to completed_task3.txt.
old_file = archive / "task3.txt"
new_file = archive / "completed_task3.txt"
if old_file.exists():
    old_file.rename(new_file)
print("Renamed task3 in archive.")

# TODO 5: Print all file names in archive.
print("\nArchive files:")
for file in archive.iterdir():
    print("-", file.name)

print("\nGreat work! Save this as solutions/day23_solution.py")
