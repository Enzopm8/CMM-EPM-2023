# Tutorial 5
#------------------------------------------------------------------------------
#Ex:1
# importing modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
import math
import random

x = np.array([0.  , 0.06666667, 0.13333333, 0.2 ,  0.26666667, 0.33333333,
     0.4 , 0.46666667, 0.53333333, 0.6 ,  0.66666667, 0.73333333,
     0.8 , 0.86666667, 0.93333333, 1.  , ])

y = np.array([ 0.00000000e+00,  7.78309056e-01,  1.24040577e+00,  1.24494914e+00,
      8.90566050e-01,  4.33012702e-01,  1.12256994e-01,  4.54336928e-03,
     -4.54336928e-03, -1.12256994e-01, -4.33012702e-01, -8.90566050e-01,
     -1.24494914e+00, -1.24040577e+00, -7.78309056e-01, -4.89858720e-16])

spl = splrep(x, y) #perform cubic spline interpolation on x and y
x2 = np.linspace(0, 1, 128) #create a smoother curve for x and y with 128 points
y2 = splev(x2, spl) #evaluate the B-Spline at the points on x2 and interpolate y2


plt.plot(x, y, 'ko', label='Data') #Plots Data
plt.plot(x2, y2, 'r-', label='Spline') #Plots interpolated spline
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show the plot
plt.show()

#------------------------------------------------------------------------------
#Ex 2:
    
plt.plot(x, y, 'ko', label='Data')

#estimate degree of polynomial for LOBF
N = 1

# Fit a 1st-degree polynomial (linear model)
coefficients = np.polyfit(x, y, N)

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
