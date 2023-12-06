# This code implements the rectangle rule for numerical integration.
# It is recommended for functions that are relatively smooth over the interval [a, b].
# Avoid using it for functions with rapidly changing behavior, as it may lead to less accurate results.
# Ensure to choose an appropriate number of subintervals (n) based on the characteristics of the function.

import numpy as np

def calculate_dx(a, b, n):
    """
    Calculate the width of each subinterval.

    Parameters:
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    n (int): Number of subintervals.

    Returns:
    float: Width of each subinterval.
    """
    return (b - a) / float(n)

def rect_rule(f, a, b, n):
    """
    Apply the rectangle rule for numerical integration.

    Parameters:
    f (function): The integrand function.
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    n (int): Number of subintervals.

    Returns:
    float: Approximation of the definite integral using the rectangle rule.
    """
    total = 0.0
    dx = calculate_dx(a, b, n)

    for k in range(0, n):
        total = total + f((a + (k * dx)))

    return dx * total

def f(x):
    """
    Define the integrand function.

    Parameters:
    x (float): Variable of integration.

    Returns:
    float: Value of the integrand function at x.
    """
    return np.exp(-x**2)

# Example usage:
result = rect_rule(f, 0, 1, 1000)
print(f"The numerical approximation of the definite integral is: {result:.6f}")





