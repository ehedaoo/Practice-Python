# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("Enter digit one: "))
num2 = int(input("Enter digit two: "))
num3 = int(input("Enter digit three: "))

if (num1 == num2) or (num1 == num3) or (num2 == num3):
    print("Sum = 0" )
else:
    print(num1 + num2 + num3)