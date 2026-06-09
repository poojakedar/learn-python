# Python Beginner Practice Setup

This workspace is organized so you can learn Python step by step.

## 1) Install Python (one-time)

1. Download Python from https://www.python.org/downloads/
2. During install, enable **Add Python to PATH**
3. Verify install in PowerShell:

```powershell
python --version
```

If `python` does not work, try:

```powershell
py --version
```

## 2) Set up VS Code for Python

1. Install the **Python** extension by Microsoft.
2. Open this folder (`c:\python`) in VS Code.
3. Press `Ctrl+Shift+P` -> **Python: Select Interpreter** -> choose your Python install.

## 3) How this folder is organized

- `lessons/`: concept demos you can run and read.
- `exercises/`: your practice tasks.
- `solutions/`: your completed answers.
- `projects/`: mini projects after basics.
- `concepts/`: simple theory notes for each day.

## 4) Run your first lesson

```powershell
python lessons/day01_variables.py
```

or

```powershell
py lessons/day01_variables.py
```

## 5) Do your first exercise

1. Open `exercises/day01_exercises.py`
2. Fill in the TODOs
3. Run it:

```powershell
python exercises/day01_exercises.py
```

## 6) Daily practice routine (30-45 mins)

1. Read one lesson file.
2. Complete one exercise file.
3. Save your answer in `solutions/`.
4. Build one tiny variation (change values, add one extra print, add one extra condition, etc).

## 7) Recommended learning order

1. Variables and data types
2. Input and operators
3. If/else
4. Loops
5. Functions
6. Lists and dictionaries
7. Files and exceptions
8. Mini projects

If you want, next I can generate Day 2 and Day 3 files automatically.
