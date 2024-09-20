def findClosestNumber(nums: list[int]) -> int:
    
        ans = nums[0]
        for i in range(len(nums)):
            #if current distance is less than previous distance , set ans to curr distance
            if abs(nums[i]) < abs(ans): 
                ans = nums[i] 
            elif abs(ans) == abs(nums[i]): #if there is another one with the same distance 
                if nums[i] > ans: #check if the current one is bigger , if so
                    ans = nums[i] #set ans to that one 
        
        return ans