# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

n = input("enter your builtin function: ")
exec("print({}.__doc__)".format(n))
