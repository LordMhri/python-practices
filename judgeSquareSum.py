import math

def judgeSquareSum(c:int)-> bool:
    bound = int(math.sqrt(c))
    right = bound 
    left = 0
    
    while left <= right:
        leftSquared =left ** 2
        rightSquared = right ** 2
        if leftSquared + rightSquared  < c:
            left += 1
        elif leftSquared + rightSquared > c:
            right -= 1
        else:
            return True
    
    return False

print(judgeSquareSum(4))