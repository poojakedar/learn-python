# Day 23 Concepts: File and Folder Automation

Automation scripts help you avoid repetitive manual file work.

## 1) Why automate file tasks

1. Save time on repeated actions
2. Reduce human error
3. Handle many files quickly
4. Build useful utility scripts

## 2) pathlib basics

pathlib gives object-based path handling.

Common operations:
1. Path("folder") create path object
2. path.mkdir(parents=True, exist_ok=True)
3. path.exists()
4. path.iterdir()
5. path.glob("*.txt")
6. path.write_text(), path.read_text()

## 3) shutil basics

shutil is useful for copy/move operations.

Common functions:
1. shutil.copy2(src, dst)
2. shutil.move(src, dst)
3. shutil.rmtree(folder)

## 4) Rename and delete

Rename:
path.rename(new_path)

Delete file:
path.unlink()

Delete folder tree:
shutil.rmtree(path)

## 5) Safe automation habits

1. Test on small sample folder first
2. Print each operation during development
3. Check file exists before rename/delete
4. Keep backup when writing destructive scripts

## 6) Common beginner mistakes

1. Using wrong relative path
2. Forgetting exist_ok=True for mkdir
3. Renaming/moving files without checking existence
4. Accidentally overwriting important files

## 7) Practice checklist

After Day 23, you should be able to:
1. create folders programmatically
2. create and read files with pathlib
3. copy files with shutil
4. rename files safely
5. list directory contents for verification
