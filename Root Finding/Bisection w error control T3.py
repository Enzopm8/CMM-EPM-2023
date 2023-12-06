# Recommendation:
# The code implements the Bisection method for solving equations with error control. Bisection is a reliable method
# for finding roots within a specified interval. The added error control enhances the accuracy of the result.

# Not recommended:
# Bisection method may not be the most efficient choice for all functions, especially those with rapid changes.
# Consider trying other methods depending on the characteristics of the function.

# How to modify for a different function or interval:
# 1. Define a new function 'f(x)' based on the equation you want to solve.
# 2. Adjust the initial interval '[a, b]' to set the range in which you want to search for a solution.
# 3. Set the tolerance level 'tolerance' based on the desired accuracy.

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
f = lambda x: x**2 + 4*x - 12

# Set the tolerance level
tolerance = 1e-6

# Find the root using the bisection method with error control
#for cuadratics a and b have to be non-negative
root, iterations = bisection_with_error_control(f, 0, 5, tolerance)
if root is not None:
    print("Bisection method root:", root)
    print("Number of iterations:", iterations)
else:
    print("Root not found within the specified tolerance.")
