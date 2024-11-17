def selectionSort(nums:list[int]) -> list[int]:
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx]  = nums[min_idx],nums[i]
    return nums


print(selectionSort([12, 9, 5, 2, 2, 1, 0, 3, 13]))