# Day 4 Concepts: Loops

Loops help you repeat code without writing the same lines again and again.

## 1) Why loops are useful

Without loops, printing numbers 1 to 10 needs 10 print statements.
With loops, you write just a few lines.

## 2) for loop

A for loop is used when you already know how many times you want to repeat.

Example idea:
- Repeat 5 times
- Go through each item in a list

Common pattern:
- for i in range(start, stop, step)

Important:
- start is included
- stop is not included
- step means jump size

Examples:
- range(5) -> 0, 1, 2, 3, 4
- range(1, 6) -> 1, 2, 3, 4, 5
- range(2, 11, 2) -> 2, 4, 6, 8, 10

## 3) while loop

A while loop repeats as long as a condition is True.

Example idea:
- Keep asking password until it is correct
- Count down from 5 to 1

Important:
- You must update something inside the loop (like count -= 1)
- If condition never becomes False, you get an infinite loop

## 4) break and continue

break:
- Stops the loop immediately

continue:
- Skips current iteration and moves to next iteration

## 5) Common beginner mistakes

1. Wrong indentation:
Python depends on indentation to know what belongs inside loop.

2. Off-by-one with range:
Remember stop value is not included.

3. Infinite while loop:
Forgetting to update loop variable.

4. Using = instead of == in conditions:
- = means assign
- == means compare

## 6) Practice checklist

After solving Day 4 exercises, check if you can do these:

1. Print 1 to 20 using one loop
2. Print odd numbers from 1 to 19
3. Print table of 7
4. Countdown 10 to 1
5. Ask password until correct

## 7) Real life analogy

Think of a loop like an alarm snooze:
- while you are still sleepy, snooze repeats
- when condition changes (you wake up), snooze stops

That is exactly how while loops work.
