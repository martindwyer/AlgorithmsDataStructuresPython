"""
Write a function called fact that recursively calculates the factorial value of
its parameter, which is an integer value.
"""

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

