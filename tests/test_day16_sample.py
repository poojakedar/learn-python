"""Sample discoverable tests for Day 16."""

import unittest


def square(n):
    return n * n


class TestSquare(unittest.TestCase):
    def test_square_positive(self):
        self.assertEqual(square(5), 25)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
