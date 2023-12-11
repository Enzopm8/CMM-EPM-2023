#                           Optimize to find Max and Min

from scipy.optimize import minimize
import numpy as np

def find_optimum(objective_function, initial_guess, find_maximum=True, bounds=None, method='Nelder-Mead', tolerance=1e-6):
    """
    Find the optimum (maximum or minimum) of an objective function within a specified range.

    Parameters:
    - objective_function: The function to optimize.
    - initial_guess: Initial guess for the optimization.
    - find_maximum: If True, find the maximum; if False, find the minimum.
    - bounds: A tuple (lower, upper) specifying the range for optimization.
    - method: Optimization method (default is 'Nelder-Mead').
    - tolerance: Tolerance for convergence (default is 1e-6).

    Returns:
    - optimum_x: x value where the optimum occurs.
    - optimum_y: Optimum y value.
    """

    # Define the objective function to be minimized or maximized
    def negated_objective(x):
        return -objective_function(x) if find_maximum else objective_function(x)

    # Define bounds explicitly
    if bounds is not None:
        bounds = [(bounds[0], bounds[1])]

    # Use minimize to find the optimum with bounds and tolerance
    result = minimize(negated_objective, initial_guess, bounds=bounds, method=method, tol=tolerance)

    # Extract the optimal x value (where the optimum occurs)
    optimum_x = result.x[0]

    # Calculate the optimum y value (negation based on whether it's a max or min)
    optimum_y = -result.fun if find_maximum else result.fun

    # Check if the optimization was successful
    if not result.success:
        raise RuntimeError(f"Optimization failed: {result.message}")

    return optimum_x, optimum_y
# Example usage:

# Define your objective function
def custom_function(x):
    return 0.01*(x**4) + 10*(x**2) + x - 10

# Initial guess
initial_guess = 0.0

# Specify the optimization bounds
lower_bound = -1.0
upper_bound = 3.0
bounds = (lower_bound, upper_bound)

# Set the tolerance
custom_tolerance = 1e-8

# Find the maximum within the specified range with custom tolerance
maximum_x, maximum_y = find_optimum(custom_function, initial_guess, find_maximum=True, bounds=bounds, tolerance=custom_tolerance)

# Find the minimum within the specified range with custom tolerance
minimum_x, minimum_y = find_optimum(custom_function, initial_guess, find_maximum=False, bounds=bounds, tolerance=custom_tolerance)

# Display the results
print(f"Maximum within the specified range at x = {maximum_x:.6f}, y = {maximum_y:.6f}")
print(f"Minimum within the specified range at x = {minimum_x:.6f}, y = {minimum_y:.6f}")
