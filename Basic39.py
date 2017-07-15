# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math


x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))
distance = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
print(distance)