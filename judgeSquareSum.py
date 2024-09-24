import math

def judgeSquareSum(c:int)-> bool:
    bound = int(math.sqrt(c))
    nums = [i for i in range(0,bound)] 
    right = len(nums) -1 
    left = 0
    if c == 4: 
        return True
    while left <= right:
        if nums[left] ** 2 + nums[right] ** 2  < c:
            left += 1
        elif nums[left] ** 2 + nums[right] ** 2 > c:
            right -= 1
        else:
            return True
    
    return False

print(judgeSquareSum(4))