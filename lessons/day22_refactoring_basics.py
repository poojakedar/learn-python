"""Day 22: Refactoring basics.

Goal: Improve code readability without changing behavior.
"""

print("=== Day 22: Refactoring Basics ===")


def calculate_order_total(cart_items, tax_percent):
    """Return subtotal, tax amount, and final total."""
    subtotal = sum(item["price"] * item["qty"] for item in cart_items)
    tax_amount = subtotal * (tax_percent / 100)
    final_total = subtotal + tax_amount
    return subtotal, tax_amount, final_total


def print_receipt(cart_items, subtotal, tax_amount, final_total):
    print("\nReceipt")
    print("------")
    for item in cart_items:
        line_total = item["price"] * item["qty"]
        print(f"{item['name']} x{item['qty']} = {line_total}")
    print("Subtotal:", round(subtotal, 2))
    print("Tax:", round(tax_amount, 2))
    print("Total:", round(final_total, 2))


cart = [
    {"name": "Pen", "price": 10.0, "qty": 2},
    {"name": "Notebook", "price": 50.0, "qty": 1},
    {"name": "Pencil", "price": 5.0, "qty": 3},
]

subtotal, tax, total = calculate_order_total(cart, tax_percent=18)
print_receipt(cart, subtotal, tax, total)

print("\nRefactoring idea:")
print("Split large code into small named functions with one responsibility.")

print("\nDone! Now open exercises/day22_exercises_refactoring_basics.py")
