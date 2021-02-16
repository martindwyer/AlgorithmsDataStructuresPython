import pytest

def pair_sum(int_array,sum_target):
    answer_set = set()

    if len(int_array) < 2:
        return answer_set

    for num in int_array:
        needed = sum_target - num
        if needed in int_array:
            if needed != num:
                answer_set.add((min(num,needed),max(num,needed)))
            elif int_array.count(num) > 1:
                answer_set.add((min(num, needed), max(num, needed)))


    return answer_set

answer = pair_sum([1,3,2,2,7,6,4,9],10)

for pair in answer:
    print(pair)
