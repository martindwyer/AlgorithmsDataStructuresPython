"""
Given non-negative integers x and n, x to the nth power can be defined as:

x to the 0th power is 1
x to the nth power can be obtained by multiplying x to the (n-1)th power with x

Write a function named power that accepts two parameters containing integer
values (x and n, in that order) and recursively calculates and returns the
value of x to the nth power.
"""

def power(x,n):
	if n==0:
		return 1
	else:
		return x*power(x,n-1)