# Day 14 Concepts: Important Built-in Libraries

This day focuses on common libraries included with Python.
No extra installation is needed.

## 1) pathlib

Use pathlib for file and folder paths.
It is cleaner than string-based path handling.

Common usage:
1. Path("file.txt")
2. path.exists()
3. path.read_text()
4. path.write_text()

## 2) os

os helps with operating system tasks.

Examples:
1. os.getcwd() current folder
2. os.listdir() list items
3. os.environ environment variables

## 3) math

math gives extra numeric functions.

Examples:
1. math.sqrt(x)
2. math.ceil(x)
3. math.floor(x)
4. math.pi

## 4) random

random helps generate random values.

Examples:
1. random.randint(a, b)
2. random.choice(list)
3. random.shuffle(list)

## 5) json

json converts between Python objects and JSON text.

Examples:
1. json.dumps(data) Python -> JSON string
2. json.loads(text) JSON string -> Python
3. json.dump(data, file) save to file
4. json.load(file) read from file

## 6) datetime

datetime helps with dates and times.

Examples:
1. date.today()
2. datetime.now()
3. strftime for custom formatting

## 7) Common beginner mistakes

1. Forgetting to import library before use
2. Confusing json.dumps and json.dump
3. Writing JSON dict directly without conversion
4. Path mistakes due to wrong relative location

## 8) Practice checklist

After Day 14, you should be able to:
1. Create/read files with pathlib
2. Use math helpers for calculations
3. Generate random values
4. Save and read JSON data
5. Print formatted current time
