"""Day 15 exercises.

Goal: Practice using a third-party library after installation.
Save final work as solutions/day15_solution.py
"""

print("=== Day 15 Exercises: requests Library ===")

import requests

# TODO 1: Print requests version.
print("requests version:", requests.__version__)

# TODO 2: Make GET request to https://httpbin.org/get and print status code.
try:
    response = requests.get("https://httpbin.org/get", timeout=8)
    print("Status code:", response.status_code)
except requests.RequestException as error:
    print("Request failed:", error)

# TODO 3: Make GET request to https://api.github.com and print two JSON keys.
try:
    github = requests.get("https://api.github.com", timeout=8)
    data = github.json()
    print("current_user_url:", data.get("current_user_url"))
    print("repository_url:", data.get("repository_url"))
except requests.RequestException as error:
    print("GitHub request failed:", error)

# TODO 4: Handle invalid URL request inside try/except.
try:
    requests.get("https://invalid.invalid-domain-example", timeout=5)
except requests.RequestException:
    print("Handled invalid URL/network error successfully.")

print("\nGreat work! Save this as solutions/day15_solution.py")
