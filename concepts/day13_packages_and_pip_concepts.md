# Day 13 Concepts: Packages and pip

Day 13 teaches how to use external libraries in Python projects.

## 1) What is a package

A package is a collection of reusable Python code.

Examples:
1. requests for HTTP calls
2. numpy for numerical work
3. pandas for data analysis

## 2) Standard library vs third-party

Standard library:
- Comes with Python installation
- Example: datetime, json, math

Third-party library:
- Must be installed separately
- Example: requests, numpy, pandas

## 3) What is pip

pip is Python's package manager.
It installs, updates, and removes third-party packages.

Common commands:
1. pip install requests
2. pip uninstall requests
3. pip list
4. pip show requests
5. pip freeze > requirements.txt

## 4) requirements.txt

requirements.txt stores package names and versions.
This helps recreate the same environment on another machine.

Install from file:
pip install -r requirements.txt

## 5) Why virtual environments matter

Virtual environments keep project dependencies separate.
This prevents version conflicts between projects.

## 6) Safe import pattern

When teaching beginners, you can check package availability first
so scripts do not crash if package is missing.

Example idea:
- check with importlib.util.find_spec
- import only if available

## 7) Common beginner mistakes

1. Installing packages in wrong Python environment
2. Forgetting to activate venv before pip install
3. Using package without installing it
4. Missing requirements.txt in project

## 8) Practice checklist

After Day 13, you should be able to:
1. Install a package with pip
2. Check if a package is installed
3. Import and use third-party package safely
4. Generate requirements.txt
5. Explain standard library vs third-party library
