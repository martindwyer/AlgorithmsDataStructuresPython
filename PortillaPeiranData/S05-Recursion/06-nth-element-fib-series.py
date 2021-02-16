"""
The Fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, 21) has as its first two values
0 and 1; each successive value is then calculated as the sum of the previous
two values. The first element in the series is considered the 0th element.

The nth element in the series, written as fib(n), is thus defined as:

n if n=0 or n=1
fib(n-1)+fib(n-2) otherwise

Write a function fib, that takes a single parameter, n, which contains
an integer value, and recursively calculates and returns the
nth element of the Fibonacci series.
"""

def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n-1) + fib(n-2)

print(fib(2))
print(fib(4))
print(fib(6))

