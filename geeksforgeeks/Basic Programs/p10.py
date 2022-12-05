# Python program for n-th fibonacci number

def nfibonacci(n):
    a = 1
    b = 1
    i = 3
    while (i <= n):
        c = a + b
        a = b
        b = c
        i += 1

    return b

# driver code
n = int(input("Enter a positive integer : "))
print(n, "th fibonacci number is", nfibonacci(n))