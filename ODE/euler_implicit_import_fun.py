# Function: Implicit Euler Method for Solving First-Order ODEs
# Description:
# The script uses the implicit Euler method to solve the first-order ordinary differential equation dy/dx = -1000y + 3000 - 2000 * exp(-x).
# Usage:
# - Applicable for solving first-order ordinary differential equations numerically with given initial conditions.
# - Not recommended for stiff differential equations where step size h might need to be significantly small.
# - Outputs the numerical solution and a refined version of the exact solution for comparison and plotting.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# Secant method (a very compact version)
def secant_2(f, a, b, iterations):
    for i in range(iterations):
        c = a - f(a)*(b - a)/(f(b) - f(a))
        if abs(f(c)) < 1e-13:
            return c
        a = b
        b = c
    return c
# ------------------------------------------------------

# Define the differential equation dy/dx
def model(y, x):
    dydx = -1000.0 * y + 3000.0 - 2000.0 * math.exp(-x)
    return dydx

# Define initial conditions and parameters
x0 = 0
y0 = 0
x_final = 0.3
h = 0.01

# Calculate the number of steps for iteration
n_step = math.ceil(x_final / h)

# Arrays to store the solution
y_eul = np.zeros(n_step + 1)
x_eul = np.zeros(n_step + 1)

# Initialize the solution arrays with initial conditions
y_eul[0] = y0
x_eul[0] = x0

# Populate the x array based on the step size
for i in range(n_step):
    x_eul[i + 1] = x_eul[i] + h

# Apply implicit Euler method iteratively
for i in range(n_step):
    F = lambda y_i_plus_1: y_eul[i] + model(y_i_plus_1, x_eul[i + 1]) * h - y_i_plus_1
    y_eul[i + 1] = secant_2(F, y_eul[i], 1.1 * y_eul[i] + 10 ** -3, 10)

# Generate a refined version of the exact solution for comparison and plotting
n_exact = 1000
x_exact = np.linspace(0, x_final, n_exact + 1)
y_exact = 3.0 - 0.998 * np.exp(-1000 * x_exact) - 2.002 * np.exp(-x_exact)

# Save the numerical solution in a text file
file_name = 'output_h' + str(h) + '.dat'
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
