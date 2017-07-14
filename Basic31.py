# Write a Python program to get the least common multiple (LCM) of two positive integers.

numerouno = int(input("Enter the first integer: "))
numerodeux = int(input("Enter the second integer: "))

# maximum number between n1 and n2 is stored in minMultiple

if numerouno > numerodeux:
    minMultiple = numerouno
else:
    minMultiple = numerodeux

# Always true

while True:
    if(minMultiple % numerouno == 0) and (minMultiple % numerodeux ==0):
        input("The LCM of " + str(numerouno) + " and " + str(numerodeux) + " is " + str(minMultiple))
        break

    ++minMultiple;