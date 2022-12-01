# A python program for factorial of a number

def factorial(num):
    i = 1
    fact = 1
    while i <= num:
        fact*= i
        i+= 1
    
    return fact

number = int(input("Enter a number : "))
print(str(number) + "! =", factorial(number))
