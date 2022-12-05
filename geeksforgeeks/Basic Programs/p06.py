# Python program to check armstrong number

def order(x):
    n = 0
    while(x != 0):
        n += 1
        x //= 10
    
    return n

def is_armstrong(n):
    temp = n
    sum = 0
    p = order(n)    # can be done by : p = len(str(n))
    while(temp != 0):
        sum += (temp%10)**p
        temp //= 10

    return (n == sum)

# driver code
num = int(input("Enter a number : "))

if is_armstrong(num):
    print(num, "is an armstrong number.")
else:
    print(num, "is not an armstrong.")