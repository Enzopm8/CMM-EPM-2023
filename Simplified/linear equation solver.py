from scipy.optimize import fsolve

# Define the system of equations with constants
def equations(vars, a, b, c, d):
    x, y = vars
    eq1 = a*x + b*y**2 - c
    eq2 = d*x**2 - y - c
    return [eq1, eq2]

# Constants
a, b, c, d = 1, 1, 4, 1  # Example values for constants

# Initial guess
initial_guess = [1, 1]

# Solve the equations
solution = fsolve(equations, initial_guess, args=(a, b, c, d))

print('solution: ', solution)
