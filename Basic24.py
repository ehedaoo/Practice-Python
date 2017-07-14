# Write a Python program to check whether a specified value is contained in a group of values.

listofvalues = list(input("Enter comma separated values: ").split(','))
number = input("Enter a number: ")
for x in listofvalues:
    if number == x:
            print("Hit")
            break
else:
    print("Not")