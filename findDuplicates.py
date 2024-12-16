'''
Given an integer array nums of length n where all the 
integers of nums are in the range [1, n] and each integer appears at most twice
, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time 
and uses only constant auxiliary space, excluding the space needed to store the output.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]'

1,2,3,4,3,2,7,8 



Output: [2,3]

'''

def findDuplicates(nums:list[int]) -> list[int]:
    ans = []
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[correct] != nums[i]:
            nums[correct],nums[i] = nums[i],nums[correct]
        else:
            i += 1
    
    for i in range(len(nums)):
        if i+1 != nums[i]:
            ans.append(nums[i])
    
    return ans


    