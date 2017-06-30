# Write a Python program to print the calendar of a given month and year.

import calendar
import datetime


def printvalues(yy, mm):
    if yy in range(1000, 4999):
        if mm in range(1, 13):
            print(calendar.month(yy, mm))
            print("Current date: " + str(datetime.datetime.now()))
        else:
            print("Enter correct value!")
    else:
        print("Enter correct value!")


yy = int(input("Enter the year: "))
mm = int(input("Enter the month: "))
printvalues(yy, mm)

