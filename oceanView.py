def oceanView(heights):
    n = len(heights)
    stack = []
    ans = []
    for i in range(n-1,-1,-1):
        if not stack or stack[-1] < heights[i]:
            ans.append(i)  
            stack.append(heights[i])
    
    return sorted(ans)

print(oceanView([4,3,2,1]))