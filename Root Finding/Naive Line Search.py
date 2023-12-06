# Recommendation:
# This code is designed for finding roots of equations using a naive root-finding approach.
# It is recommended for simple functions where a brute-force approach is acceptable and the solution is expected to be found within a reasonable number of iterations.

# Not recommended:
# This method is not suitable for functions with multiple roots, and the convergence can be slow for certain functions.
# Additionally, it may not work well for functions with sharp turns or near-vertical slopes.

# How to modify for a different function:
# 1. Define the new function f(x): Replace the lambda function for 'f' with the one corresponding to the new function.
# 2. Adjust the initial guess ('x_guess'): Set an appropriate initial value based on the characteristics of the new function.
# 3. Modify the tolerance level and step size: Adjust 'tolerance' and 'step_size' based on the desired level of accuracy and computational resources.

def naive_root(f, x_guess, tolerance, step_size):
    steps_taken = 0
    
    while abs(f(x_guess)) > tolerance:
        if f(x_guess) > 0:
            x_guess -= step_size
        elif f(x_guess) < 0:
            x_guess += step_size
        else:
            return x_guess
        
        steps_taken += 1
    
    return x_guess, steps_taken

# Define the function f(x)
f = lambda x: x**2 - 20

# Set the initial guess, tolerance level, and step size
x_guess = 4.5
tolerance = 0.01
step_size = 0.001

# Find the root using the naive root-finding approach
root, steps = naive_root(f, x_guess, tolerance, step_size)
print("Root is:", root)
print("Steps taken:", steps)
