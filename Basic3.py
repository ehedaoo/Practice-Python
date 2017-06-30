# Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

radius = int(input("Enter the radius of the circle: "))
area1 = math.pi * pow(radius, 2)
print(area1)
area2 = math.pi * radius**2
print(area2)