"""Day 18: Command-line arguments and simple CLI tools."""

import argparse

print("=== Day 18: CLI Arguments ===")

parser = argparse.ArgumentParser(description="Simple greeting CLI")
parser.add_argument("name", help="Your name")
parser.add_argument("--times", type=int, default=1, help="Number of greetings")
parser.add_argument("--shout", action="store_true", help="Print greeting in uppercase")
args = parser.parse_args()

message = f"Hello, {args.name}!"
if args.shout:
    message = message.upper()

for _ in range(args.times):
    print(message)

print("\nDone! Now open exercises/day18_exercises_cli_args.py")
