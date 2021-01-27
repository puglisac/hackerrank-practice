"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

    >>> chaotic_queue([2,1,5,3,4])
    3
    >>> chaotic_queue([2,5,1,3,4])
    Too chaotic
    >>> chaotic_queue([1,2,5,3,7,8,6,4])
    7
    >>> chaotic_queue([1,2,5,3,4,7,8,6])
    4
"""


def chaotic_queue(arr):
    bribes_count = 0
    for k in range(0,3):
        for j in range(len(arr)-1,0,-1):
            if(arr[j]<arr[j-1]):
                if(k==2):
                    print("Too chaotic")
                    return
                tmp = arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=tmp
                bribes_count+=1
    print(bribes_count)
