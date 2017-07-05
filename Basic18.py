# Write a Python program to get a new string from a given string
# where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

text1 = input("Enter a string: ")
text = text1.lower().split()
textlist = list(text)
textlist1 = list()
for x in text:
    if textlist[0] == 'is':
        print(text1)
        break
    elif x == 'is':                   #### previous: textlist.index('is') > 0 [Checks the first occurrence of is]
        textlist1.insert(0, "is")
        # textlist.insert(0, textlist.pop(textlist.index('is')))
        # str1 = ' '.join(textlist)    ## This code finds the first occurrence of the keyword and pushes it
        # break                        ## in front
    else:
        textlist1.append(x)
str1 = ' '.join(textlist1)
print(str1)
