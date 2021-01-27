"""
You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
"""

def minimum_swaps(arr):
    swap_count=0
    curr_val=None
    for i in range(0,len(arr)):
        while arr[i] == i+1:
            if(i>=len(arr)-1):
                break
            i+=1
        curr_val=arr[i]
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[j-1] and arr[j]!=j+1):
                arr[i]=arr[j]
                arr[j]=curr_val
                swap_count+=1
                break
    return swap_count           

print(minimum_swaps([2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19
]))


