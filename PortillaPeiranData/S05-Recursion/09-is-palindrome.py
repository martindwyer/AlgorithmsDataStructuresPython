"""
A palindrome is a word or phrase that reads the same forwards or backwards (e.g.
"dad", "mom", "deed"). Write a recrusive function, isPalindrome that accepts a
string and returns whether the string is a palindrome. A string is a palindrome
if:

it is an empty string or consists of a single letter, or if the first and last
characters are the same, and the rest of the string forms a palindrome
Your function should ignore spaces and only compare letters.
"""
def isPalindrome(aString):
	aString = aString.replace(" ","")
	if len(aString) <= 1:
		return True
	if aString[0] == aString[-1]:
		return isPalindrome(aString[1:-1])
	else:
		return False