def finder(array1, array2):
    if len(array1) > len(array2):
        base = array1.sort()
        corrupt = array2.sort()
    else:
        base = array2.sort()
        corrupt = array1.sort()

    d = dict()

    for num in corrupt:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    for num in base:
        if num not in d:
            return num


print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
