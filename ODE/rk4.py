# Recommendation:
# This code is recommended for solving first-order ordinary differential equations (ODEs) of the form dy/dx = f(x, y).
# It is suitable for educational or demonstrative purposes, providing a clear example of the Fourth Order Runge-Kutta method.
# The code allows manual control over step size and iterations, making it useful for understanding the RK4 method.

# Caution:
# Not recommended for complex or varied ODEs where higher-order methods or specialized solvers might be more appropriate.
# The code assumes a simple ODE with a fixed coefficient, limiting its applicability to a specific class of problems.

# Comments on Code:
# - The model function defines the ODE (dy/dx = k * y) and can be modified for different equations.
# - Initial conditions, step size, and solution interval are customizable for different scenarios.
# - The RK4 method is implemented with clear steps, making it easy to understand and modify.

# Suggestions:
# - Ensure that the provided ODE matches the form dy/dx = f(x, y) for accurate results.
# - Consider adapting the code for dynamic step size based on the solution behavior.
# - Explore additional error analysis techniques for a more comprehensive understanding.

# Additional Notes:
# - The code generates a plot for visual comparison between the RK4 solution and the exact solution.
# - Results are printed on screen and saved in a text file for further analysis.

# Usage:
# Example usage is provided for solving the ODE dy/dx = -y. Customize initial conditions and parameters accordingly.
# Save the code with a meaningful filename and adjust the model function for different ODEs.
# Execute the script to obtain numerical solutions and visual comparisons.

# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import math

# Define the differential equation dy/dx
def model(y, x):
    k = (1 - y)
    dydx = k * y
    return dydx

# Initial conditions and parameters
x0 = 0  # Initial x
y0 = np.exp(-4) / (np.exp(-4) + 1)  # Initial condition for y
x_final = 10  # Total solution interval
h = 0.01  # Step size

# Fourth Order Runge-Kutta method

# Calculate the number of steps for iteration
n_step = math.ceil(x_final / h)

# Definition of arrays to store the solution
y_rk = np.zeros(n_step + 1)
x_rk = np.zeros(n_step + 1)

# Initialize solution arrays with initial conditions
y_rk[0] = y0
x_rk[0] = x0

# Populate the x array based on the step size
for i in range(n_step):
    x_rk[i + 1] = x_rk[i] + h

# Apply RK method n_step times
for i in range(n_step):
    # Compute the four slopes using RK4 method
    x_dummy = x_rk[i]
    y_dummy = y_rk[i]
    k1 = model(y_dummy, x_dummy)

    x_dummy = x_rk[i] + h / 2
    y_dummy = y_rk[i] + k1 * h / 2
    k2 = model(y_dummy, x_dummy)

    x_dummy = x_rk[i] + h / 2
    y_dummy = y_rk[i] + k2 * h / 2
    k3 = model(y_dummy, x_dummy)

    x_dummy = x_rk[i] + h
    y_dummy = y_rk[i] + k3 * h
    k4 = model(y_dummy, x_dummy)

    # Compute the slope as a weighted average of the four slopes
    slope = 1 / 6 * k1 + 2 / 6 * k2 + 2 / 6 * k3 + 1 / 6 * k4

    # Use the RK method to solve the ODE
    y_rk[i + 1] = y_rk[i] + h * slope

    # Generate a finely sampled exact solution for comparison, MODIFY
    n_exact = 100
    x_exact = np.linspace(0, x_final, n_exact + 1)
    y_exact = np.exp(x_exact - 4) / (np.exp(x_exact - 4) + 1)

# Calculate exact values of the solution for comparison
for i in range(n_exact + 1):
    y_exact[i] = y0 * math.exp(-x_exact[i])

# Print results on screen
# Print results on screen with neatly aligned columns
rounding_precision = 4

# Print results on screen with neatly aligned columns and rounding
print(f'Step\t\t x\t\t\t y-eul\t\t\t y-exact\t\t\t Error (%)')
for i in range(n_step + 1):
    print(f'{i}\t\t {x_rk[i]:.{rounding_precision}f}\t\t {y_rk[i]:.{rounding_precision}f}\t\t {y0 * math.exp(-x_rk[i]):.{rounding_precision}f}\t\t {(y_rk[i] - y0 * math.exp(-x_rk[i])) / (y0 * math.exp(-x_rk[i])) * 100:.{rounding_precision}f}')

'''
# Save results in a text file
file_name = 'output_h' + str(h) + '.dat'
f_io = open(file_name, 'w')
for i in range(n_step + 1):
    s1 = str(i)
    s2 = str(x_rk[i])
    s3 = str(y_rk[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
'''

# Plot results for comparison
plt.plot(x_rk, y_rk, 'b.-', x_exact, y_exact, 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
