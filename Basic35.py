# Write a Python program to add two objects if both objects are an integer type.


def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a + b

obj1 = int(input("Enter an integer 1: "))
obj2 = int(input("Enter an integer 2: "))
print(add_numbers(obj1, obj2))



# import ast
#
# def value():
#     obj1 = input()
#     try:
#         return isinstance(ast.literal_eval(obj1), int)
#     except ValueError:
#         return ast.literal_eval(obj1)
#
# print(value())
