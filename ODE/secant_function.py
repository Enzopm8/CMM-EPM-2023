# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# Comment: Secant Method for root finding
# Recommended Usage: Suitable for finding roots of a function when the derivative is not easily available.
# Not Recommended: Not ideal for functions with sharp turns or if the initial guess is far from the root.
def secant_2(f, a, b, iterations):
    """
    Parameters:
    f (function): The target function for root finding.
    a (float): Initial guess 1.
    b (float): Initial guess 2.
    iterations (int): Number of iterations.

    Returns:
    float: Approximation of the root.
    """
    for i in range(iterations):
        c = a - f(a)*(b - a)/(f(b) - f(a))
        if abs(f(c)) < 1e-13:
            return c
        a = b
        b = c
    return c
# ------------------------------------------------------
# Example usage
def example_function(x):
    return x**2 - 81

# Initial guesses
initial_guess_1 = 1.0
initial_guess_2 = 10.0

# Number of iterations
num_iterations = 10

# Applying the secant method
root_approximation = secant_2(example_function, initial_guess_1, initial_guess_2, num_iterations)

# Output
print("Approximated root:", root_approximation)
