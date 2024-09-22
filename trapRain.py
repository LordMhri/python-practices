def trap(height:list[int]) -> int:
    #apparently you can calculate the left and right max on the fly
    #not intuitive
    ans = 0
    leftMax = 0
    rightMax = 0
    left = 0
    right = len(height) - 1
    
    while left <= right:
         #check on which boundary collected water depends on
        if height[left] < height[right]: #height at left is smaller therfore it depends on the left one
            leftMax = max(height[left],leftMax) #update leftMax with the max of the current one and the previous max
            ans += leftMax - height[left] #update answer with the difference between curr left max and curr element
            left += 1 #move left pointer forward
        else:
            rightMax = max(height[right],rightMax)
            ans += rightMax - height[right]
            right -= 1

            
    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]    
print(trap(height=height))  
    

'''
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
'''