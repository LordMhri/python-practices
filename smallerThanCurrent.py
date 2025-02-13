def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    count = [0] * (max(nums) + 1)

    for i in range(len(nums)):
        count[nums[i]] += 1
    

    #cumulative count

    cumulative = [0] * len(count)
    for i in range(1, len(count)):
        cumulative[i] = cumulative[i - 1] + count[i - 1]
    
    ans = [0] * len(nums)
    for i in range(len(nums)):
        ans[i] = cumulative[nums[i]]
    
    return ans



print(smallerNumbersThanCurrent([8,1,1,2,3]))