"""
Polynomial Long Division

This code performs polynomial long division by iterating through the coefficients.
It takes an array 'A' containing coefficients of p(x) and a value 't' and outputs
the coefficients of the quotient q(x) and the residual r.

When to use this code:
- Use this code when you want to perform polynomial long division using the iterative method.
- Suitable for polynomials where long division is applicable.

When not to use this code:
- Avoid using this code for non-polynomial functions or in cases where long division is not the appropriate method.

Steps to modify for different polynomials:
1. Define your polynomial coefficients in the 'A' array.
2. Set the value of 't' for the division.
3. Run the code and observe the output coefficients of the quotient q(x) and the residual r.

"""

import numpy as np

def poly_iter(A, t):
    # Function to perform polynomial long division by iterating
    # The function takes an array 'A' containing coefficients of p(x) and a value 't'
    
    # Get the degree of the polynomial (n)
    n = len(A) - 1
    # Array 'q' to store coefficients of q(x) (quotient)
    q = np.zeros(n, dtype=np.int8)
    # Initialize the residual 'r'
    r = A[n]

    # Iterate through the coefficients to perform polynomial long division
    for a in reversed(range(n)):
        s = A[a]
        q[a] = r // t**(n - a - 1)
        r = s + r * t

    # Output the coefficients of the quotient q(x) and the residual r
    print('----------------------------------------')
    print('Quotient q(x):')
    for i, coef in enumerate(q):
        print(f'a{len(q) - i - 1}: {coef}', end='  ')
    print('\n----------------------------------------')
    print(f'Residual r: {r}')
    print('----------------------------------------')
    
    # Return an empty list (currently, the function returns an empty list)
    return []

# Example usage of the function with polynomial coefficients 'A' and a value 't'

#A is the coefficients of the polynomial in order (left to right)
A = np.array([-42, 0, -12, 1])

#t is the polynomia you want to divide by, e.g t= 3 == (x-2)
t = 3

poly_iter(A, t)
