from playground.counting.factorial import *

# ways to arrange items from a set of size n into k slots
# duplicate combinations are ignored

def combinations(n,k):
    return factorial(n) / (factorial(k)*factorial(n-k))

#  in a 13 card deck of spades, how many ways can you deal six cards to
#  your opponent? DO NOT DOUBLE COUNT COMBINATIONS WHICH MAY BE DEALT IN
#  DIFFERENT ORDER

print(combinations(13,6))