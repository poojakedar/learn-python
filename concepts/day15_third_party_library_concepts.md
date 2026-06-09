# Day 15 Concepts: Installing and Using Third-Party Libraries

This day is focused on one practical workflow:
1. install a package
2. import it in Python
3. use it safely

## 1) What is a third-party library

A third-party library is code written by others and shared for reuse.
It is not included in standard Python by default.

Example:
- requests for HTTP API calls

## 2) Install command

Install with pip:

pip install requests

If you use a virtual environment, activate it first.
Then install so package is added to that environment.

## 3) Use in code

After install:

import requests
response = requests.get("https://api.github.com")
print(response.status_code)

## 4) Why try/except is important

Network calls can fail due to:
1. no internet
2. timeout
3. invalid URL
4. server issues

Use:
try:
    ...
except requests.RequestException:
    ...

## 5) Requirements file

Store dependencies in requirements.txt so project setup is repeatable.

Create/update:
pip freeze > requirements.txt

Install from file:
pip install -r requirements.txt

## 6) Common beginner mistakes

1. Installing in one env, running in another env
2. Forgetting import statement
3. Not handling network errors
4. Assuming every response is successful

## 7) Practice checklist

After Day 15, you should be able to:
1. Install requests with pip
2. Import and use requests in code
3. Make GET request and read status code
4. Parse JSON response with response.json()
5. Handle request errors safely
