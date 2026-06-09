"""Day 16: unittest basics.

Run this file directly to see tests execute.
"""

import unittest


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestMathFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    print("=== Day 16: Unit Testing with unittest ===")
    unittest.main(verbosity=2)
