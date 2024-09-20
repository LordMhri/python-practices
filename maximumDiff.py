def maximumDifference(nums: list[int]) -> int:
        ans = 0
        check = nums[0]
        for num in nums:
            if num < check:
                check = num
            else:
                ans = max(ans,num-check)
        
        if ans <= 0:
            return -1
        else:
            return ans