def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    maxArea = -1 # initialized maxArea to -1 so that it gets update
    while left < right:
        # currentArea is the minimum of the two heights on our left and right ends
        # and the distance between right and left 
        currArea = min(height[left],height[right]) * (right - left) 
        #maxArea updates the maximum area we've found so far
        maxArea = max(currArea,maxArea)
        #if the left height is smaller then we know that the right one is good
        #so we move our left pointer right in hopes of finding a bigger one 
        if height[left] < height[right]:
            left += 1
        #the opposite of what was in our if clause
        else:
            right -= 1
    return maxArea