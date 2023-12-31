# December 2017 Past Paper
#------------------------------------------------------------------------------
#                                 Q1
# a) graphically plot a 5th order function to find max deflection
print('\n------ Q1. a)------\n')
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
L = 800     #cm
E = 40000   #kN/cm^2
I = 40000   #cm^4
w0 = 3.5    #kN/cm

# Function definition y = 
def beam_equation(x, w0, E, I, L):
    return (w0 / (120 * E * I * L)) * (-x**5 + 2 * (L**2) * (x**3) - (L**4) * x)

# Specify the range of x values, max lengt is the length of the beam L
x_values = np.linspace(0, L, 1000)

# Calculate corresponding y values using the function
y_values = beam_equation(x_values, w0, E, I, L)

# Find the minimum point (maximum deflection)
min_index = np.argmin(y_values)
max_deflection = y_values[min_index]
x_max_deflection = x_values[min_index]

# Plotting the function with the maximum deflection point
plt.plot(x_values, y_values, label='Beam Equation')
plt.scatter(x_max_deflection, max_deflection, color='red', label=f'Max Deflection\n({x_max_deflection:.2f}, {max_deflection:.2f})')
plt.title('Beam Equation Plot with Max Deflection Point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Output the maximum deflection and x point
print(f'Maximum Beam Deflection: {max_deflection:.2f} at x = {x_max_deflection:.2f}')

#find the max deflection using an optimisation technique
print('\n------ Q1. b)------\n')
from scipy.optimize import minimize

# Objective function to minimize (negative of the beam equation to find the maximum)
objective_function = lambda x: beam_equation(x, w0, E, I, L)

# Initial guess for the minimum point
initial_guess = L / 2

# Use scipy.optimize.minimize to find the minimum (maximum of the negative)
result = minimize(objective_function, initial_guess, bounds=[(0, L)])

# Extract the x-coordinate and corresponding deflection from the result
x_max_deflection = result.x[0]
print ('using an optimization technique x = ', x_max_deflection)


# write taylor series expansion of the function with perturbation
print('\n------ Q1. c)------\n')
import sympy as sym

# Define the variables
x = sym.Symbol('x')

# Define the function y(x) as exp(-x) and add the perturbation h
y = sym.exp(-x + 0.1) 

#solve the epansion of y func w.r.t x for 3 terms and print
taylor = y.series(x, n=3)
print('taylor series of s(x): ', taylor)


#use a function to calc the change in f(x) and sensitivity for the given perturbation
print('\n------ Q1. d)------\n')

import numpy as np
from scipy.misc import derivative

# Given function
def f(x):
    return np.exp(-x)

# Initial value of x and perturbation h
x_initial = 1.0
h = 0.1

# Calculate sensitivity using the the scipy derivative function
sensitivity = derivative(f, x_initial, dx=h, n=1, order=3)

# Taylor series expansion with initial values
taylor_expansion = f(x_initial) + derivative(f, x_initial, dx=h, n=1, order=3) * (x_initial - 1)

# Calculate change in the function value
delta_f = f(x_initial + h) - f(x_initial)

# Print results
print(f"Sensitivity: {sensitivity:.6f}")
print(f"Taylor Series Expansion: {taylor_expansion:.6f}")
print(f"Change in f(x): {delta_f:.6f}")

#------------------------------------------------------------------------------
#                                 Q2 
# calculate the inerest rate using a given equation
print('\n------ Q2. a)------\n')
from scipy.optimize import newton

# Given values 
present_worth = 25000
annual_payments = 5500
number_of_years = 6

# Define the equation to find the interest rate, make it = 0
equation = lambda i: present_worth * (i * (1 + i)**number_of_years) / ((1 + i)**number_of_years - 1) - annual_payments

# Use Newton-Raphson method to find the root (interest rate in % )
interest_rate = newton(equation, x0=0.05) * 100  # Provide an initial guess (e.g., 0.05)

# Display the calculated interest rate
print(f"The interest rate is approximately: {interest_rate:.6f} %")

#find the displacement of the rocket after 30s using a given eq
print('\n------ Q2. b)------\n')
import numpy as np

#using simpsons rule from lecure
def simps(f, a, b, N):

    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    S = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S

# given constants
u = 1.8 * (10**3)
m0 = 160 * (10**3)
q = 2.5 * (10**3)

#define the equation tht needs to be integrated (sub for x)
f = lambda x: u * np.log( m0 / (m0 - q * x))

#integrate f between 0 and 3 for N = 100
numerical_integration_result = simps(f, 0, 30, 100)
print(f"The distance traveled by the rocket is: {numerical_integration_result:.2f} m")

#------------------------------------------------------------------------------
#                                 Q3 
#find how much volume of soil has to be removed using optimisation
print('\n------ Q3. a,b,c)------\n')

import numpy as np
from scipy import integrate, optimize

# Given parameters in m
c1 = 30
c2 = 5
L = 1000

# Define Zh and Zr functions for hill and road resp
Zh = lambda x: c1 * (1 - (np.abs(x) / L)**2) + c2 * (1 - (np.abs(x) / L)**4)

# b is gradient and therefore is a function of a and L
Zr = lambda x, a: a + (a / L) * np.abs(x)

# Function to integrate from -L to L where zh meets zr
objective_function = lambda a: integrate.quad(lambda x: np.abs(Zh(x) - Zr(x, a)), -L, L)[0]

# Initial guess for 'a'
initial_a = 20

# Minimize the objective function to find the minimum volume
result = optimize.minimize(objective_function, initial_a)

# Extract the optimized value of 'a', b found from inspection of graqph
optimized_a = result.x[0]
optimized_b = - (optimized_a / L)

# Calculate the integration result for the optimized values
integration_result = integrate.quad(lambda x: np.abs(Zh(x) - Zr(x, optimized_a)), -L, L)[0]

print("Optimized 'a':", optimized_a)
print("Optimized 'b':", optimized_b)
print("volume of soil to be removed:", integration_result)
