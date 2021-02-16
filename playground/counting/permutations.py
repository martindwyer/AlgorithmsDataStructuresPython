
from playground.counting.factorial import *

# ways to arrange items from a set of size n into k slots
# duplicate combinations are ignored

def permutations(n,k):
    return factorial(n) / factorial(n-k)

#  in a 13 card deck of spades, how many ways can you deal six cards to
#  your opponent?

print(permutations(13,6))
