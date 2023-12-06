# Euler Method for Ordinary Differential Equations
# This script uses the Euler method to solve the first-order ordinary differential equation dy/dx = -y numerically.

# Description:
#It calculates and visualizes the approximate solution of the differential equation using the Euler method.

# Usage:
# This code is recommended for solving first-order ordinary differential equations with specified initial conditions.
# It demonstrates the approximation of the solution using the Euler method with a predefined step size.
# Also, it compares the Euler method approximation with the exact solution for reference and calculates the error percentage.

# Recommended Usage:
# - Use 'euler' method for quick approximations with larger step sizes.
# - Use 'runge_kutta' method for more accurate results, especially with smaller step sizes.
# - Adjust the step size based on the desired balance between accuracy and computation time.


import numpy as np
import matplotlib.pyplot as plt
import math


def model(y, x, k):
    dydx = k * y
    return dydx


def runge_kutta_step(model, y, x, h, k):
    k1 = h * model(y, x, k)
    k2 = h * model(y + 0.5 * k1, x + 0.5 * h, k)
    k3 = h * model(y + 0.5 * k2, x + 0.5 * h, k)
    k4 = h * model(y + k3, x + h, k)

    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def solve_ode(model, x0, y0, x_final, h, method='euler', params=None, plot=True, save_results=False):
    """
    Solve a first-order ordinary differential equation numerically.

    Parameters:
    - model: Function defining the ODE.
    - x0, y0: Initial conditions.
    - x_final: Total solution interval.
    - h: Step size for the integration method.
    - method: Integration method ('euler' or 'runge_kutta').
    - params: Additional parameters for the ODE model.
    - plot: Whether to plot the results.
    - save_results: Whether to save the results in a file.

    Returns:
    - x_eul, y_eul: Arrays storing the numerical solution.
    - x_exact, y_exact: Arrays storing the exact solution.
    """
    n_step = math.ceil(x_final / h)

    # Arrays to store the solution
    y_eul = np.zeros(n_step + 1)
    x_eul = np.zeros(n_step + 1)

    # Initialize the solution arrays with the initial condition, x0 and y0 given in call
    y_eul[0] = y0
    x_eul[0] = x0

    # Populate the x array based on the step size
    for i in range(n_step):
        x_eul[i + 1] = x_eul[i] + h

    # Apply the selected integration method
    for i in range(n_step):
        if method == 'euler':
            slope = model(y_eul[i], x_eul[i], params)
            y_eul[i + 1] = y_eul[i] + h * slope
        elif method == 'runge_kutta':
            y_eul[i + 1] = runge_kutta_step(model, y_eul[i], x_eul[i], h, params)

    # Generate a finely sampled exact solution for comparison
    n_exact = 1000
    x_exact = np.linspace(0, x_final, n_exact + 1)
    y_exact = y0 * np.exp(-x_exact)

    # Print results and calculate the error percentage
    print('Step | x    | y-approx  | y-exact   | Error (%)')
    for i in range(n_step + 1):
        error_percentage = (y_eul[i] - y0 * np.exp(-x_eul[i])) / (y0 * np.exp(-x_eul[i])) * 100
        print(f'{i:4} | {x_eul[i]:.2f} | {y_eul[i]:.4f}    | {y0 * np.exp(-x_eul[i]):.4f}    | {error_percentage:.4f}%')

    # Save results in a text file for future use if needed
    if save_results:
        file_name = f'output_{method}_h{h}.dat'
        np.savetxt(file_name, np.column_stack((x_eul, y_eul)), fmt='%.4f', header='x y-approx')

    # Plot the approximate and exact solutions
    if plot:
        plot_solution(x_eul, y_eul, x_exact, y_exact, method)

    return x_eul, y_eul, x_exact, y_exact

def plot_solution(x_eul, y_eul, x_exact, y_exact, method):
    plt.plot(x_eul, y_eul, 'b.-', label=f'Approximate Solution ({method.capitalize()} Method)')
    plt.plot(x_exact, y_exact, 'r-', label='Exact Solution')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.show()

# Example usage: can use either 'euler' or 'runge_kutta'
x_eul, y_eul, x_exact, y_exact = solve_ode(model, x0=0, y0=1, x_final=1, h=0.1, method='runge_kutta', params=-1, plot=True, save_results=False)
