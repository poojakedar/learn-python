# Day 5 Concepts: Functions

Functions help you organize code into reusable blocks.
Instead of repeating code, you write it once and call it many times.

## 1) What is a function

A function is a named block of code that does one task.

Basic structure:

def function_name(parameters):
    # code block
    return value

## 2) Why use functions

1. Reuse: write once, use many times
2. Readability: code is easier to understand
3. Debugging: easier to test small parts
4. Organization: divide big problem into small parts

## 3) Defining and calling

Define:

def greet(name):
    print("Hello", name)

Call:
greet("Pooja")

## 4) Parameters and arguments

Parameter:
- Variable in function definition (name)

Argument:
- Actual value passed during call ("Pooja")

Example:

def add(a, b):
    return a + b

add(10, 20)

## 5) return vs print

print:
- Shows output on screen

return:
- Sends value back to caller

Use return when result is needed for later calculations.

## 6) Default parameters

You can set default values.

Example:

def introduce(name, city="Unknown"):
    print(name, city)

If city is not passed, it uses "Unknown".

## 7) Scope basics

Variables inside function are local.
They are not accessible outside unless returned.

## 8) Common beginner mistakes

1. Forgetting parentheses when calling function
2. Forgetting return when value is needed
3. Wrong indentation inside function
4. Mismatch in number of arguments

## 9) Practice checklist

After Day 5, you should be able to:

1. Create a function with one parameter
2. Create a function with two parameters
3. Return a value from function
4. Use function result in print or calculations
5. Use default parameters
