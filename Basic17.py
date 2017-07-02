# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.


def calsum(numlist):
    if len(set(numlist)) == 1:
        print("Sum = " + str(sum((numlist)) * 3))
    else:
        print("Sum = " + str(sum(numlist)))

    
number = (input("Enter 3 numbers separated by commas: ").split(", "))
numlist = list(map(int, number))

