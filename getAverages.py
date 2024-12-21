def getAverages( nums: list[int], k: int) -> list[int]:
    if k == 0:
        return nums
    n = len(nums)
    if k > n:
        return [-1]
    
    ans = [-1] * n
    currSum = 0
    for i in range(n):
        currSum += nums[i]
        if i-k >= k:    
            ans[i-k] = currSum//(n-k+1)
            currSum -= nums[i-k]

    return ans 

nums = [7,4,3,9,1,8,5,2,6]
k = 3

print(getAverages(nums,k))