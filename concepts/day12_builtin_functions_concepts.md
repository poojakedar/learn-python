# Day 12 Concepts: Python Built-in Functions

Built-in functions are ready-made functions provided by Python.
You can use them directly without importing extra modules.

## 1) Why built-ins matter

1. Save time
2. Reduce bugs
3. Make code shorter and clearer
4. Improve performance in many common tasks

## 2) Common built-ins for collections

For lists and similar data:
1. len(data) -> number of items
2. max(data) -> largest item
3. min(data) -> smallest item
4. sum(data) -> total of numeric items
5. sorted(data) -> new sorted list

## 3) Common built-ins for type conversion

1. int(text) -> convert to integer
2. float(value) -> convert to decimal
3. str(value) -> convert to string
3. bool(value) -> convert to True/False

## 4) Useful numeric built-ins

1. abs(x) -> absolute value
2. round(x, n) -> rounded value with n digits
3. pow(a, b) -> a raised to power b

## 5) Iteration helpers

1. range(start, stop, step) -> number sequence
2. enumerate(list) -> index + value pair

## 6) Type checking and help

1. type(value) -> returns data type
2. isinstance(value, type) -> type check
3. help(function) -> shows documentation in console

## 7) Common beginner mistakes

1. Forgetting parentheses, for example len instead of len(list)
2. Passing wrong type to function, for example sum("123")
3. Expecting sorted(list) to change original list in place
4. Conversion errors, for example int("abc")

## 8) Practice checklist

After Day 12, you should be able to:
1. Use len, max, min, sum, sorted
2. Convert values with int, float, str
3. Use abs and round for numeric cleanup
4. Use enumerate in loops
5. Handle ValueError when conversion fails
