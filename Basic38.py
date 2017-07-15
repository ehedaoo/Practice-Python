# Write a Python program to compute the future value of a
# specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

principal_amount = int(input("Enter PA: "))
roi = float(input("Enter rate of interest: "))
noy = float(input("Enter the number of years: "))
si = round(principal_amount * (1 + roi*noy), 2)
ci = round(principal_amount * ((1 + roi)**noy), 2)
print("Simple interest: " + str(si))
print("Compounded interest: " + str(ci))
