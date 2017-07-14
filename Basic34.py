# Write a Python program that will return true
# if the two given integer values are equal or their sum or difference is 5.

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
sumis = num1 + num2
diffis = abs(num1 - num2)

if num1 == num2 or sumis == 5 or diffis == 5:
    print("True")
else:
    print("False")