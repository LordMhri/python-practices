def sortedSquares(nums:list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    
    nums = [i*i for i in nums] 
    #squaring the elements from the get go
    #could also compare the absolute value of each and then square at the end
    
    #merge sort
    left = 0
    right = len(nums) - 1
    idx = right
    while left <= right:
        l = nums[left]
        r = nums[right]
        if nums[left] >= nums[right]:
            ans[idx] = nums[left]
            left += 1
        else:
            ans[idx] = nums[right]
            right -= 1
        idx -= 1 
    
    
    return ans 
    
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))