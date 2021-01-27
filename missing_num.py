"""
 Write a Python program to find a missing number from a list.
>>> print(is_missing_num([1,2,3,4,6,7,8]))
5
 """

def is_missing_num(num):
    return sum(range(num[0], num[-1]+1))-sum(num)

print(is_missing_num([1,2,3,4,6,7,8]))