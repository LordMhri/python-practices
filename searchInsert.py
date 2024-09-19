def searchInsert(nums:list[int],target:int)-> int:
    i = 0
    j = len(nums) - 1   
    while i<=j:
        mid = (i+j) // 2
        if target > mid:
            i = mid + 1
        else:
            j = mid - 1
        
    return i