"""Day 4: for and while loops."""

print("=== Day 4: Loops ===")

print("\nFor loop with range(5):")
for i in range(5):
    print("i =", i)

print("\nFor loop through a list:")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)

print("\nWhile loop example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\nBreak example:")
for n in range(1, 10):
    if n == 5:
        print("Stopping at", n)
        break
    print(n)

print("\nContinue example:")
for n in range(1, 6):
    if n == 3:
        continue
    print(n)

print("\nDone! Now open exercises/day04_exercises.py")
