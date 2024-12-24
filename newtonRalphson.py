def f(x):
    # Example function: x^2 - 2
    return x**2 - 2

'''
f(x) is a sample function given to check the newton-raphson method.
It has a root at sqrt(2) (~1.414213).
'''

def derivative(f, x, h=1e-5):
    '''
    Since we don't know the derivative of any function that could be given to us,
    we use the limit definition of a derivative with a step size h = 10^-5.
    '''
    return (f(x + h) - f(x)) / h

def newton_raphson(f, x0, tol=1e-7, max_iter=1000):
    '''
    x0 is the initial guess
    '''
    x = x0
    for i in range(max_iter):
        fx = f(x)
        '''
        **First Iteration:**
        Starting with x0 = 1:
        fx = f(1) = 1^2 - 2 = -1
        dfx = f'(1) = (f(1 + h) - f(1)) / h
            = ((1.00001)^2 - 2 - (-1)) / 0.00001
            ≈ 2 (numerical approximation)

        Update x:
        x = 1 - (-1 / 2) = 1 + 0.5 = 1.5

        **Second Iteration:**
        Now x = 1.5:
        fx = f(1.5) = 1.5^2 - 2 = 2.25 - 2 = 0.25
        dfx = f'(1.5) = (f(1.50001) - f(1.5)) / h
            = ((1.50001)^2 - 2 - 0.25) / 0.00001
            ≈ 3.00001 (numerical approximation)

        Update x:
        x = 1.5 - (0.25 / 3.00001) ≈ 1.5 - 0.08333 = 1.41667

        **Third Iteration:**
        Now x = 1.41667:
        fx = f(1.41667) = (1.41667)^2 - 2 ≈ 2.006944 - 2 = 0.006944
        dfx = f'(1.41667) = (f(1.41668) - f(1.41667)) / h
            = ((1.41668)^2 - 2 - 0.006944) / 0.00001
            ≈ 2.83334 (numerical approximation)

        Update x:
        x = 1.41667 - (0.006944 / 2.83334) ≈ 1.41667 - 0.00245 = 1.41422
        '''

        if abs(fx) < tol:
            print(f"Root found: {x}")
            return x  # Stop if the value of f(x) is close enough to 0

        dfx = derivative(f, x)
        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None  # Cannot proceed if the derivative is zero

        x = x - fx / dfx

    print("Maximum iterations reached. No solution found.")
    return None  # If no solution is found within max_iter iterations

# Example usage:
initial_guess = 1
root = newton_raphson(f, initial_guess)

'''
Expected root for x^2 - 2 is approximately sqrt(2) (~1.414213).
'''
