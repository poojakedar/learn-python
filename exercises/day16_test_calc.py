"""Day 16 exercises.

Goal: Write and run unittest test cases.
Save final work as solutions/day16_solution.py (or keep as test file output).
"""

import unittest

from day16_calc import is_even, multiply, safe_subtract


class TestDay16Calc(unittest.TestCase):
    # TODO 1: Test multiply with positive numbers.
    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    # TODO 2: Test multiply with zero.
    def test_multiply_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    # TODO 3: Test is_even for an even number.
    def test_is_even_true(self):
        self.assertTrue(is_even(8))

    # TODO 4: Test is_even for an odd number.
    def test_is_even_false(self):
        self.assertFalse(is_even(7))

    # TODO 5: Test safe_subtract result.
    def test_safe_subtract(self):
        self.assertEqual(safe_subtract(10, 3), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
