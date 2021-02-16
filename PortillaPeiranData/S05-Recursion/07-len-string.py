"""
Write a recursive function, len, that accepts a parameter that holds a string
value, and returns the number of characters in the string.

The length of the string is:
0 if the string is empy ("")

1 more than the length of the string beyond the first character
"""

def len(aString):
    if aString == "":
        return 0
    else:
        return 1 + len(aString[1:])