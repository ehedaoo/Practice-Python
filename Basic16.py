# Write a Python program to test whether a number is within 100 of 1000 or 2000.

number = int(input("Enter a number between 1000-2000: "))
if number in range(1000, 2001):
    if number % 100 == 0:
        print("In range")
    else:
        print("Not in range")
else:
    print("Enter number between given range")