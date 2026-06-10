# Day 21 Concepts: API Basics

An API lets one program talk to another program over the network.
Many APIs return JSON data.

## 1) What is an API

API stands for Application Programming Interface.
In beginner Python work, this often means making HTTP requests to web services.

## 2) Common API workflow

1. send request
2. receive response
3. check status
4. convert JSON to Python data
5. use the data

## 3) GET requests

GET is used to fetch data.

Example:
response = requests.get(url)

## 4) Important response parts

1. response.status_code
2. response.json()
3. response.text
4. response.raise_for_status()

## 5) JSON response structure

API data often comes as:
1. list of dictionaries
2. nested dictionaries
3. list inside dictionary

You access it like normal Python objects.

## 6) Error handling

Always use try/except for network code.
Possible problems:
1. no internet
2. timeout
3. invalid URL
4. server error

## 7) Common beginner mistakes

1. forgetting response.json() before using data
2. assuming API always returns success
3. not checking nested keys carefully
4. printing too much full JSON instead of selected fields

## 8) Practice checklist

After Day 21, you should be able to:
1. fetch API data with requests
2. check request success
3. convert JSON to Python objects
4. read selected fields from nested data
5. summarize API data with loops and conditions
