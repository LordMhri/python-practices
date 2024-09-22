def trap(height:list[int]) -> int:
    #two loops one for finding the right and left max for a specified index
    #find left max
    leftMaxElements = [0]
    leftMax = 0
    rightMaxElements = [0]
    rightMax = 0
    for i in range(1,len(height)):
        currMax = height[i-1]
        leftMax = max(currMax,leftMax)
        leftMaxElements.append(leftMax)
        
    #start from the second most right element and go to the start
    for i in range(len(height)-2,-1,-1): 
        currMax = height[i+1]
        rightMax = max(currMax,rightMax)
        rightMaxElements.append(rightMax)
    rightMaxElements.reverse()
    

    #loop for calculation of trapped water
    ans = 0
    for i in range(len(height)):
        #the bound is the minimum of the left and right bounds
        bound = min(leftMaxElements[i],rightMaxElements[i])
        #if the bound - current height is < 0 we've encountered a peak
        #else it is a valley so we can calculate how much it would hold
        if bound - height[i] >= 0:
            ans += bound-height[i]
            
    return ans
height = [0,1,0,2,1,0,1,3,2,1,2,1]    
print(trap(height=height))  
    

'''
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
'''