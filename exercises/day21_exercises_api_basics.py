"""Day 21 exercises.

Goal: Practice reading JSON data from APIs.
Save final work as solutions/day21_solution.py
"""

import requests

print("=== Day 21 Exercises: API Basics ===")

# TODO 1: Fetch posts from JSONPlaceholder.
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=8)
    response.raise_for_status()
    posts = response.json()
    print("Total posts:", len(posts))
except requests.RequestException as error:
    print("Could not fetch posts:", error)
    posts = []

# TODO 2: Print title of first 5 posts.
print("\nFirst 5 post titles:")
for post in posts[:5]:
    print("-", post["title"])

# TODO 3: Fetch users and print names + usernames.
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=8)
    response.raise_for_status()
    users = response.json()
    print("\nUsers:")
    for user in users[:5]:
        print(user["name"], "->", user["username"])
except requests.RequestException as error:
    print("Could not fetch users:", error)

# TODO 4: Count how many posts belong to userId = 1.
count = sum(1 for post in posts if post.get("userId") == 1)
print("\nPosts by userId=1:", count)

print("\nGreat work! Save this as solutions/day21_solution.py")
