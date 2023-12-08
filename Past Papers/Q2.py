# solve the non-linear systems and linear systems
# report the sol for theta and w at t: 10, 20 ,30 for both cases
# inital cond: t = 0, w0 = 0 and theta0 = pi/4
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
l = 9.81  # length of the pendulum (m)
h = 0.001  # time step for Euler method (s)
t_max = 30  # maximum time (s)

# Function to compute derivatives for the non-linear system
def derivatives_nonlinear(theta, omega):
    dtheta_dt = omega
    domega_dt = -g / l * np.sin(theta)
    return dtheta_dt, domega_dt

# Function to compute derivatives for the linearized system
def derivatives_linear(theta, omega):
    dtheta_dt = omega
    domega_dt = -g / l * theta
    return dtheta_dt, domega_dt

# Function to solve the system using the Euler method
def solve_system(derivatives, initial_conditions):
    t_values = np.arange(0, t_max + h, h)
    theta_values = np.zeros_like(t_values)
    omega_values = np.zeros_like(t_values)

    # Set initial conditions
    theta_values[0] = initial_conditions['theta']
    omega_values[0] = initial_conditions['omega']

    # Euler method
    for i in range(1, len(t_values)):
        dtheta_dt, domega_dt = derivatives(theta_values[i - 1], omega_values[i - 1])
        theta_values[i] = theta_values[i - 1] + h * dtheta_dt
        omega_values[i] = omega_values[i - 1] + h * domega_dt

    return t_values, theta_values, omega_values

# Function to calculate the period of oscillation
def calculate_period(t_values, theta_values):
    # Find the indices where the system crosses theta = 0 from positive to negative
    zero_crossings = np.where(np.diff(np.sign(theta_values)) < 0)[0]

    # Calculate the period based on the time values at the zero crossings
    periods = np.diff(t_values[zero_crossings])
    average_period = np.mean(periods)

    return average_period

# Function to print the values of theta and omega at specified times
def print_values_at_times(t_values, theta_values, omega_values, times):
    header = ["Time (s)", "Theta", "Omega"]

    rows = []
    for time in times:
        index = int(time / h)
        rows.append([time, theta_values[index], omega_values[index]])

    print(tabulate(rows, headers=header, tablefmt="grid"))

# Function to find 𝜃0 for a given difference range
def find_theta0_for_difference_range(difference_range):
    theta0_range = np.arange(np.pi / 4, np.pi / 2, 0.01)  # Adjust the step size as needed

    for theta0 in theta0_range:
        initial_conditions = {'theta': theta0, 'omega': 0}

        t_values_nonlinear, _, _ = solve_system(
            derivatives_nonlinear, initial_conditions
        )

        t_values_linear, _, _ = solve_system(
            derivatives_linear, initial_conditions
        )

        period_nonlinear = calculate_period(t_values_nonlinear, _)
        period_linear = calculate_period(t_values_linear, _)

        difference_percentage = abs((period_linear - period_nonlinear) / period_nonlinear) * 100

        if difference_range[0] <= difference_percentage <= difference_range[1]:
            return theta0

    return None  # Return None if no suitable 𝜃0 is found within the range

# Evaluate periods and plot oscillations for different initial conditions
initial_conditions_list = [{'theta': np.pi / 4, 'omega': 0},
                            {'theta': np.pi / 2, 'omega': 0},
                            {'theta': np.pi / 8, 'omega': 0}]

for initial_conditions in initial_conditions_list:
    t_values_nonlinear, theta_values_nonlinear, omega_values_nonlinear = solve_system(
        derivatives_nonlinear, initial_conditions
    )

    t_values_linear, theta_values_linear, omega_values_linear = solve_system(
        derivatives_linear, initial_conditions
    )

    period_nonlinear = calculate_period(t_values_nonlinear, theta_values_nonlinear)
    period_linear = calculate_period(t_values_linear, theta_values_linear)

    print(f"Initial conditions: Theta0 = {initial_conditions['theta']:.4f}")
    print(f"Non-linear system period: {period_nonlinear:.4f} seconds")
    print(f"Linearized system period: {period_linear:.4f} seconds")

    # Print values of theta and omega at specified times
    print("\nValues at specified times:")
    print("Non-linear system:")
    print_values_at_times(t_values_nonlinear, theta_values_nonlinear, omega_values_nonlinear, [10, 20, 30])
    print("\nLinearized system:")
    print_values_at_times(t_values_linear, theta_values_linear, omega_values_linear, [10, 20, 30])
    print("\n")

    # Plot oscillations for each initial condition
    plt.figure(figsize=(10, 5))
    plt.plot(t_values_nonlinear, theta_values_nonlinear, label="Non-linearized")
    plt.plot(t_values_linear, theta_values_linear, label="Linearized")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Theta (radians)")
    plt.title(f"Theta Motion: Theta0={initial_conditions['theta']:.4f}")
    plt.legend()
    plt.show()

# Find 𝜃0 for a specified difference range
difference_range = [0.95, 1.05]  # Adjust the range as needed
found_theta0 = find_theta0_for_difference_range(difference_range)

if found_theta0 is not None:
    print(f"The value of 𝜃0 for a difference between linear and non-linear periods within {difference_range[0]:.2f}% and {difference_range[1]:.2f}% is approximately: {found_theta0:.4f}")
else:
    print("No suitable 𝜃0 found within the specified difference range.")

