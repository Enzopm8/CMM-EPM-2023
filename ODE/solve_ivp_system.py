# Function: Solve a system of first-order ordinary differential equations using solve_ivp from SciPy
# Description:
# This script utilizes solve_ivp from the SciPy library to numerically solve a system of first-order ordinary differential equations (ODEs) defined in the function 'model'.
# Usage:
# - Suitable for solving systems of first-order ODEs.
# - Convenient for cases where an appropriate step size can be determined by the solver.
# - Provides an automated approach for solving ODEs and plotting the results.
# - Suitable for quick and efficient computation of ODE solutions.
# - Not recommended for scenarios requiring manual control over the step size or other specific solver parameters.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ------------------------------------------------------
# Function defining the system of first-order ODEs
# The equation is dy_j/dx = f_j(x, y_j) for j = [1, 2] in this case
def model(x, y):
    y_1, y_2 = y[0], y[1]
    f_1 = -0.5 * y_1
    f_2 = 4.0 - 0.3 * y_2 - 0.1 * y_1
    return [f_1, f_2]
# ------------------------------------------------------

# ------------------------------------------------------
# Initial conditions and parameters
initial_x = 0
initial_conditions = [4, 6]  # y_1 and y_2 initial values
final_x = 20
# Step size is determined automatically by the solver, not explicitly set here
# ------------------------------------------------------

# ------------------------------------------------------
# Apply solve_ivp method to solve the ODEs
solution = solve_ivp(model, [initial_x, final_x], initial_conditions)
# ------------------------------------------------------

# ------------------------------------------------------
# Print the results in an easy-to-understand format
print("X \t\t y_1 \t\t y_2")
for t, y1, y2 in zip(solution.t, solution.y[0], solution.y[1]):
    print(f"{t:.2f}\t\t {y1:.4f}\t {y2:.4f}")
# ------------------------------------------------------

# ------------------------------------------------------
# Plot the results
plt.plot(solution.t, solution.y[0, :], 'b.-', label='y_1')
plt.plot(solution.t, solution.y[1, :], 'r-', label='y_2')
plt.xlabel('x')
plt.ylabel('Values for y')
plt.legend()
plt.show()
# ------------------------------------------------------

# ------------------------------------------------------
'''
# Save the results in a text file for later use
file_name = 'output.dat'
f_io = open(file_name, 'w')
n_step = len(y.t)
for i in range(n_step):
    s1 = str(i)
    s2 = str(y.t[i])
    s3 = str(y.y[0, i])
    s4 = str(y.y[1, i])
    s_tot = s1 + ' ' + s2 + ' ' + s3 + ' ' + s4
    f_io.write(s_tot + '\n')
f_io.close()
'''
# ------------------------------------------------------