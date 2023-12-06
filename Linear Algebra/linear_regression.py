# Linear Regression Comparison with Excel Option
# Description:
# This script demonstrates two methods of performing linear regression and compares their results by fitting a linear model to given data.
# The script provides the option to read 'x' and 'y' values from an Excel file.
# Recommended Use:
# - This code is suitable for comparing manual linear regression calculations with Python function-based linear regression.
# - Use it when you want to visualize and compare the results of two different linear regression methods.
# - Helpful for educational purposes and understanding the underlying calculations.

# Not Recommended Use:
# - Avoid using this code as a standalone linear regression tool for large datasets, as it primarily focuses on comparison and visualization.
# - For production-level tasks, consider dedicated libraries like scikit-learn for more robust and efficient linear regression implementations.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

''''
Use This if you want to import from excel
file_path = XXXXXXXX
data = pd.read_excel(file_path)
x = data['x'].values
y = data['y'].values
'''

# If not reading from Excel, provide sample data or read from 'data_reg.py'
x = np.array([1, 3, 7, 10, 15, 22, 30, 45, 60, 75, 90])
y = np.array([2, 8, 15, 22, 31, 42, 55, 72, 90, 110, 132])

# Array defining points for evaluating the fitted model
x_fit = np.linspace(0, 100, num=100)

# ----------------------------------------------------
# Linear regression using least squares 
# with formulas presented in Lecture

n = len(x)
a_1 = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
a_0 = np.mean(y) - a_1 * np.mean(x) 

# Evaluate the linear regression at the desired points 
y_reg_lin = a_0 + a_1 * x_fit 

# Print coefficients of linear regression:
print('Manual Linear Regression Coefficients:')
print(f'a_1 (Slope): {a_1:.4f}')
print(f'a_0 (Intercept): {a_0:.4f}')
# ----------------------------------------------------

# ----------------------------------------------------
# Linear regression using Python functions

# Compute the coefficients for the linear regression
coef = np.polyfit(x, y, 1)
# Generate the linear function that fits the data 
f_reg_lin = np.poly1d(coef)

# Evaluate the linear regression at the desired points 
y_reg_lin_py = f_reg_lin(x_fit)

# Print coefficients of linear regression:
print('\nPython Function Linear Regression Coefficients:')
print(f'a_1 (Slope): {coef[0]:.4f}')
print(f'a_0 (Intercept): {coef[1]:.4f}')
# ----------------------------------------------------

# Plot results
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

axes[0].plot(x, y, 'gh', ms=5, label='Data Points')
axes[0].plot(x_fit, y_reg_lin, 'b-', label='Manual Regression')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].legend()
axes[0].set_title('Manual Linear Regression')

axes[1].plot(x, y, 'gh', ms=5, label='Data Points')
axes[1].plot(x_fit, y_reg_lin_py, 'r-', label='Python Function Regression')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].legend()
axes[1].set_title('Python Function Linear Regression')

plt.tight_layout()
plt.show()
