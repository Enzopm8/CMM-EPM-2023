# Implicit Euler Method for Ordinary Differential Equations
# Description:
# This script solves a first-order ordinary differential equation using the implicit Euler method.
# It computes and compares the approximate solution obtained via the implicit Euler method with the exact solution.
# Usage:
# - Solves a first-order ordinary differential equation dy/dx = -1000y + 3000 - 2000 * exp(-x) with specific initial conditions.
# - Implements the implicit Euler method to approximate the solution within a given step size.
# - Compares the approximated solution with the exact solution for validation.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Function representing dy/dx in the equation to solve
def model(y, x):
    dydx = -1000.0 * y + 3000.0 - 2000.0 * math.exp(-x)
    return dydx

# Initial conditions and parameters
x0 = 0  # Initial x value
y0 = 0  # Initial y value
x_final = 0.3  # Total solution interval
h = 0.01  # Step size for the implicit Euler method

# Function for Secant method to find roots
def secant_2(f, a, b, iterations):
    for i in range(iterations):
        c = a - f(a) * (b - a) / (f(b) - f(a))
        if abs(f(c)) < 1e-13:
            return c
        a = b
        b = c
    return c

# Calculate the number of steps
n_step = math.ceil(x_final / h)

# Arrays to store the solution
y_eul = np.zeros(n_step + 1)
x_eul = np.zeros(n_step + 1)

# Initialize the solution arrays with the initial condition
y_eul[0] = y0
x_eul[0] = x0

# Populate the x array based on the step size
for i in range(n_step):
    x_eul[i + 1] = x_eul[i] + h

# Apply implicit Euler method to approximate the solution
for i in range(n_step):
    F = lambda y_i_plus_1: y_eul[i] + model(y_i_plus_1, x_eul[i + 1]) * h - y_i_plus_1
    y_eul[i + 1] = secant_2(F, y_eul[i], 1.1 * y_eul[i] + 10**-3, 10)

# Generate a finely sampled exact solution for comparison
n_exact = 1000
x_exact = np.linspace(0, x_final, n_exact + 1)
y_exact = 3.0 - 0.998 * np.exp(-1000 * x_exact) - 2.002 * np.exp(-x_exact)

# Save results in a text file for future use if needed
file_name = 'output_h' + str(h) + '.dat'
f_io = open(file_name, 'w')
for i in range(n_step + 1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()

# Save exact solution in a text file for reference
file_name = 'output_exact.dat'
f_io = open(file_name, 'w')
for i in range(n_exact + 1):
    s1 = str(i)
    s2 = str(x_exact[i])
    s3 = str(y_exact[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()

# Plot the approximate and exact solutions for comparison
plt.plot(x_eul, y_eul, 'b.-', x_exact, y_exact, 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
