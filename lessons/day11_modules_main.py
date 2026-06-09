"""Day 11: Modules and project structure."""

from day11_math_utils import add, divide, multiply, subtract

print("=== Day 11: Modules and Structure ===")

x = 20
y = 5

print("x =", x, "y =", y)
print("Add:", add(x, y))
print("Subtract:", subtract(x, y))
print("Multiply:", multiply(x, y))
print("Divide:", divide(x, y))

try:
    print("Divide by zero test:", divide(x, 0))
except ValueError as error:
    print("Handled error:", error)

print("\nDone! Now open exercises/day11_exercises_main.py")
