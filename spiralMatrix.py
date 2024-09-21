def spiralMatrix(matrix:list[list[int]]) -> list[int]:
    ans = [] #answer array
    n = len(matrix)  #refers to rows
    m = len(matrix[0]) #refers to cols
    left = 0 # pointer for left side of the array
    top = 0 # pointer for the top side of the array
    right = m - 1 # pointer for the right side of the array
    bottom = n - 1
    direction = 0 #direction of traversal 1 for bottom right,2 for bottom left, 3 for top left
    while len(ans) < n * m:
        if direction == 0:  # Traverse from left to right along the top row
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            direction = 1
        elif direction == 1:  #traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            direction = 2
        elif direction == 2:   #traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            direction = 3
        elif direction == 3:   #traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):  
                ans.append(matrix[i][left])
            left += 1
            direction = 0  
            
    
    return ans


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralMatrix(matrix))
                
            
    