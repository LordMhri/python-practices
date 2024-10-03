def maximumAverageSubArray(nums:list[int], k:int) -> float:
    if(len(nums) == 1):
        return nums[0]
        

    maxSum = sum(nums[:k])
    currentSum = maxSum
    
    for i in range(len(nums) - k):
        currentSum -= nums[i]
        currentSum += nums[i+k]
        maxSum = max(currentSum,maxSum)
    
    return maxSum/k