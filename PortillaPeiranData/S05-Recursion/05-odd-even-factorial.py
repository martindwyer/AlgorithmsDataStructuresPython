"""
The "odd/even factorial" of a positive integer n is represented as n and is
defined non-recursively as: (n)(n-2)(n-4)...(4)(2) if n is even and
(n)(n-2)(n-4)...(5)(3)(1) if n is odd. For example, the odd factorial of 7
equals 7*5*3*1 or 105, and the even factorial of 6 equals 6*4*2 or 48.

Come up with a recursive definition for the odd/even factorials and use it to
write a function called oddevenfact that recursively calcules that odd/even
factorial value of its single parameter, which contains an integer value.
"""

def oddevenfact(n):
	if n > 2:
		return n*oddevenfact(n-2)
	else:
		return n