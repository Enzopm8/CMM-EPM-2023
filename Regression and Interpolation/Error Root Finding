"""
Numerical Root-Finding Methods

This code demonstrates the Newton-Raphson and Secant methods for root-finding.
These methods iteratively find the root of a given function using different approaches.
Use these methods when you have an initial guess and want to find a root of a function.
However, be cautious as they may fail to converge or provide inaccurate results for complex functions or poor initial guesses.

When to use this code:
- Use this code when you have a continuous function and an initial guess for the root.
- The function should have a derivative for Newton's method.

When not to use this code:
- Avoid using this code when the function is discontinuous or lacks a derivative.
- Be cautious when using it for functions with multiple roots or near singular points.

Steps to modify for different functions:
1. Define your function f(x) in the 'f' lambda function.
2. If using Newton's method, define the derivative of your function Df(x) in the 'df' lambda function.
3. Adjust the initial guess (x0 for Newton, a and b for Secant) accordingly.
4. Optionally, adjust the maximum number of iterations (n_max) and other parameters as needed.

"""

# Importing necessary modules
import math
import numpy as np
import matplotlib.pyplot as plt

# Definition of functions for Newton and Secant methods
def newton2(f, Df, x0, N):
    # Newton's method for root-finding
    # f - function
    # Df - derivative of function
    # x0 - initial guess
    # N - maximum number of iterations
    xn = x0
    for n in range(0, N):
        fxn = f(xn)
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
    return xn

def secant(f, a, b, N):
    # Secant method for root-finding
    # f - function
    # a, b - initial guesses for the root
    # N - maximum number of iterations
    if f(a) * f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1, N + 1):
        m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found an exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))

# Initial setup for the first function: x^2 + 4x - 12
f = lambda x: x**2 + 4*x - 12
df = lambda x: 2*x + 4
x0 = 1
a = 1
b = 3

# Arrays for storing results
n_max = 20
n_array_N = np.zeros(n_max - 1)
sol_array_N = np.zeros(n_max - 1)
fun_array_N = np.zeros(n_max - 1)
n_array_S = np.zeros(n_max - 1)
sol_array_S = np.zeros(n_max - 1)
fun_array_S = np.zeros(n_max - 1)

# Iterations for Newton and Secant methods for the first function
for i in range(1, n_max):
    solution = newton2(f, df, x0, i)
    n_array_N[i - 1] = i
    sol_array_N[i - 1] = solution
    fun_array_N[i - 1] = np.absolute(f(solution))
    
    solution = secant(f, a, b, i)
    n_array_S[i - 1] = i
    sol_array_S[i - 1] = solution
    fun_array_S[i - 1] = np.absolute(f(solution))

# Print the numerical solutions
print("Newton Method - Numerical Solution:", sol_array_N[-1])
print("Secant Method - Numerical Solution:", sol_array_S[-1])

# Plotting for the first function with legends and displaying the iterations, solution, and error
plt.figure()
plt.plot(n_array_N, sol_array_N, '-o', label='Newton Method')
plt.plot(n_array_S, sol_array_S, '-o', label='Secant Method')
plt.xlabel("Number of iterations")
plt.ylabel("Solution")
plt.xlim(0, n_max)
plt.legend()
plt.show()

plt.figure()
plt.semilogy(n_array_N, fun_array_N, '-o', label='Newton Method')
plt.semilogy(n_array_S, fun_array_S, '-o', label='Secant Method')
plt.semilogy(n_array_S, np.exp(-2.0*n_array_S), label='Error - Exp(-2.0*n)')
plt.semilogy(n_array_S, np.exp(-2.5*n_array_S), label='Error - Exp(-2.5*n)')
plt.xlabel("Number of iterations")
plt.ylabel("Error, defined as f(solution)")
plt.xlim(0, n_max)
plt.legend()
plt.show()
