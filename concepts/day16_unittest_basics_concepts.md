# Day 16 Concepts: Unit Testing with unittest

Unit testing means checking small pieces of code automatically.
Python includes `unittest` in the standard library.

## 1) Why testing is useful

1. Finds bugs early
2. Prevents old code from breaking after changes
3. Gives confidence when refactoring
4. Documents expected behavior

## 2) Basic unittest structure

A test file usually has:
1. imports
2. class that extends unittest.TestCase
3. test methods that start with `test_`
4. `unittest.main()` to run tests

## 3) Common assertions

1. assertEqual(a, b)
2. assertTrue(value)
3. assertFalse(value)
4. assertRaises(ErrorType)

## 4) Running tests

Run a single test file:
python exercises/day16_test_calc.py

Run all tests in tests folder:
python -m unittest discover -s tests -p "test_*.py"

## 5) Good test habits

1. One idea per test
2. Use clear test method names
3. Keep tests independent
4. Test normal and edge cases

## 6) Common beginner mistakes

1. Forgetting `test_` prefix in method name
2. Import path errors
3. Expecting exceptions without using assertRaises
4. Changing production code to satisfy wrong test expectations

## 7) Practice checklist

After Day 16, you should be able to:
1. Create a unittest class
2. Write 4-5 basic assertions
3. Run tests from terminal
4. Read pass/fail output
5. Fix code using test feedback
