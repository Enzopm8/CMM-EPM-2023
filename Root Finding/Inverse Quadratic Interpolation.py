# Recommendation:
# This code is designed for finding roots of equations using Inverse Quadratic Interpolation method.
# It is recommended for functions where convergence is assured and the root is expected to be found within a reasonable number of iterations.

# Not recommended:
# The Inverse Quadratic Interpolation method may not converge for functions with multiple roots, and it might not be as efficient for well-behaved functions with simple roots.
# Additionally, it may not work well for functions with sharp turns or near-vertical slopes.

# How to modify for a different function:
# 1. Define the new function f(x): Replace the existing function 'f' with the one corresponding to the new function.
# 2. Adjust the initial guesses ('x0', 'x1', 'x2'): Set appropriate initial values based on the characteristics of the new function.
# 3. Modify the maximum number of iterations and tolerance: Adjust 'max_iter' and 'tolerance' based on the desired level of accuracy and computational resources.

def inverse_quadratic_interpolation(f, x0, x1, x2, max_iter=20000000, tolerance=1e-5):
    steps_taken = 0
    while steps_taken < max_iter and abs(x1 - x0) > tolerance:  # last guess and new guess are very close
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
        new = L0 + L1 + L2
        x0, x1, x2 = new, x0, x1
        steps_taken += 1
    return x0, steps_taken

# Define the function f(x)
f = lambda x: x**3 + 2*x**2 + 4*x + 5

# Set the initial guesses
x0, x1, x2 = 4.3, 4.4, 4.5

# Find the root using Inverse Quadratic Interpolation
root, steps = inverse_quadratic_interpolation(f, x0, x1, x2)
print("Root is:", root)
print("Steps taken:", steps)
