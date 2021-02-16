"""
The nth harmonic number is defined non-recursively as: 1+1/2+1/3+1/4+...+1/n.
Come up with a recursive definition and use it to write a function called
harmonic that accepts a parameter n that contains an integer value and returns
the nth harmonic number.
"""

def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1.0/n + harmonic(n-1)

