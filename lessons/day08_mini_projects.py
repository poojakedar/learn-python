"""Day 8: Mini project style coding.

This lesson shows how to combine input, loops, functions, lists,
and file handling into one small app-like flow.
"""

print("=== Day 8: Mini Projects ===")


def calculate_total(prices):
    """Return sum of all prices in a list."""
    return sum(prices)


def save_total(total, file_path):
    """Save result to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Total amount: {total}\n")


def main():
    prices = []

    print("Enter 3 item prices:")
    for i in range(1, 4):
        value = float(input(f"Price {i}: "))
        prices.append(value)

    total = calculate_total(prices)
    print("\nItems:", prices)
    print("Total:", total)

    save_total(total, "day08_total.txt")
    print("Saved total in day08_total.txt")


main()

print("\nDone! Now open exercises/day08_exercises.py")
