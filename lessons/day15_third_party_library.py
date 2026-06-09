"""Day 15: Install and use a third-party library (requests)."""

print("=== Day 15: Third-Party Library (requests) ===")

import requests

print("requests version:", requests.__version__)

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=8)
    print("Status code:", response.status_code)

    # Convert JSON response to Python dictionary
    data = response.json()
    print("Current user URL:", data.get("current_user_url"))
    print("Current user authorizations HTML URL:", data.get("current_user_authorizations_html_url"))
except requests.RequestException as error:
    print("Network error:", error)

print("\nInstall command used for this lesson:")
print("pip install requests")

print("\nDone! Now open exercises/day15_exercises_third_party_library.py")
