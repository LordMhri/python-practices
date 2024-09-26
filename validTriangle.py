def triangleNumber(nums: list[int]) -> int:
    #dont have to start at the front sometimes
    #look at it from the back
    nums.sort()
    ans = 0
    for i in range(len(nums) - 1, - 1 , - 1):
        left = 0
        right = i - 1
        while left < right:
            #nums[i] is the biggest number we have, because we sorted the list and are starting from the end
            if nums[left] + nums[right] > nums[i]:
                #if nums[left] + nums[right] > nums[i] then all numbers between right and left satisfy
                #requirements of a valid triangle
                ans += (right - left)
                right -= 1
            else:
                #if not then increase left 
                left += 1 
    return ans

'''
nums = [2,2,3,4], starting from the back 4 is nums[i] 
now 2 + 3 which are nums[left] and nums[right] is greater than 4
so between 2(the first one) and 3 all are valid triangles
so 2 - 0 = 2 now ans is 2 and then we move right to the left 
[2,2,3] by one so now we have nums[right] = 3 and check if 2 + 3 is greater than 4 yes it is
so move right to the left by 1 then we have nums[right] = 2 and
2 + 2 is not bigger than 4, moving left by one to the right causes right == left and 
we move out of the loop and continue the same thing for the other num[i] members 
'''

nums = [2,2,3,4]
print(triangleNumber(nums))