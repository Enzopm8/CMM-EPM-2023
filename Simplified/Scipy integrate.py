from scipy import integrate
import numpy as np

def integrate_function(func, a, b, decimal_places=4):
    """
    Perform definite integration of a given function.

    Parameters:
    - func: The function to be integrated.
    - a: Lower limit of integration.
    - b: Upper limit of integration.
    - decimal_places: Number of decimal places to round the result (default is 4).

    Returns:
    - result: The definite integral of the function over the specified interval.
    """
    result, _ = integrate.quad(func, a, b)
    result = round(result, decimal_places)
    return result

# Example usage:
# Define the function to be integrated
def custom_function(x):
    return np.sin(x) * np.cos(3.89 * x)

# Specify the integration limits
lower_limit = 0
upper_limit = np.pi

# Call the function to perform integration
integration_result = integrate_function(custom_function, lower_limit, upper_limit)

# Display the result
print(f"Definite Integral from {lower_limit} to {upper_limit}: {integration_result}")

