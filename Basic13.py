# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

yy1 = int(input("Enter the first year: ").replace(" ", ""))
yy2 = int(input("Enter the second year: ").replace(" ", ""))
mm1 = int(input("Enter the first month: ").replace(" ", ""))
mm2 = int(input("Enter the second month: ").replace(" ", ""))
dd1 = int(input("Enter the first date: ").replace(" ", ""))
dd2 = int(input("Enter the second date: ").replace(" ", ""))
d0 = date(yy1, mm1, dd1)
d1 = date(yy2, mm2, dd2)

difference = d0 - d1
print(difference.days + "days")