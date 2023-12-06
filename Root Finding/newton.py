# Recommendation:
# This code is designed for finding roots of equations using Newton's method.
# It is recommended for well-behaved functions where convergence is assured and for cases where the derivative
# of the function is readily available.

# Not recommended:
# Newton's method may not converge for functions with multiple roots, and the convergence can be slow for certain functions.
# Additionally, it is not suitable for functions with sharp turns or near-vertical slopes where the derivative is close to zero.

# How to modify for a different function:
# 1. Define the new function f(x): Replace the lambda function for 'f' with the one corresponding to the new function.
# 2. Define the new derivative Df(x): Replace the lambda function for 'Df' with the derivative of the new function.
#    If the derivative is not readily available, an approximate derivative or other numerical methods can be used.
# 3. Adjust the initial guess ('x0'): Set an appropriate initial value based on the characteristics of the new function.
# 4. Modify the tolerance level and maximum number of iterations: Adjust 'epsilon' and 'max_iter' based on the desired level of accuracy and computational resources.

def newton(f, Df, x0, epsilon, max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f, Df, 1, 1e-8, 10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

# Define the function f(x) and its derivative Df(x)
f = lambda x: x**2 - x - 1
Df = lambda x: 2*x - 1

# Set the tolerance level and maximum number of iterations
epsilon = 0.0000001
max_iter = 10

# Initial guess for Newton's method
x0 = 1

# Find the root using Newton's method
solution = newton(f, Df, x0, epsilon, max_iter)
print(solution)
