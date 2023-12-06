
# Function: Solving a System of First-Order ODEs using the Euler Method
# Description:
# This script is used to numerically solve a system of first-order ordinary differential equations (ODEs).
# The equations are defined as dy_j/dx = f_j(x, y_j) for j = [1, 2] in this case.
# Usage:
# - Applicable for solving systems of ODEs numerically with given initial conditions and parameters.
# - Useful for understanding the behavior of dynamic systems represented by ODEs.
# - The Euler method might not be accurate for stiff equations or may require very small step sizes in some cases.
# - Provides a numerical solution and allows comparison between different variables' behaviors.
# - Saves the results in a text file for later analysis or usage.
# Import necessary modules
import numpy as np  # Module for numerical operations
import matplotlib.pyplot as plt  # Module for plotting
import math  # Module for mathematical functions

# ------------------------------------------------------
# Function defining the system of first-order ODEs
# The equation is dy_j/dx = f_j(x, y_j) for j = [1, 2] in this case
def model(x, y_1, y_2):
    # Define the ODEs for the system
    f_1 = -0.5 * y_1
    f_2 = 4.0 - 0.3 * y_2 - 0.1 * y_1
    return [f_1, f_2]
# ------------------------------------------------------

# ------------------------------------------------------
# Initial conditions and parameters
x0 = 0  # Initial x
y0_1 = 4  # Initial condition for y_1
y0_2 = 6  # Initial condition for y_2
x_final = 20  # Total solution interval
h = 0.1  # Step size
# ------------------------------------------------------

# ------------------------------------------------------
# Euler method for solving the system of ODEs

# Calculate the number of steps for iteration
n_step = math.ceil(x_final / h)

# Define arrays to store the solution
y_1_eul = np.zeros(n_step + 1)  # Array to store the solution for y_1
y_2_eul = np.zeros(n_step + 1)  # Array to store the solution for y_2
x_eul = np.zeros(n_step + 1)  # Array to store x values

# Initialize solution arrays with initial conditions
y_1_eul[0] = y0_1
y_2_eul[0] = y0_2
x_eul[0] = x0

# Populate the x array based on the step size
for i in range(n_step):
    x_eul[i + 1] = x_eul[i] + h

# Apply the Euler method iteratively to solve the ODEs
for i in range(n_step):
    # Compute the slope using the system of differential equations
    [slope_1, slope_2] = model(x_eul[i], y_1_eul[i], y_2_eul[i])
    # Use the Euler method to solve the ODEs
    y_1_eul[i + 1] = y_1_eul[i] + h * slope_1
    y_2_eul[i + 1] = y_2_eul[i] + h * slope_2
# ------------------------------------------------------

# ------------------------------------------------------
# Plot the results for visualization
plt.plot(x_eul, y_1_eul, 'b.-', x_eul, y_2_eul, 'r-')
plt.xlabel('x')
plt.ylabel('y_1(x), y_2(x)')
plt.show()
# ------------------------------------------------------

# ------------------------------------------------------
# Save the results in a text file for later use
file_name = 'output_h' + str(h) + '.dat'
f_io = open(file_name, 'w')
for i in range(n_step + 1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_1_eul[i])
    s4 = str(y_2_eul[i])
    s_tot = s1 + ' ' + s2 + ' ' + s3 + ' ' + s4
    f_io.write(s_tot + '\n')
f_io.close()
# ------------------------------------------------------
