# Adaptive Simpson's Rule for Numerical Integration

def adaptive_simpson(f, a, b, tol):
    """
    Evaluates the integral of f(x) on [a,b] using adaptive Simpson's rule.

    Parameters:
        f (function): The function to integrate.
        a, b (float): Left and right endpoints of the interval of integration.
        tol (float): Desired upper bound on allowable error.

    Returns:
        float: The value of the integral.

    Notes:
        Integrates the function f(x) on [a, b] with adaptive Simpson's rule,
        providing an error bound given by tol. The function is recursive and
        may recompute function values inefficiently for educational clarity.

        Suitable Use Cases:
        - When the function is not highly oscillatory or has discontinuities.
        - For functions with rapidly changing curvature.
        
        Not Suitable Use Cases:
        - For functions with severe oscillations or singularities.
        - When highly efficient integration is required (more efficient methods exist).

    """
    # Theory says the factor to multiply the tolerance by should be 15, but
    # since that assumes that the fourth derivative of f is fairly constant,
    # we want to be a bit more conservative...
    tol_factor = 10

    # Calculate the interval subdivisions
    h = 0.5 * (b - a)
    x0 = a
    x1 = a + 0.5 * h
    x2 = a + h
    x3 = a + 1.5 * h
    x4 = b

    # Evaluate the function at each point
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f4 = f(x4)

    # Compute Simpson's rule approximations
    s0 = h * (f0 + 4.0 * f2 + f4) / 3.0
    s1 = h * (f0 + 4.0 * f1 + 2.0 * f2 + 4.0 * f3 + f4) / 6.0

    # Check if further subdivision is needed
    if abs(s0 - s1) >= tol_factor * tol:
        s = adaptive_simpson(f, x0, x2, 0.5 * tol) + \
            adaptive_simpson(f, x2, x4, 0.5 * tol)
    else:
        # Use Richardson extrapolation for final result
        s = s1 + (s1 - s0) / 15.0

    return s

import numpy as np

# Test function
def f(x):
    return np.exp(-x**2)

# Example usage
result = adaptive_simpson(f, 0, 10, 1e-6)
print(f"The numerical integration result is: {result}")
