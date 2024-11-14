def minSubArrayLen(target: int, nums: list[int]) -> int:
        left = 0
        sm = nums[left]
        right =  0
        ans = float('inf')
        while right < len(nums):
            if sm < target:
                right += 1
                if right < len(nums):
                    sm += nums[right]    
            else:
                ans = min(ans,right - left + 1)
                sm -= nums[left]
                left += 1
                
    
        return ans if ans != float('inf') else 0

target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(target,nums))