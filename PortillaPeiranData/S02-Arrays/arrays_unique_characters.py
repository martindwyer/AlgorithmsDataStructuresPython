def unique_characters(s):
    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True



print(unique_characters('abcde'))
print(unique_characters('abcdee'))
print(unique_characters('aabcdee'))