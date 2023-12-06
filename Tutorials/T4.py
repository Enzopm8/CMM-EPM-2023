#                                  Tutorial 4
#Ex1:
import numpy as np
import matplotlib.pyplot as plt
import math


# Define the Newton-Raphson method
def newton(f, Df, x0, epsilon, max_iter):
    xn = x0
    iterations = []
    errors = []
    for n in range(0, max_iter):
        fxn = f(xn)
        iterations.append(n)
        errors.append(fxn)
        if abs(fxn) < epsilon:
            break  # Exit the loop when the solution is found
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
    if n == max_iter - 1:
        print('Exceeded maximum iterations. No solution found.')
    return xn, iterations, errors

# Define the Secant method with specified interval [a, b]
def secant(f, a, b, N):
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
            print("Found exact solution:", m_n)
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))

# Define the function and its derivative
f = lambda x: x**2 + 4*x - 12
df = lambda x: 2*x + 4  

x0 = 1
max_iter = 100

N_values = [1, 10]

solutions_newton = []
iteration_counts_newton = []
error_values_newton = []

# Define the interval [a, b] you want to use for the Secant method
a = 0
b = 5.0

# Call the secant method with the specified interval [a, b]
solution_secant = secant(f, a, b, max_iter)

solutions_secant = []
iteration_counts_secant = []
error_values_secant = []

for N in N_values:
    epsilon = 10**(-N)
    solution_newton, iterations_newton, errors_newton = newton(f, df, x0, epsilon, max_iter)
    solution_secant = secant(f, x0, x0 + epsilon, max_iter)  # Use Secant method
    solutions_newton.append(solution_newton)
    iteration_counts_newton.append(iterations_newton)
    
    error_values_newton.append(errors_newton)
    solutions_secant.append(solution_secant)
    iteration_counts_secant.append(np.arange(1, len(iterations_newton) + 1))  # Incremental iterations
    error_values_secant.append([f(x) for x in iterations_newton])  # Evaluate error for Secant method

# Plot the results with only one legend entry for each method
plt.figure(figsize=(10, 6))
for i, N in enumerate(N_values):
    plt.semilogy(iteration_counts_newton[i], np.abs(error_values_newton[i]), label=f'Newton N={N}' if i == 0 else '')
    plt.semilogy(iteration_counts_secant[i], np.abs(error_values_secant[i]), label=f'Secant N={N}' if i == 0 else '')

plt.xlabel('Number of Iterations')
plt.ylabel('Error (|f(xroot)|)')
plt.legend()
plt.title('Convergence Behavior of Newton-Raphson and Secant methods for different N values')
plt.grid(True)
plt.show()

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Ex2:
def synthetic_division(coefficients, divisor):
    n = len(coefficients)
    
    # Initialize the result list with the first coefficient
    result = [coefficients[0]]
    
    # Perform synthetic division
    for i in range(1, n):
        term = coefficients[i] + result[-1] * divisor
        result.append(term)
    
    # Calculate the remainder as the last term of the result
    remainder = result[-1]
    
    return result[:-1], remainder

# Coefficients of the polynomial f(x) = x^2 + 2x - 24
coefficients = [1, 2, -24]

# Divisor: (x - 4)
divisor = 4

# Perform synthetic division
quotient, remainder = synthetic_division(coefficients, divisor)

# Print the quotient coefficients and remainder
print("Quotient coefficients:", quotient)
print("Remainder:", remainder)
