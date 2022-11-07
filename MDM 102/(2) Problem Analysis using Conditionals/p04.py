# A python program to find
# the largest between two numbers.

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

if num1 > num2:
    print(num1, "is the largest")
elif num1 < num2:
    print(num2, "is the largest")
else:
    print(num1, "=", num2)