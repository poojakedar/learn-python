"""Day 5: Functions in Python."""

print("=== Day 5: Functions ===")


def greet(name):
    print("Hello", name)


def add_numbers(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


# Calling functions
greet("Pooja")

result = add_numbers(10, 20)
print("10 + 20 =", result)

print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))


# Function with default parameter
def introduce(name, city="Unknown"):
    print("Name:", name, "City:", city)


introduce("Pooja")
introduce("Asha", "Pune")

print("\nDone! Now open exercises/day05_exercises.py")
