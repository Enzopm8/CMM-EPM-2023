# Function: Adaptive Step Size Euler Method for Solving First-Order ODEs
# Description:
# This script uses the Euler method to solve a first-order ordinary differential equation dy/dx = -1000y + 3000 - 2000 * exp(-x).
# The step size changes at x = x2, increasing after this point.
# Usage:
# - Suitable for solving first-order ordinary differential equations with adaptive step sizes for better accuracy.
# - Not recommended for highly stiff differential equations.
# - Outputs the numerical solution and a refined version of the exact solution for comparison and plotting.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Define the differential equation dy/dx
def model(y, x):
    dydx = -1000.0 * y + 3000.0 - 2000.0 * math.exp(-x)
    return dydx

# Define initial conditions and parameters
x0 = 0
y0 = 0
x_final = 0.3

# Change step size at x = x2
x2 = 0.01
# Step size for x < x2
h1 = 0.0002
# Increased step size for x > x2
h2 = 0.0021

h = h1  # Set initial step size

# Calculate the number of steps for iteration
n_step = math.ceil(x2 / h1) + math.ceil((x_final - x2) / h2)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step + 1)
x_eul = np.zeros(n_step + 1)

# Initialize the solution arrays with initial conditions
y_eul[0] = y0
x_eul[0] = x0

# Populate the x array with varying step sizes
for i in range(n_step):
    if x_eul[i] > x2:
        x_eul[i + 1] = x_eul[i] + h2
    else:
        x_eul[i + 1] = x_eul[i] + h

# Apply the Euler method with adaptive step sizes
for i in range(n_step):
    slope = model(y_eul[i], x_eul[i])  # Compute the slope using the differential equation
    if x_eul[i] > x2:
        h = h2  # Change step size after x = x2
    else:
        h = h1
    y_eul[i + 1] = y_eul[i] + h * slope  # Use the Euler method

# Generate a refined version of the exact solution for comparison and plotting
n_exact = 1000
x_exact = np.linspace(0, x_final, n_exact + 1)
y_exact = 3.0 - 0.998 * np.exp(-1000 * x_exact) - 2.002 * np.exp(-x_exact)

# Save the numerical solution in a text file
file_name = 'output' + str(h1) + '_' + str(h2) + '.dat'
f_io = open(file_name, 'w')
for i in range(n_step + 1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()

# Save the refined exact solution in a text file for comparison
file_name = 'output_exact.dat'
f_io = open(file_name, 'w')
for i in range(n_exact + 1):
    s1 = str(i)
    s2 = str(x_exact[i])
    s3 = str(y_exact[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()

# Plot the numerical and refined exact solutions for comparison
plt.plot(x_eul, y_eul, 'b.-', x_exact, y_exact, 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
