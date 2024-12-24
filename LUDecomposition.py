def lu_decomposition(A):
    n  = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    '''
    L and U are the answers so we're allocating space for them
    since we're only dealing with square matrices
    given a square matrix of length 3
    L now equals = [[0.0],[0.0],[0.0],
                    [0.0],[0.0],[0.0],
                    [0.0],[0.0],[0,0]] 
    the same goes for U
    '''

    for i in range(n):
        #upper triangular matrix
        for k in range(i,n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - sum
        '''
    This nested loop calculates the elements 
    of the upper triangular matrix ( U ). 
    For each element ( U[i][k] ), it subtracts the 
    sum of the products of the corresponding elements of 
    ( L ) and ( U ) from the element ( A[i][k] ).'''

        for k in range(i,n):
            if i == k:
                L[i][i] = 1 #diagonal is one
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
            L[k][i] = (A[k][i] - sum ) / U[i][i]

        '''
        This nested loop calculates the elements of the lower triangular matrix ( L ). 
        For the diagonal elements, it sets ( L[i][i] ) to 1. 
        For the off-diagonal elements, it subtracts 
        the sum of the products of the corresponding elements of ( L ) and ( U ) 
        from the element ( A[k][i] ) and then divides by ( U[i][i] ).
        
        '''
    return L,U

A = [[2, -1, -2],
     [-4, 6, 3],
     [-4, -2, 8]]
L,U = lu_decomposition(A)
print("L:")
for row in L:
    print(row)
print("U:")
for row in U:
    print(row)