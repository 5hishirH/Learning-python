# A python program to find maximum among two numbers

num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number : "))

if num1 > num2:
    max = num1
elif num2 > num1:
    max = num2

print("Max =", max)