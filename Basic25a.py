# Write a Python program to create a histogram from a given list of integers using loop.

number = input("Enter a number: ").split(',')
numlist = list(map(int, number))
for x in numlist:
    print("*"*x)