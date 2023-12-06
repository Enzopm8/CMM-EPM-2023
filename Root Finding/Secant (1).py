# Recommendation:
# This code is designed for finding approximate solutions of equations using the Secant method.
# It is recommended for cases where the Newton-Raphson method may not be applicable or if the derivative
# of the function is challenging or computationally expensive to obtain.

# Not recommended:
# The secant method may not converge for functions with multiple roots, and the convergence can be slow for certain functions.
# Additionally, it is not suitable for functions with sharp turns or near-vertical slopes where the derivative is close to zero.

import math

def secant(f, a, b, N):
    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    m_N : number
        The x intercept of the secant line on the the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iterations, the secant method fails and returns None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f, 1, 2, 5)
    1.6180257510729614
    '''
    if f(a) * f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    
    for n in range(1, N + 1):
        m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
        f_m_n = f(m_n)
        
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None

    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))

# Define the function f(x) CHANGE
f = lambda x: x**2 - x - 1

# Find and print the solution using the Secant method CHANGE
solution = secant(f, 1, 2, 5)
print(solution)
