# Day 9 Concepts: OOP Basics

Object-oriented programming (OOP) helps organize code using classes and objects.

## 1) Class and object

Class:
- A blueprint/template

Object:
- A real instance created from class

Example idea:
- Class: Student
- Objects: student1, student2

## 2) __init__ method (constructor)

__init__ runs automatically when object is created.
Use it to set starting values.

Example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

## 3) self keyword

self means current object.
Use self to access object data and methods.

Example:
self.name
self.marks

## 4) Attributes and methods

Attributes:
- Data stored in object
- Example: name, age, balance

Methods:
- Functions inside class
- Example: deposit(), withdraw(), show_info()

## 5) Why OOP is useful

1. Better organization for large programs
2. Reuse through class design
3. Easier maintenance and readability
4. Real-world modeling (Student, Book, Account)

## 6) Common beginner mistakes

1. Forgetting self in method parameters
2. Not using self.attribute when storing values
3. Calling method without object
4. Confusing class name and object name

## 7) Practice checklist

After Day 9, you should be able to:

1. Create a class
2. Create objects from class
3. Store object data with __init__
4. Add methods to update and show data
5. Use multiple objects from one class
