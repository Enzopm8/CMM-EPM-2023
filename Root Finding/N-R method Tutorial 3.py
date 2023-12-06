# Recommendation:
# This code is designed for finding roots of equations using the Newton-Raphson and Secant methods with error control.
# It is recommended for well-behaved functions where convergence is assured and for cases where the derivative
# of the function is challenging or computationally expensive to obtain.

# Not recommended:
# These methods may not converge for functions with multiple roots, and the convergence can be slow for certain functions.
# Additionally, they are not suitable for functions with sharp turns or near-vertical slopes where the derivative is close to zero.

# How to modify for a different function:
# 1. Define the new function f(x): Replace the lambda function for 'f' with the one corresponding to the new function.
# 2. Define the new derivative df(x): Replace the lambda function for 'df' with the derivative of the new function.
#    If the derivative is not readily available, an approximate derivative or other numerical methods can be used.
# 3. Adjust the initial guess ('x0' and 'x1'): Set appropriate initial values based on the characteristics of the new function.
# 4. Modify the tolerance level and maximum number of iterations: Adjust 'tolerance' and 'max_iterations' based on the desired level of accuracy and computational resources.


import math

def newton_raphson_with_error_control(f, df, x0, tolerance, max_iterations):
    x = x0
    iteration = 0
    while abs(f(x)) > tolerance and iteration < max_iterations:
        x = x - f(x) / df(x)
        iteration += 1
    if iteration >= max_iterations:
        return None
    return x, iteration

def secant_with_error_control(f, x0, x1, tolerance, max_iterations):
    x_prev = x0
    x_current = x1
    iteration = 0
    while abs(f(x_current)) > tolerance and iteration < max_iterations:
        x_next = x_current - f(x_current) * (x_current - x_prev) / (f(x_current) - f(x_prev))
        x_prev = x_current
        x_current = x_next
        iteration += 1
    if iteration >= max_iterations:
        return None
    return x_current, iteration

# Define the function f(x) and its derivative df(x)
f = lambda x: x**2 + 4*x - 12
df = lambda x: 2*x + 4

# Set the tolerance level and maximum number of iterations
tolerance = 1e-6
max_iterations = 100

# Initial guess for Newton-Raphson and Secant methods
x0 = 1.0
x1 = 2.0

# Find the root using the Newton-Raphson method with error control
newton_root, newton_iterations = newton_raphson_with_error_control(f, df, x0, tolerance, max_iterations)
if newton_root is not None:
    print("Newton-Raphson method root:", newton_root)
    print("Number of iterations:", newton_iterations)
else:
    print("Newton-Raphson method did not converge within the specified tolerance or iterations.")

# Find the root using the Secant method with error control
secant_root, secant_iterations = secant_with_error_control(f, x0, x1, tolerance, max_iterations)
if secant_root is not None:
    print("Secant method root:", secant_root)
    print("Number of iterations:", secant_iterations)
else:
    print("Secant method did not converge within the specified tolerance or iterations.")
