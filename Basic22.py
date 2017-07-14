# Write a Python program to get the n (non-negative integer)
# copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

stringtest = list(input("Enter a string: "))
number = int(input("Enter the no. of copies: "))
# stringlist = list(stringtest)
if len(stringtest) > 2:
    print(stringtest[:2])
else:
    for x in range(number):
        print(''.join(stringtest))