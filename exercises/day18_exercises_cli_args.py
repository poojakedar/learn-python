"""Day 18 exercises.

Goal: Practice argparse and CLI options.
Save final work as solutions/day18_solution.py
"""

import argparse

print("=== Day 18 Exercises: CLI Args ===")

parser = argparse.ArgumentParser(description="Calculator CLI")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("--operation", choices=["add", "subtract", "multiply", "divide"], default="add", help="Operation to perform")
parser.add_argument("--verbose", action="store_true", help="Show detailed steps")
args = parser.parse_args()

if args.verbose:
    print(f"Received num1={args.num1}, num2={args.num2}, operation={args.operation}")

if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
else:
    if args.num2 == 0:
        print("Cannot divide by zero")
        raise SystemExit(1)
    result = args.num1 / args.num2

print("Result:", result)
print("\nGreat work! Save this as solutions/day18_solution.py")
