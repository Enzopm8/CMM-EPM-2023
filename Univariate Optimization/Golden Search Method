import numpy as np

def golden_section_maximize(function, x_left, x_mid, x_right, tolerance=1e-9):
    """
    Applies the golden-section algorithm to maximize the given function.

    Parameters:
    - function: The function to maximize.
    - x_left, x_mid, x_right: Initial bracketing values such that x_left < x_mid < x_right
                             and function(x_left), function(x_right) <= function(x_mid).
    - tolerance: Tolerance level for terminating the algorithm (default is 1e-9).

    Returns:
    The value of x that maximizes the function within the specified tolerance.

    Golden ratio plus one:
    golden_ratio_plus_one = 1 + (1 + np.sqrt(5)) / 2

    Successively refines x_left, x_right, and x_mid until the difference between x_right and x_left is less than or equal to tolerance.
    """
    golden_ratio_plus_one = 1 + (1 + np.sqrt(5)) / 2

    # Successively refine x_left, x_right, and x_mid
    f_left = function(x_left)
    f_right = function(x_right)
    f_mid = function(x_mid)

    while (x_right - x_left) > tolerance:
        if (x_right - x_mid) > (x_mid - x_left):
            new_x = x_mid + (x_right - x_mid) / golden_ratio_plus_one
            f_new = function(new_x)

            if f_new >= f_mid:
                x_left, f_left = x_mid, f_mid
                x_mid, f_mid = new_x, f_new
            else:
                x_right, f_right = new_x, f_new
        else:
            new_x = x_mid - (x_mid - x_left) / golden_ratio_plus_one
            f_new = function(new_x)

            if f_new >= f_mid:
                x_right, f_right = x_mid, f_mid
                x_mid, f_mid = new_x, f_new
            else:
                x_left, f_left = new_x, f_new

    return x_mid

# Initial values
x_left = 0
x_mid = 5
x_right = 10

# Define the function to maximize
def quadratic_function(x):
    return 2 * np.sin(x) - (x**2)/10

# Apply the golden section algorithm and print the result
optimal_x = golden_section_maximize(quadratic_function, x_left, x_mid, x_right, tolerance=1e-9)
optimal_value = quadratic_function(optimal_x)

print("Optimal x:", optimal_x)
print("Optimal function value:", optimal_value)
