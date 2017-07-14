# Write a Python program to concatenate all elements in a list into a string and return it.

element = list(input("Enter values in the list separated by commas: ").split(","))
# print(element)
newlist = ''.join(element)
print(newlist)