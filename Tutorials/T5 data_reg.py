# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
import random

x = np.array([0.0, 0.06666667, 0.13333333, 0.2, 0.26666667, 0.33333333,
              0.4, 0.46666667, 0.53333333, 0.6, 0.66666667, 0.73333333,
              0.8, 0.86666667, 0.93333333, 1.0])

y = np.array([2.17312991, 2.19988829, 2.33988149, 2.33940595, 2.41968027, 2.99955891,
              3.04855788, 3.86631749, 3.66009775, 4.42305111, 4.22747852, 4.11717969,
              3.87539822, 4.53121841, 5.52211102, 5.30792203])

plt.plot(x, y, 'ko', label='Data')
# Fit a 1st-degree polynomial (linear model)
coefficients = np.polyfit(x, y, 1)

# Create a linear function based on the coefficients
linear_model = np.poly1d(coefficients)

# Plot the linear model as a new line
x_range = np.linspace(0, 1, 100)  # Create an x range for the model
plt.plot(x_range, linear_model(x_range), 'r-', label='Line of Best Fit (LOBF)')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show the plot
plt.show()

# Print the coefficients of the linear model (slope and intercept)
print("Linear Model Coefficients:")
print(f"Slope (m): {coefficients[0]}")
print(f"Intercept (b): {coefficients[1]}")
#This code adds the line of best fit (LOBF) to your plot, and you can see how it fits the data points.