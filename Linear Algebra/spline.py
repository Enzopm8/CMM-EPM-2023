# Interpolation Comparison
# Description:
# This script showcases two different interpolation techniques: linear and spline interpolation.
# It imports data from an external file, performs interpolation using both methods, and plots the results.

# Recommended Use:
# - Utilize this code when you need to understand and compare linear and spline interpolation methods.
# - Useful for educational purposes, demonstrating the differences between interpolation techniques.
# - Suitable for cases where smooth curves are needed between known data points.

# Not Recommended Use:
# - Avoid using this code as a standalone interpolation tool for large datasets.
# - For production-level tasks or precise interpolations, consider specialized libraries like SciPy.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

'''
# Import data from an external file 'data_int.py'
import data_int

# Assign variables for x and y data from the imported file
x = data_int.x
y = data_int.y
'''
# Sample data for testing interpolation
x = np.array([0.1, 0.3, 0.5, 0.8])
y = np.array([1.2, 0.9, 1.5, 1.0])

# Array defining points for evaluating the interpolation
x_int = np.linspace(min(x), max(x), num=64)

# Perform linear interpolation
f_lin = interpolate.interp1d(x, y, kind='linear')
# Evaluate linear interpolation at the desired points
y_int_lin = f_lin(x_int)

# Perform spline interpolation
f_spline = interpolate.splrep(x, y, s=0)

# Evaluate spline interpolation at the desired points
y_int_spline = interpolate.splev(x_int, f_spline, der=0)


# Plot the interpolation results
plt.figure()
plt.plot(x, y, 'go-', label='Original Data')  # plot the original data points
plt.plot(x_int, y_int_lin, 'r.', label='Linear Interpolation')  # plot linear interpolation
plt.plot(x_int, y_int_spline, 'b.', label='Spline Interpolation')  # plot spline interpolation
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolation Comparison')
plt.show()

# Plot a zoomed-in version of the interpolation results
plt.figure()
plt.plot(x, y, 'go-', label='Original Data')  # plot the original data points
plt.plot(x_int, y_int_lin, 'r.', label='Linear Interpolation')  # plot linear interpolation
plt.plot(x_int, y_int_spline, 'b.', label='Spline Interpolation')  # plot spline interpolation
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Zoomed-In Interpolation Comparison')
plt.xlim(0.05, 0.3)  # set x-axis limits for the zoomed-in plot
plt.ylim(0.5, 1.5)  # set y-axis limits for the zoomed-in plot
plt.show()
