from scipy.optimize import linprog

def minimize_linear_function(c, A_ub, b_ub, bounds=None, method='highs'):
    """
    Minimize a linear objective function subject to linear inequality constraints.

    Parameters:
    - c: Coefficients of the linear objective function to be minimized.
    - A_ub: Coefficients of the inequality constraints (left-hand side).
    - b_ub: Constants on the right-hand side of the inequality constraints.
    - bounds: Bounds for variables (default is None).
    - method: Optimization method (default is 'highs').

    Returns:
    - result: The result object containing the solution.
    """
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method=method)

    # Check if the optimization was successful
    if not result.success:
        raise RuntimeError(f"Optimization failed: {result.message}")

    print("\nLinear Programming Problem:")
    print("===========================")
    print("Objective Function Coefficients:", c)
    print("Linear Inequality Constraints (Ax <= b):")
    for i, row in enumerate(A_ub):
        print(f"   Constraint {i + 1}: {row} <= {b_ub[i]}")
    if bounds:
        print("Variable Bounds:")
        for i, (lower, upper) in enumerate(bounds):
            print(f"   x{i + 1}: {lower} <= x{i + 1} <= {upper}")

    print("\nOptimization Results:")
    print("=====================")
    print("Status:", result.message)
    print("Optimal Values of Variables:")
    for i, value in enumerate(result.x, 1):
        print(f"   x{i}: {value:.4f}")
    print("Optimal Value of the Objective Function:", -result.fun)

    return result

# Example usage:
# if you have more coefficients just increase the numbers in all the follwing lists

# Define the coefficients of the objective function to minimize
c = [-1, 2]

# Define the coefficients of the inequality constraints (left-hand side)
A_ub = [[1, 1], [-1, 2], [0, -1]]

# Define the constants on the right-hand side of the inequality constraints
b_ub = [4, 2, -1]

# Specify variable bounds (optional)
bounds = [(0, None), (0, None)]

# Call the function to perform linear optimization
result = minimize_linear_function(c, A_ub, b_ub, bounds=bounds)

# Display the result
