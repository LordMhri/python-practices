def rotate(matrix: list[list[int]]) -> None:

    
    '''
    given matrix = [[1,2,3],
                    [4,5,6],
                    [7,8,9]] , after modification [7,4,1],
                                                  [8,5,2],
                                                  [9,6,3]]
     transposedMatrix = [[1,4,7],
                         [2,5,8],
                         [3,6,9]]
                         
    horizontalSwap = [7,4,1],
                     [8,5,2],
                     [9,6,3]] exchange (0,0) with (0,2) or whatever is the end instead of 2
                     and we dont have to worry about the middle one 
                     
                     (0,0) , (0,2) = (0,2) , (0,0)
                     (1,0) , (1,2) = (1,2) , (1,0)
                      
    '''
    #transpose
    n = len(matrix)
    for i in range(len(matrix[0])):
        for j in range(i+1,n):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
    
    #horizontal swap 
    for i in range(n): #iterates over the whole thing
        #horizontal swap so only need half of matrix
        #swap this side of the matrix with the horizontally parallel side  
        for j in range(n // 2): 
            matrix[i][j] , matrix[i][n-j-1] = matrix[i][n-j-1] , matrix[i][j]
            
            
            
    
    
    
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]