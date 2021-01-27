
"""
>>> hourglass_sum ([[1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]])
7
>>> hourglass_sum([ [-1,1,0,-9,-2,-2],[-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-4,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]])
-4
"""

def hourglass_sum(arr):
    #return the largest hourglass sum from a 6X6 array
    row = 1
    max_sum=None
    while(row <= 4):
        col = 1
        while(col<=4):
            arr_sum=[]
            arr_sum.extend([arr[row-1][col-1], 
                            arr[row-1][col], 
                            arr[row-1][col+1], 
                            arr[row+1][col-1], 
                            arr[row+1][col], 
                            arr[row+1][col+1]])
            arr_sum.append(arr[row][col])
            if (max_sum==None or sum(arr_sum)>max_sum):
                max_sum=sum(arr_sum)
            col+=1
        row+=1
    return max_sum

