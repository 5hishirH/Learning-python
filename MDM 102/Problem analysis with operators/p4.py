# A python program to calculate the area of a triangle using three sides

import math

print("Enter the sides of the triangle: ")
side1 = float(input())
side2 = float(input())
side3 = float(input())

half_parameter = (side1 + side2 + side3)/2
area = math.sqrt(half_parameter*(half_parameter - side1)*(half_parameter - side2)*(half_parameter - side3))

print("The area is", area)