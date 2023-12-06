# Recommended Use:
# This code is suitable for numerically integrating a given function using Simpson's rule.
# Adjust the 'f' function for your specific integration requirements.

# Not Recommended Use:
# Avoid using this code for functions with singularities or highly oscillatory behavior.
# Ensure that the 'f' function is well-behaved within the specified integration limits.

import numpy as np

def simps(f, a, b, N=50):
    """
    Numerical integration using Simpson's rule.

    Parameters:
    f (function): The function to be integrated.
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    N (int): Number of intervals (must be an even integer).

    Returns:
    float: Result of the numerical integration.
    """
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    S = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S

# Example usage
f = lambda x: np.exp(x**-2)
numerical_integration_result = simps(f, 1, 2, 24)
print(f"The numerical integration result is: {numerical_integration_result:.6f}")
