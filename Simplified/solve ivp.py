from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def solve_system_of_odes(t, y, functions):
    dydt = [func(t, y) for func in functions]
    return dydt

def solve_ode(initial_conditions, t_span, output_time, functions, step_size=None, method='RK45', plot_solution=True, decimal_places=4, rtol=None, atol=None):
    try:
        # Solve the system of ODEs using solve_ivp with max_step and customizable tolerance
        sol = solve_ivp(
            solve_system_of_odes, t_span, initial_conditions,
            args=(functions,), method=method, max_step=step_size,
            rtol=rtol, atol=atol
        )

        # Check if the integration was successful
        if not sol.success:
            raise RuntimeError(f"Integration failed: {sol.message}")

        # Create a dictionary to store the output values
        output_dict = {f'y{i+1}': np.interp(output_time, sol.t, sol.y[i]) for i in range(len(initial_conditions))}

        # Print the output values in a structured format with customizable decimal places
        print("\nResults:")
        for i, (var, val) in enumerate(output_dict.items()):
            print(f"{var} at time {output_time}: {val:.{decimal_places}f}")

        # Plot the entire solution if requested
        if plot_solution:
            plt.figure(figsize=(8, 6))
            for i in range(len(initial_conditions)):
                plt.plot(sol.t, sol.y[i], label=f'y{i+1}(t)')
                plt.scatter(output_time, output_dict[f'y{i+1}'], color='red', marker='o', label=f'y{i+1} at t={output_time}')
            plt.title('Solution of the System of Ordinary Differential Equations')
            plt.xlabel('Time (t)')
            plt.ylabel('State variables')
            plt.legend()
            plt.grid(True)
            plt.show()

        return sol, output_dict

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage for a system of two ODEs with different formats
def ode1(t, y):
    return -2 * y[0]  # dy1/dt = -2y1

def ode2(t, y):
    return y[1]  # dy2/dt = y2

initial_conditions_system = [1.0, 0.5]  # Initial values of the state variables
time_span_system = (0, 5)                 # Time span for integration
output_time_system = 2.5                  # Time at which to output the solution
custom_step_size_system = 0.01             # Specify the desired step size
functions_system = [ode1, ode2]           # List of functions for each ODE
custom_decimal_places =  6                # Customize the number of decimal places
custom_rtol = 1e-5                      # relative tolerance
custom_atol = 1e-7                      # absolute tolerance

# Solve the system of ODEs with the specified parameters, output the values at the specified time, and plot the solution
solution_system, output_values = solve_ode(
    initial_conditions_system, time_span_system, output_time_system,
    functions_system, step_size=custom_step_size_system,
    plot_solution=True, decimal_places=custom_decimal_places,
    rtol=custom_rtol, atol=custom_atol
    )