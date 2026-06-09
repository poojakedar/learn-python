for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print("Even:", i)

num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
count = 5
while count >= 1:
    print("Countdown:", count)
    count -= 1
password = ""
while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Wrong password, try again.")

print("Access granted")
print("\nGreat work! Save this as solutions/day04_solution.py")
