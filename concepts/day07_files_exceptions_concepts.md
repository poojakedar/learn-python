# Day 7 Concepts: Files and Exceptions

Day 7 teaches how to save data in files and how to handle errors safely.

## 1) Why files are important

Variables keep data only while program is running.
Files keep data even after program ends.

Examples:
1. Save notes
2. Save scores
3. Save logs

## 2) open function and file modes

Basic pattern:
with open("file_name.txt", "mode", encoding="utf-8") as file:
    # file operations

Common modes:
1. "w" write: create new or overwrite existing
2. "r" read: read existing file
3. "a" append: add text at end

## 3) Why use with open

with automatically closes the file after block ends.
This is safer and recommended.

## 4) Reading and writing

Write:
file.write("Hello\n")

Read all content:
content = file.read()

## 5) What are exceptions

An exception is an error that happens while program runs.

Examples:
1. ValueError: invalid type conversion
2. FileNotFoundError: file does not exist
3. ZeroDivisionError: divide by zero

## 6) try and except

Use try-except so program does not crash.

Pattern:
try:
    # risky code
except SomeError:
    # error handling

## 7) Multiple except blocks

You can handle different errors separately.
This helps print clear messages.

## 8) Common beginner mistakes

1. Forgetting file mode
2. Using "w" when you wanted "a" (overwrites file)
3. Not handling invalid user input
4. Forgetting newline \n when writing multiple lines

## 9) Practice checklist

After Day 7, you should be able to:

1. Create and write a text file
2. Read file content
3. Append data to existing file
4. Catch ValueError from input conversion
5. Catch FileNotFoundError for missing files
