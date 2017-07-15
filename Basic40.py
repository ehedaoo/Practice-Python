# Write a Python program to check whether a file exists.

import os

path = input("Enter the file name: ")
filename = os.path.isfile(path)
if filename:
    print("Exists")
else:
    print("Doesn't exist")