def maxSubArrayLen(nums, k):
    mapp = {0:-1}
    maxLen = 0
    prefix = 0
    for right in range(len(nums)):
        prefix += nums[right]
        if prefix - k in mapp:
            maxLen = max(right-mapp[prefix-k],maxLen)
        if prefix not in mapp:
            mapp[prefix] = right

    return maxLen

nums = [1, -1, 5, -2, 3]
k = 3
print(maxSubArrayLen(nums, k))