"""
Function Description

Complete the function reverseArray in the editor below.

reverseArray has the following parameter(s):

int A[n]: the array to reverse
Returns

int[n]: the reversed array

>>> reverse_array([1, 2, 3])
[3, 2, 1]

"""

def reverse_array(arr):
    reversed=[]
    for i in range(0,len(arr)):
        reversed.append(arr.pop())
    return reversed

