# Python program to find area of a circle
import math

def area_circle(r):
    return math.pi*r*r

radius = float(input("Enter the radius of a circle : "))
area = area_circle(radius)
print("Area of the circle is", area)