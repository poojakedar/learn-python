"""Day 21: API basics with requests and JSON."""

import requests

print("=== Day 21: API Basics ===")

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=8)
    response.raise_for_status()
    users = response.json()

    print("Total users:", len(users))
    print("\nFirst 3 users:")
    for user in users[:3]:
        print(user["name"], "-", user["email"], "-", user["address"]["city"])
except requests.RequestException as error:
    print("API request failed:", error)

print("\nDone! Now open exercises/day21_exercises_api_basics.py")
