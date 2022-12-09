# Python program to check whether a number is fibonacci or not

def is_fibonacci(n):
    a = 1
    b = 1
    while (b < n):
        c = a + b
        a = b
        b = c

    return ( b == n )

# driver code
num = int(input("Enter a number : "))
if is_fibonacci(num):
    print(num, "is a fibonacci number")
else:
    print(num, "is not a fibonacci number")