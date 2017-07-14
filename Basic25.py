# Write a Python program to create a histogram from a given list of integers.

import matplotlib.pyplot as plt

number = input("Enter a list of integers: ").split(',')
numlist = list(map(int, number))
plt.hist(numlist)
# plt.plot(number)
plt.show()