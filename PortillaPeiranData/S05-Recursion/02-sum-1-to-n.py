
"""
The sum of the numbers 1 to n can be calculated recursively as follows:

The sum from 1 to 1 is 1.
The sum from 1 to n is n more than the sum from 1 to n-1

Write a function named sum that accepts a variable containing an integer value
as its parameter and returns the sum of the numbers from 1 to to the parameter
(calculated recursively).
"""

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)


print(sum(3))
print(sum(10))
print(sum(30))

"""
But by Gauss' formula we know this sum can be expressed as n(n+1)/2

So we should use the much more efficient calculation
"""

def gauss_sum(n):
    return int(n * (n + 1)/2)

print(gauss_sum(3))
print(gauss_sum(10))
print(gauss_sum(30))

