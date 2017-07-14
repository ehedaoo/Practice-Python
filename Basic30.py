# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

import math

numerouno = int(input("Enter the first integer: "))
numerodeux = int(input("Enter the second integer: "))
result = math.gcd(numerouno, numerodeux)
print(result)