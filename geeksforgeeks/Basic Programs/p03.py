# A python program for factorial of a number

def factorial(n):
    fact = 1
    while (n > 1):
        fact*= n
        n-= 1
    
    return fact

num = int(input("Enter a number : "))
print(str(num) + "! =", factorial(num))

# can be done : 
# import math
# math.factorial(num)
