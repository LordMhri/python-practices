def gaussian_elimination(A,b):
    n = len(A)

    '''
    Given a linear equation, 
    2x + 3y + z = 1
    4x + y + 2z = 2
    3x + 2y + 3z = 3,
    The A variable represents the coefficient matrix
    [2,  3,  1]
    [4,  1,  2]
    [3,  2,  3]
    The b variable represents,
    [1,
    2,
    3]
    '''

    #this creates the augumented matrix
    for i in range(n):
        A[i].append(b[i])

    '''
    The above line of code appends the b matrix to the A matrix creating
    [2,  3,  1, 1]
    [4,  1,  2, 2]
    [3,  2,  3, 3]
    '''
    

    for i in range(n):
        #normalization
        pivot = A[i][i]
        for j in range(i, n+1):
            A[i][j] /= pivot  

        # Eliminate elements below the pivot
        for k in range(i+1, n):  # Rows below the pivot
            factor = A[k][i] 
            for j in range(i, n+1):  # Iterate through columns
                A[k][j] -= factor * A[i][j]  # Row reduction


    ''' 
        The above lines of code first normalize each row meaning each element in a row
        is divided by the pivot element which is the diagonal element
        so for the first row we have [1 , 1.5 , .5 , .5] because the pivot element is 2

        then the second inner loop starts row reducing by starting from each element below our current
        row meaning for the i = 0 iteration we have after we're done with the first inner loop
        [1 , 1.5 , .5 , .5]
        [4,  1,    2,    2]
        [3 , 2,    3,    3]

        now K starts from i+1 so we have k = 1 
        (indexing starts from 0 in python so r2 means k=1 in this context)
        which refers to the second row
        and we perfrom the r2 = r2 - 'factor' * r1 operation
        our factor element is 4 so performing r2= r2-factor*r1 for the second row
        we have [0,-5,0,0]
        and performing r3 = r3-factor*r1 for the third row 
        we have [0,-2.5,1.5,1.5]

        all of the above operation is just for the i=0 iteration

        for the i = 1 iteration we first normalize our row so
        normalizing the 2nd row (indexing starts from 0 so i= 0 means 1st row...)
        we have [0,1,0,0]

        going into the second loop we have the r3 = r3-factor*(r2) operation
        so the third row becomes [0,0,1.5,1.5]

        and after normalization it becomes [0,0,1,1]

        putting it all together we have the upper triangular matrix
        [1, 1.5, 0.5 , 0.5]
        [0, 1,   0,    0  ]
        [0, 0,   1,  1]

    '''
    
    x = [0 for _ in range(n)]
    for i in range(n-1,-1,-1):#the loop starts from the bottom because we have an upper triangular matrix
        x[i] = A[i][n] #this is the constant term of the augumented matrix
        answer = x[i]
        for j in range(i+1,n): #loop through columns to subtract contributions 
            x[i] -= A[i][j] * x[j] #subtract the contributions

    '''
    The above line of code first allocates space for the answer matrix
    so x is first equal to 
    [0,0,0]
    
    so starting from the bottom we go upwards
                        [0,0,0]
                             |
                             v
    x[i] = A[i][n] means -> x[2] = A[i][n]
                            x[2] = 1
    and the inner loop doesn't execute becomes it starts from i + 1 -> 2+1 -> 3
    it starts from 3 and tries to goes up until n which is 3

    so for i = 2 , the second loop doesn't execute
    for i = 1, the loop first assigns x[1] = 0.0 as the answer and j = 3 becuase j = i+1
    then the inner loop decreases A[i][j] * x[j] from x[1]
    a[i][j] and x[j] are both zero so this doesn't have any effect on x[1]

    by the time the loop finishes 

    x is [0,0,1]
    
    
    '''
    
    return x

A = [
    [2,3,1],
    [4,1,2],
    [3,2,3]
]

b = [1,2,3]

solution = gaussian_elimination(A,b)
print("Solution, ",solution)