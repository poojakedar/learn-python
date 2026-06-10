# Day 22 Concepts: Refactoring Basics

Refactoring means improving code structure without changing output behavior.

## 1) Why refactoring is important

1. Code becomes easier to read
2. Bugs become easier to find
3. Repeated logic is reduced
4. Future changes become safer

## 2) Signs code needs refactoring

1. repeated code blocks
2. very long functions
3. unclear variable names
4. too many nested conditions

## 3) Common refactoring steps

1. Extract function
2. Rename variables for clarity
3. Remove duplicate logic
4. Split one big function into smaller units

## 4) Keep behavior the same

Refactoring should not change what code does.
Only internal structure should improve.

A good rule:
1. run code/tests before refactor
2. refactor small piece
3. run code/tests again

## 5) DRY principle

DRY means "Don't Repeat Yourself".
If the same logic appears in multiple places, move it to one function.

## 6) Refactoring with confidence

Use tests to confirm behavior is still correct.
If tests pass before and after, refactor is safer.

## 7) Common beginner mistakes

1. doing too many changes at once
2. changing logic accidentally while cleaning code
3. deleting useful validation
4. renaming too aggressively without checking usage

## 8) Practice checklist

After Day 22, you should be able to:
1. identify duplicated logic
2. extract reusable functions
3. rename unclear variables
4. simplify output/summary code
5. keep behavior same after cleanup
