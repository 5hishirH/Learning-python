# A python program to ceil, round, and floor a floating-point number
import math

num = float(input("Enter a floating point number: "))
CEIL = math.ceil(num)
ROUND = round(num)
FLOOR = math.floor(num)

print("Ceil:", CEIL)
print("Round:", ROUND)
print("Floor:", FLOOR)