import numpy as np
import math
import matplotlib.pyplot as plt

# Define the target function
def f(x):
    return -x**3 + 6*x**2 - 4*x - 2

# Plot the target function
x = np.linspace(-1, 1)
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()

# Define the first and second derivatives of the target function
def fprime(x):
    return -3*x**2 + 12*x - 4

def fsecond(x):
    return -6*x + 12

# Define the quadratic approximation function
def quadratic_approx(x, x0, f, fprime, fsecond):
    return f(x0) + fprime(x0)*(x - x0) + 0.5*fsecond(x0)*(x - x0)**2

# Plot the target function and its quadratic approximation
x = np.linspace(-1, 1)
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()
ax.plot(x, quadratic_approx(x, 0, f, fprime, fsecond), color='red', label='quadratic approximation')
ax.set_ylim([-5, 3])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.legend()

# Define the Newton optimization method
def newton(x0, fprime, fsecond, maxiter=100, eps=0.0001):
    x = x0
    for i in range(maxiter):
        xnew = x - (fprime(x) / fsecond(x))
        if xnew - x < eps:
            print('Converged')  # Indicate convergence in the console
            return xnew
        x = xnew
    return x

# Apply Newton's method and plot the result
x_star = newton(0, fprime, fsecond)
print("Optimal x:", x_star)

fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()
ax.plot(x, quadratic_approx(x, x_star, f, fprime, fsecond), color='red', label='quadratic approximation')
ax.set_ylim([-5, 3])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.axvline(x=x_star, color='green')  # Indicate the optimal x with a green vertical line
plt.legend()