# Recommendation:
# The code uses the root_scalar function from SciPy to find the root of a given function within a specified bracket.
# SciPy provides robust numerical methods for root finding, and the bisect method is suitable for well-behaved functions.

# Not recommended:
# For functions with more complex behavior, consider exploring other root-finding methods provided by SciPy.

# How to modify for a different function or bracket:
# 1. Define a new function 'f(x)' based on the equation you want to solve.
# 2. Adjust the bracket in the 'root_scalar' function to set the range in which you want to search for a solution.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

# Define the function f(x)
f = lambda x: np.sin(x) * np.exp(x ** 0.1)

# Plot the function to visualize its behavior
x_values = np.linspace(0.1, 10, 1000)
plt.plot(x_values, f(x_values))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# Find the root using the root_scalar function with a refined interval
result = root_scalar(f, bracket=[2, 4], method='bisect')
if result.converged:
    approx_root = result.root
    print("Approximate root:", approx_root)
else:
    print("Root not found within the specified bracket.")
