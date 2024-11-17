def bubbleSort(nums:list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1] , nums[j]
    
    return nums



print(bubbleSort([12,9,5,2,2,1,0,3,13]))