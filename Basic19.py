# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

stringy = input("Enter a string: ")
numero = int(input("Enter the no. of copies: "))
for x in range(numero):
    if numero > 0:
        print(stringy)
else:
    print("Not cool")