#                                       Tutorial 3
#------------------------------------------------------------------------------
#Ex1: Applying the bisection code
import numpy as np
# Bisection method with error control
def bisection_with_error_control(f, a, b, tolerance):
    # Check if a and b bound a root
    if f(a) * f(b) >= 0:
        print("Initial values 'a' and 'b' must have opposite signs.")
        return None
    
    iteration = 0
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    # The root is approximately in the middle of the interval [a, b]
    root = (a + b) / 2
    return root, iteration

# Define the function f(x)
f = lambda x: np.sin(x) * np.exp(x ** (0.1))

# Set the tolerance level
tolerance = 1e-6

# Find the root using the bisection method with error control
root, iterations = bisection_with_error_control(f, -10, 100, tolerance)
if root is not None:
    print("Bisection method root:", root)
    print("Number of iterations:", iterations)
else:
    print("Root not found within the specified tolerance.")
#------------------------------------------------------------------------------
#Ex2: Applying the bisection code, different function

# Define the function f(x)
f = lambda x: x**2 + 4*x - 12

# Set the tolerance level
tolerance = 1e-6

# Find the root using the bisection method with error control
root, iterations = bisection_with_error_control(f, 0, 10, tolerance)
if root is not None:
    print("Bisection method root Part 2:", root)
    print("Number of iterations:", iterations)
else:
    print("Root not found within the specified tolerance.")

from scipy.optimize import fsolve
Scipy_sol = fsolve(f,2)
print ('Using Scipy:', Scipy_sol)
