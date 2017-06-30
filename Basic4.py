# Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.

name = input("Enter your name please: ")
if len(name) > 0:
    print(name[::-1])