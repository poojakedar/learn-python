def greet_user(name):
    print("Hello", name)
greet_user("Pooja")

def square(n):
    return n * n


print("Square of 6:", square(6))

def max_of_two(a, b):
    if a > b:
        return a
    return b

print("Max of 10 and 25:", max_of_two(10, 25))

def check_pass(mark):
    if mark >= 35:
        return "Pass"
    return "Fail"


print("Result for 72:", check_pass(72))
print("Result for 20:", check_pass(20))
