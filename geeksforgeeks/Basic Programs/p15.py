# Python program for sum of cubes of first n natural number

def sum_cube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3

    return sum

# driver code
n = int(input("Enter n : "))
sum = sum_cube(n)
print("Sum =", sum)