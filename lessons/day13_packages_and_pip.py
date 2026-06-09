"""Day 13: pip, packages, and third-party libraries."""

from importlib.util import find_spec

print("=== Day 13: Packages and pip ===")

# Standard library example (always available)
import datetime
print("Today:", datetime.date.today())

# Third-party package check (optional)
package_name = "requests"
if find_spec(package_name) is not None:
    import requests

    print("\nrequests is installed.")
    print("Version:", requests.__version__)

    try:
        response = requests.get("https://api.github.com", timeout=5)
        print("GET https://api.github.com ->", response.status_code)
    except requests.RequestException as error:
        print("Network request failed:", error)
else:
    print("\nrequests is NOT installed in this environment.")
    print("Install with:")
    print("pip install requests")

print("\nUseful pip commands:")
print("pip install <package>")
print("pip uninstall <package>")
print("pip list")
print("pip show <package>")
print("pip freeze > requirements.txt")

print("\nDone! Now open exercises/day13_exercises_packages_and_pip.py")
