"""Day 13 exercises.

Goal: Practice package usage and safe imports.
Save final work as solutions/day13_solution.py
"""

from importlib.util import find_spec

print("=== Day 13 Exercises: Packages and pip ===")

# TODO 1: Check whether 'requests' package is installed.
if find_spec("requests") is not None:
    print("requests is installed")
else:
    print("requests is not installed")

# TODO 2: If installed, print requests version.
if find_spec("requests") is not None:
    import requests

    print("requests version:", requests.__version__)

# TODO 3: Use pip in terminal (outside this file):
# pip list
# pip show requests

# TODO 4: Create a dictionary with package names and whether installed.
packages = ["requests", "numpy", "pandas"]
availability = {}
for package in packages:
    availability[package] = find_spec(package) is not None

print("Package availability:")
for name, installed in availability.items():
    print(name, "->", installed)

# TODO 5: Optional challenge
# If requests is installed, make a GET request to https://httpbin.org/get
if find_spec("requests") is not None:
    try:
        import requests

        response = requests.get("https://httpbin.org/get", timeout=5)
        print("Status code:", response.status_code)
    except requests.RequestException as error:
        print("Request failed:", error)

print("\nGreat work! Save this as solutions/day13_solution.py")
