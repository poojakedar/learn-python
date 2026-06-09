"""Day 4 exercises.

Instructions:
1) Complete each TODO using for/while loops.
2) Save final work as solutions/day04_solution.py
"""

print("=== Day 4 Exercises ===")

# TODO 1: Print numbers 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

# TODO 2: Print all even numbers from 2 to 20.
for i in range(2, 21, 2):
    print("Even:", i)

# TODO 3: Ask for a number and print its multiplication table (1 to 10).
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# TODO 4: Use a while loop to print countdown from 5 to 1.
count = 5
while count >= 1:
    print("Countdown:", count)
    count -= 1

# TODO 5: Ask for a password until user enters "python123".
password = ""
while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Wrong password, try again.")

print("Access granted")
print("\nGreat work! Save this as solutions/day04_solution.py")
