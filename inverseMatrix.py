def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
'''
    Given the matrix and the position of the current number that is the i and j
    matrix[:i] means all all elements before the ith element
    matrix[i+1:] means all elements after the ith element the One is added because indexing starts from 0
    row[:j] and row[j+1:] does the same thing above but for the row
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    for the i=0 and j=0 case we ignore the entire row 1,2,3 and the entire column 1,4,7
    so we have [5,6]
               [8,9]
'''



def get_matrix_determinant(matrix):
    # for the 2 by 2 matrix 
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * get_matrix_determinant(get_matrix_minor(matrix, 0, c))
    return determinant

'''
    This is used to check if the matrix's determinant is zero 
    if it is zero then the inverse for this matrix doesn't exist


    This funcion has a recursive call where the base case is len(matrix) == 2
    get_matrix_determinant(A) where A = [1,2,3]
                                        [4,5,6]   
                                        [7,8,9]
    len(matrix) == 3 at first so it doesnt reach the base case
    it goes into the for loop
    for the first case -> c = 0
    determinant = -1**0 * matrix[0][0], this is the (-1)^(i+j) part
    when the get_matrix_determinant function is called again 
    it is called after calling the get_matrix_minor function
    which takes the 3by3 matrix and returns a 2 by 2 matrix 
    which means we've hit the base case in the get_matrix_determinant() function
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    so now matrix[0][0] = 5 
           matrix[0][1] = 6
           matrix[1][0] = 8
           matrix[1][1] = 9
    we apply matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] onto it

    determinant = -1^(i+j) * Aij * minor(matrix,i,j) -> this is what the normal procedure is 
    but for this function we're only checking the first row where i=0 and j changes
    so determinant = -1^(c) * A0c * minor(matrix,c,0) is sufficient 
    '''

def transpose_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for j in range(len(matrix)):
            transposed_row.append(matrix[j][i])
        transposed.append(transposed_row)
    return transposed

'''
    This function returns the transposed version of a given matrix
    transposition is exchanging the i and j values across the diagonal
    '''

def get_matrix_inverse(matrix):
    determinant = get_matrix_determinant(matrix)
    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")

    # Special case for 2x2 matrix
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]
    '''
    This the [[a,b],
              [c,d]] case the determinant is
                [ad-bc,-1(bc-ad)]
                [-1(cb-ad),ad-bc]
    '''

    # Find matrix of cofactors
    cofactors = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            minor = get_matrix_minor(matrix, r, c)
            cofactor_row.append(((-1) ** (r + c)) * get_matrix_determinant(minor))
        cofactors.append(cofactor_row)

    '''
    The above loop builds the cofactor matrix, since we're given a sqaure matrix
    the number of rows is len(matrix) and the number of columns is also len(matrix)
    each row has len(matrix) amount of columns

    for each element the get_matrix_minor is called to get the minor element
    then on the cofactor row we assign that value
     (-1) ** (r + c)) * get_matrix_determinant(minor)

     example = [1,2,3]
                [4,5,6]
                [7,8,9]]
    and r = 0 and c = 0
    we first find the minor of that particular number
    minor(matrix,0,0) -> [[5,6]
                         [8,9]] 
    the determinant is 45-48 -> - 3
    now -1 ^(r+c) = 1 so 1*-3 = -3
    now the cofactor matrix looks like
    [[-3,  ,  ]
    [,  ,  ]
    [,  ,  ]]
    and this will continue to update the cofactor matrix in a similar manner

    '''


    cofactors = transpose_matrix(cofactors) #this transposes the matrix

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    
    '''
        This is the final operation where we divide every element of the transposed cofactor matrix
        with the determinant
    '''
    return cofactors

# Example usage:
matrix = [[4, 7,1], [2, 6,5],[1,2,4]]
inverse = get_matrix_inverse(matrix)
print("Inverse of the matrix is:")
for row in inverse:
    print(row)