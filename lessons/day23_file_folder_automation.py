"""Day 23: File and folder automation with pathlib and shutil."""

from pathlib import Path
import shutil

print("=== Day 23: File/Folder Automation ===")

base = Path("day23_workspace")
source = base / "source"
backup = base / "backup"

# Create folders if missing
source.mkdir(parents=True, exist_ok=True)
backup.mkdir(parents=True, exist_ok=True)
print("Created folders:", source, "and", backup)

# Create sample files
(source / "notes1.txt").write_text("Python automation day 23\n", encoding="utf-8")
(source / "notes2.txt").write_text("Practice pathlib and shutil\n", encoding="utf-8")
print("Created sample files in source")

# Copy all .txt files from source to backup
for file in source.glob("*.txt"):
    shutil.copy2(file, backup / file.name)
    print("Copied:", file.name)

# Rename one copied file
old_name = backup / "notes2.txt"
new_name = backup / "notes2_renamed.txt"
if old_name.exists():
    if new_name.exists():
        new_name.unlink()
    old_name.rename(new_name)
    print("Renamed notes2.txt -> notes2_renamed.txt")

# List final files in backup
print("\nBackup folder files:")
for file in backup.iterdir():
    print("-", file.name)

print("\nDone! Now open exercises/day23_exercises_file_folder_automation.py")
