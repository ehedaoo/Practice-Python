# Write a Python program to add two objects if both objects are an integer type.

def value():
    obj1 = input("Enter an object: ")
    try:
        return type(int(obj1))
    except ValueError:
        return type(obj1)

print(value())

# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b
#
#
# print(add_numbers("test", 20))