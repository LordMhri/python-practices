def gauss_jacobi(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    x = [0] * n
    x_new = x[:]
    
    '''
    n is the length of the given matrix, x is the initial guess for the solution
    x_new is a copy of x that is used to store the updated values in each iteration

    tolerance is the level of error that we're allowed to have in the calculations,
    it is given as an argument that could be changed but if not specified it continues as 1^(-10)

    max_iterations is the number of maximum times the loop executes , this is required so that we have a 
    stop condition in our loop and it doesn't run forever,
    during the loop if the answer doesn't go to the tolerance level then that means it doesn't converge
    so we print the error
    '''


    for iteration in range(max_iterations):
        for i in range(n):
            sum_Ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_Ax) / A[i][i]
        
        '''
        the above nested loop is just the code version of the jacobi method
        where the new x values are calculated like 
            x = (bi - SumAX)/ (A[i][i])
        the sum function in sum_Ax is the same as the sigma notation in the maths version
        so sum_Ax = summation of (A[i][j] * x[j] for j in range(n) if j!=i)
        x[j] is the intial guess we have for the first try and for all subsequent loops 
        it is the previous value we have meaning x represents xi(k) in the maths version
        x_new[i] represents the xi(k+1) answer 

        '''
        
        converged = True
        for i in range(n):
            if abs(x_new[i] - x[i]) >= tolerance:
                converged = False
                break
        if converged:
            return x_new
        '''
        we start with assuming that we've reached convergence -> convergence = True
        
        as we itearate through the answer matrices we have x_new and x
        if we find out that the difference between our current and previous answer is greater or equal to tolerance 
        then we haven't reached convergence so we change convergence to False
        and break out of our loop, the loop may end prematurely meaning we dont go through all elements if we find
        one that breaks our convergence then we stop but if we don't find anything that is bigger than our tolerance level
        that means we have reached a suitable answer

        so the if converged:
                return x_new 
            condition returns our answer
        
        '''
        

        
        x = x_new[:]

        '''
        x = x_new[:] means when we finish the loop if the answer we have is not satisfactory
        we update our x with the values we just finished getting,
        this is in preparation of our next loop
        when we use x again in our next loop, we're using an updated version of it


        '''
    
    raise Exception("Solution did not converge")
    '''
    If we dont reach convergence then we will reach the above line of code
    so we raise an exception which says Solution did not converge
    '''


# Example usage:
A = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
b = [4, 7, 3]
solution = gauss_jacobi(A, b)
print("Solution:", solution)