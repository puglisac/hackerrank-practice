"""
Function Description

Complete the rotateLeft function in the editor below.

rotateLeft has the following parameters:

int d: the amount to rotate by
int arr[n]: the array to rotate
Returns

int[n]: the rotated array
>>> rotate_left([1,2,3,4,5], 3)
[4, 5, 1, 2, 3]
"""


def rotate_left(arr, n):
    #return the array rotated left n times
    if(n==0):
        return arr
    i=1
    while(i <= n):
        first = arr.pop(0)
        arr.append(first)
        i+=1
    return arr
