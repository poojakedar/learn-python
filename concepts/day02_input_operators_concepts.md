# Day 2 Concepts: Input and Operators

Day 2 teaches how to take user input and do calculations.

## 1) input function

input() reads data from keyboard.

Example:
name = input("Enter your name: ")

Important:
- input() always returns a string

## 2) Type conversion

To convert input text into number:

1. int() for whole numbers
2. float() for decimal numbers

Example:
age = int(input("Enter age: "))

## 3) Arithmetic operators

1. + addition
2. - subtraction
3. * multiplication
4. / normal division (float result)
5. // floor division (whole part)
6. % remainder
7. ** power

Example:
10 // 3 gives 3
10 % 3 gives 1

## 4) Comparison operators

Used to compare values.
Result is True or False.

1. == equal
2. != not equal
3. > greater than
4. < less than
5. >= greater than or equal
6. <= less than or equal

## 5) Operator precedence

Python follows precedence like math.
Parentheses help make order clear.

Example:
2 + 3 * 4 = 14
(2 + 3) * 4 = 20

## 6) Common beginner mistakes

1. Forgetting conversion before math
- input gives string, not number

2. Using = instead of == in comparison
- = assign
- == compare

3. Dividing by zero
- Causes error

## 7) Practice checklist

After Day 2 you should be able to:

1. Read input from user
2. Convert string to int
3. Do basic math operations
4. Compare numbers and print True/False
