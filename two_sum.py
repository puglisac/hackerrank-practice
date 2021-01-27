def twoSum(nums, target):
    #find the indexes of 2 numbers in the array that add up to the target
    sorted_arr=nums[:]
    sorted_arr.sort()
    left = 0
    right = len(nums)-1
    while(left<right):
        if(sorted_arr[left]+sorted_arr[right]==target):
            if(nums.index(sorted_arr[left]) == nums.index(sorted_arr[right])):
                index_arr=[]
                for i in range(0, len(nums)):  
                   if(nums[i]==sorted_arr[left]):
                       index_arr.append(i)
                return index_arr
            return [nums.index(sorted_arr[left]), nums.index(sorted_arr[right])]
        elif(sorted_arr[left]+sorted_arr[right]>target):
            right-=1
        else:
            left+=1

print(twoSum([0,1,3,0], 0))