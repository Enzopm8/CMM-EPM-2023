#                           Scipy fsolve
#remember scipy comes from numpy so convert sympy to numpy using lambdify if needed
import numpy as np
from scipy.optimize import fsolve

def solve_equation(equation, initial_guesses):
    """
    Solve a given equation with fsolve using multiple initial guesses.

    Parameters:
    - equation: The equation to solve, expressed as a lambda function.
    - initial_guesses: List of initial guesses.

    Returns:
    - solutions: List of solutions.
    """

    solutions = []
    for idx, guess in enumerate(initial_guesses, 1):
        solution = fsolve(equation, guess)
        solutions.append(solution[0])
        print(f"Root {idx}: {solution[0]:.6f} (Initial Guess: {guess})")

    return solutions

# Example usage:

# Define the equation as a lambda function
quadratic_equation = lambda x: x**2 - 4

# Set up a list of initial guesses
initial_guesses = [2.0, -2.0]

# Solve the equation with fsolve
solutions = solve_equation(quadratic_equation, initial_guesses)

# Display the results
print("\nSummary of Results:")
for idx, solution in enumerate(solutions, 1):
    print(f"Root {idx}: {solution:.6f}")
    
#------------------------------------------------------------------------------
#                           Fsolve for systems of equations
def system_of_equations(variables):
    x, y = variables
    equation1 = x**2 + y**2 - 1  # Circle equation
    equation2 = x - y             # Diagonal line

    return [equation1, equation2]

# List of initial guesses for the variables
initial_guesses = [[0.5, 0.5], [-0.5, 0.5]]

# Solve the system of equations with fsolve for each initial guess
solutions = [fsolve(system_of_equations, guess) for guess in initial_guesses]

# Display all solutions
print("Solutions for the system of equations:")
for idx, solution in enumerate(solutions, 1):
    print(f"Solution {idx}: x = {solution[0]:.6f}, y = {solution[1]:.6f}")

