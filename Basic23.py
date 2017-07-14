# Write a Python program to test whether a passed letter is a vowel or not.

vowellist = ['a', 'e', 'i', 'o', 'u']
character = input("Enter a character: ")
for x in vowellist:
    if character == x:
            print("Vowel")
            break
else:
    print("Not")