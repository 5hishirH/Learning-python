# Python program for sum of squares of first n natural number

def sum_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2

    return sum

# driver code
n = int(input("Enter n : "))
sum = sum_squares(n)
print("Sum =", sum)