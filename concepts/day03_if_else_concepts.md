# Day 3 Concepts: if, elif, else

Conditions help your program make decisions.

## 1) Why conditions are needed

Without conditions, program does same thing every time.
With conditions, output changes based on data.

## 2) if statement

if runs a block when condition is True.

Example:
age = 20
if age >= 18:
    print("Adult")

## 3) else statement

else runs when if condition is False.

Example:
if age >= 18:
    print("Adult")
else:
    print("Minor")

## 4) elif statement

Use elif for multiple conditions.

Example:
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")

## 5) Indentation is very important

Python uses indentation to define blocks.
All lines inside if/else/elif must align correctly.

## 6) Nested conditions

You can put one if inside another if.
Use this when decisions depend on multiple checks.

## 7) Common beginner mistakes

1. Using = instead of ==
2. Bad indentation
3. Wrong condition order in elif
- Put most specific/highest checks first

## 8) Practice checklist

After Day 3 you should be able to:

1. Check if number is positive/negative/zero
2. Check adult/minor using age
3. Create grade system with if-elif-else
4. Compare password text and print result
