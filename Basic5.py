# Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.

numbers = input("Enter your list of number using commas: ")
newlist = numbers.split(',')
print(newlist)
print(tuple(newlist))