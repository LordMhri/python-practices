def teamForming(nums:list[int])->int:
    ans = 0
    nums.sort()
    for i in range(1,len(nums),2):
        ans += nums[i] - nums[i-1]
    
    return ans


n = 6
nums = [1,100]

print(teamForming(nums))