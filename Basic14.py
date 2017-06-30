# Write a Python program to get the volume of a sphere with radius 6.

import math


def volume(radius):
    pie = math.pi
    vol = round(pie*radius**3*(4/3), 2)
    print(vol)

radius = int(input("Enter radius: "))
volume(radius)