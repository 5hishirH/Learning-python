# A python program to find 
# the smallest among three numbers.

num1 = float(input("Enter num1 : "))
num2 = float(input("Enter num2 : "))
num3 = float(input("Enter num3 : "))

min = num1
if num2 < min:
    min = num2
if num3 < min:
    min = num3

print(min, "is the smallest.")