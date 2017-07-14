# Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.

num1 = int(input("ENter num 1: "))
num2 = int(input("Enter num 2: "))
result = num1+num2

if result < 15 or result > 20:
    print(result)
elif 15 <= result <= 20:
    print("20")