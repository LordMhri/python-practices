from collections import Counter

def minSubarray(nums,p):
    if sum(nums) % p == 0:
        return 0
    prefix = 0
    ans = float("inf")
    target = sum(nums) % p
    counter = Counter({0:-1})
    for right in range(len(nums)):
        prefix += nums[right]
        mod = prefix % p
        need = mod % p
        if need in counter:
            ans = min(ans,right - counter[need])
        counter[mod] = right
        
    
    return ans if ans < len(nums)  else -1
        

print(minSubarray([6,2],6))