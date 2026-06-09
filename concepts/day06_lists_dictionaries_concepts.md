# Day 6 Concepts: Lists and Dictionaries

Lists and dictionaries are two very important data structures in Python.
They help you store many values in organized ways.

## 1) Lists

A list stores multiple items in order.

Example:
fruits = ["apple", "banana", "mango"]

Important:
- List items keep order
- Lists can contain duplicates
- Lists can be changed after creation

## 2) Indexing in lists

Each item has an index starting at 0.

Example:
- fruits[0] is first item
- fruits[1] is second item
- fruits[-1] is last item

## 3) Common list methods

1. append() - add item at end
2. remove() - remove first matching item
3. insert() - add item at a specific position
4. pop() - remove and return item

## 4) Looping through a list

Use for loop to read each item.

Example:
for fruit in fruits:
    print(fruit)

## 5) Dictionaries

A dictionary stores key-value pairs.

Example:
student = {
    "name": "Pooja",
    "age": 21,
    "city": "Pune"
}

Important:
- Keys must be unique
- Keys are used to find values
- Dictionary order is based on insertion in modern Python

## 6) Accessing dictionary values

Example:
student["name"]
student["age"]

## 7) Updating dictionaries

You can change values or add new keys.

Example:
student["age"] = 22
student["grade"] = "A"

## 8) Looping through dictionaries

Use .items() to get key and value together.

Example:
for key, value in student.items():
    print(key, value)

## 9) Common beginner mistakes

1. Using wrong index for list
2. Trying to access a key that does not exist
3. Confusing list and dictionary syntax
- List uses [] with positions
- Dictionary uses key names

## 10) Practice checklist

After Day 6 you should be able to:

1. Create a list
2. Read items using index
3. Add and remove list items
4. Create a dictionary
5. Access and update dictionary values
6. Loop through dictionary items
