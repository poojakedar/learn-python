"""Day 12: Python built-in functions."""

print("=== Day 12: Built-in Functions ===")

numbers = [4, 1, 9, 2, 7]
name = "pooja"
text_number = "123"

print("Original list:", numbers)
print("len(numbers):", len(numbers))
print("max(numbers):", max(numbers))
print("min(numbers):", min(numbers))
print("sum(numbers):", sum(numbers))
print("sorted(numbers):", sorted(numbers))

print("\nText functions:")
print("name:", name)
print("name.upper():", name.upper())
print("name.capitalize():", name.capitalize())
print("type(name):", type(name))

print("\nType conversion built-ins:")
print("int(text_number):", int(text_number))
print("float(5):", float(5))
print("str(3.14):", str(3.14))

print("\nRange and enumerate:")
for index, value in enumerate(numbers, start=1):
    print(index, value)

print("\nUsing abs and round:")
print("abs(-20):", abs(-20))
print("round(3.14159, 2):", round(3.14159, 2))

print("\nDone! Now open exercises/day12_exercises_builtin_functions.py")
