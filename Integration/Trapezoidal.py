# Recommended Use:
# This code is suitable for visualizing a function and calculating the area under the curve using the trapezoid rule.
# Adjust the 'f' function for your specific integration requirements.

# Not Recommended Use:
# Avoid using this code for highly oscillatory functions or functions with singularities.
# Ensure that the 'f' function is well-behaved within the specified integration limits.

import numpy as np
import matplotlib.pyplot as plt

# Generate data for plotting
x = np.linspace(-0.5, 1.5, 100)
y = np.exp(-x**2)  #Function
plt.plot(x, y)

# Define points for filling the area under the curve
x0 = 0; x1 = 1;
y0 = np.exp(-x0**2); y1 = np.exp(-x1**2);
plt.fill_between([x0, x1], [y0, y1])

# Set plot limits and display
plt.xlim([-0.5, 1.5]); plt.ylim([0, 1.5]);
plt.show()

# Calculate the area using the trapezoid rule
A = 0.5 * (y1 + y0) * (x1 - x0)
print("Trapezoid area:", A)

def trapz(f, a, b, N=1000):
    '''
    Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral ∫_a^b f(x) dx by the sum:
    (dx/2) ∑_{k=1}^N (f(x_k) + f(x_{k-1}))
    where x_k = a + k*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal length.

    Examples
    --------
    >>> trapz(np.sin, 0, np.pi/2, 1000)
    0.9999997943832332
    '''
    x = np.linspace(a, b, N+1)  # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:]  # right endpoints
    y_left = y[:-1]  # left endpoints
    dx = (b - a) / N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

result_trapz = trapz(np.sin, 0, np.pi/2, 1000)
print ('trapz:',result_trapz )