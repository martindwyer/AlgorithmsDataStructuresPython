# -*- coding: utf-8 -*-
'''
Introduction to Big O Notation

Goal:  How will runtime grow as input grows
'''

'''
A simple algorithm for computing the sum of 0 to n
Version 1:

Number of assignments => n + 1 times (from 'for' loop)
                         final_sum is reassigned over and over
Technically this is O(n+1) but the constant is dropped so
this algorithm is O(n)
'''
def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

print(sum1(10))


'''
But this does function solves the same problem using Gauss's Trick

Number of assignements => 1 
This algorithm is O(1)
Version 2
'''
def sum2(n):
    return (n*(n+1))/2

print(sum2(10))






