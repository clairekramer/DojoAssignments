# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

def findChar(list,char):
    new = []
    for each in list:
        if char in each:
            new.append(each)
        else:
            continue
    print new

findChar(['hello','world','my','name','is','Anna'],'o')
