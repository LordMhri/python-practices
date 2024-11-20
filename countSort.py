
#this is a non comparison sort
#mainly used for small range comparison

def countSort(nums:list[int]) -> list[int]:
    arr = [0] * (max(nums) + 1)

    #first pass count the occurence of the numbers

    for num in nums:
        arr[num] += 1
    
    target = 0
    for index,value in enumerate(arr):
        for i in range(value):
            nums[target] = index
            target += 1
    
    return nums

print(countSort([1,4,2,5,3,2,1,7]))
