"""
Write a recursive function, reverse, that accepts a parameter containing a
string value and returns the original string in reverse. For example, calling
reverse('goodbye') would return 'eybdoog'.

Reversing a string involves:
No action if the string is empty or only has 1 character
Concatenating the last character with the result of reversing the string
consisting of the second through next-to-last character, followed by the first
character
"""

def reverse(str):
    if len(str) <= 1:
        return str
