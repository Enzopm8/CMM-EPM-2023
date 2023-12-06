# Recommendation:
# This code is designed for solving systems of nonlinear equations using the Newton-Raphson method.
# It is suitable when a quick and accurate convergence to the solution is needed for well-behaved functions.

# Not recommended:
# This code may not be suitable for poorly conditioned or ill-posed problems, where the Jacobian matrix is close to singular.
# Additionally, for functions with multiple solutions, the initial guesses might lead to convergence to a local minimum or a divergent solution.

# How to modify for other functions:
# 1. Update the 'equations' function: Replace the equations with the ones corresponding to the new system.
# 2. Update the 'jacobian' function: Adjust the computation of the Jacobian matrix based on the partial derivatives of the new equations.
# 3. Adjust initial guesses ('x0' and 'y0'): Set appropriate initial values based on the characteristics of the new system.
# 4. Modify the convergence criteria: Adjust 'tolerance' and 'max_iterations' based on the desired level of accuracy and computational resources.


import numpy as np

# Define the system of equations
def equations(x, y):
    eq1 = x**2 + x*y - 10
    eq2 = y + 3*x*y**2 - 57
    return eq1, eq2

# Define the Jacobian matrix
def jacobian(x, y):
    J = np.zeros((2, 2))
    J[0, 0] = 2*x + y
    J[0, 1] = x
    J[1, 0] = 3*y**2
    J[1, 1] = 1 + 6*x*y
    return J

# Initial guesses
x0, y0 = 1.5, 3.5

# Tolerance and maximum number of iterations
tolerance = 0.01
max_iterations = 10

for i in range(max_iterations):
    # Evaluate the system of equations at the current point
    F = np.array(equations(x0, y0))
    
    # Evaluate the Jacobian matrix at the current point
    J = jacobian(x0, y0)
    
    # Solve for the update vector using the linear system: J * delta = -F
    delta = np.linalg.solve(J, -F)
    
    # Update the current point using the calculated delta
    x0 += delta[0]
    y0 += delta[1]
    
    # Calculate the relative error
    relative_error = np.linalg.norm(delta) / np.linalg.norm([x0, y0])
    
    # Check if the solution has converged based on the specified tolerance
    if relative_error < tolerance:
        break

# Output the final solution and relative error
print(f"Solution after convergence: x = {x0:.6f}, y = {y0:.6f}")
print(f"Relative error after 2 further steps: {relative_error:.6f}")
