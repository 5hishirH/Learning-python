# Python Program to print all prime numbers in an interval

def is_prime(n):
    i = 2
    while (i <= n // 2):
        if n%i == 0:
            return False
        i += 1
    return False if n <= 1 else True

def prime_interval(l, u):
    prime = []
    while(l <= u):
        if is_prime(l):
            prime.append(l)
        l += 1
    return prime

# driver code
print("[Enter range]")
lower_point = int(input("From : "))
upper_point = int(input("To : "))
list = prime_interval(lower_point, upper_point)
if len(list) == 0:
    print("\nThere is no prime number in this range.")
else:
    print("\nPrime numbers in this range are :", list)
