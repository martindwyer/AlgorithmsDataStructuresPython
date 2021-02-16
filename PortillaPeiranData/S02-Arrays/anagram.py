import pytest

def anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = dict()
    # initiate set with set()

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False

    for k in count:
        if count[k] != 0:
            return False
        else:
            return True

print(anagram('god','dog'))
print(anagram('clint eastwood','old west action'))
print(anagram('public relations','crap built on lies'))
print(anagram('public relations','crap built on lies##'))



