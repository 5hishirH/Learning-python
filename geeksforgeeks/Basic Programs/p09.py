# Python program to check whether a number is prime or not

def is_prime(n):
    i = 2
    while (i <= n//2):
        if n%i == 0:
            return False
        i += 1
    return False if n == 1 else True

# driver code
num = int(input("Enter a number : "))
if is_prime(num):
    print(num, "is a prime")
else:
    print(num, "is not a prime")