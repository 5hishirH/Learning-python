# A python program for factorial of a number

def factorial(n):
    return 1 if ( n == 0 or n == 1) else n*factorial(n-1)

num = int(input("Enter a number : "))
print(str(num) + "! =", factorial(num))