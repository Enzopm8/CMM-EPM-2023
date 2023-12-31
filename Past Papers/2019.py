# December 2019 Past Paper
#------------------------------------------------------------------------------
#                                 Q1 
print('\n------ Q1. a)------\n')
#find the 2 real and imaginary roots of w given initial conditions
import numpy as np

def find_roots(coefficients):
    # Find roots using NumPy's roots function
    roots = np.roots(coefficients)
    
    # Separate real and complex roots
    real_roots = roots[np.isreal(roots)].real
    complex_roots = roots[np.iscomplex(roots)].real
    complex_roots_imag = roots[np.iscomplex(roots)].imag
    
    # Print the polynomial equation
    print("Polynomial Equation:")
    equation_str = " + ".join([f"{coeff}w^{power}" if power > 0 else f"{coeff}" for power, coeff in enumerate(coefficients[::-1]) if coeff != 0])
    print(f"P(x) = {equation_str}\n")
    
    # Print the roots
    print("Roots:")
    for i, root in enumerate(real_roots):
        print(f"{i + 1}st Root: {root}")
    
    for i, (real, imag) in enumerate(zip(complex_roots, complex_roots_imag)):
        print(f"{i + 1}st Root: {real} + {imag}i")
        print(f"{i + 2}nd Root: {real} - {imag}i")
        # Incrementing i by 1 again to skip the next iteration
        i += 1

# Define coefficients of the polynomial in descending order of power of x 
s = 1500
c = 12
coefficients = [1, 2*c, 3*s,  s*c, s**2] 

#call the function
find_roots(coefficients)


print('\n------ Q1. b)------\n')
#calc the smallest possible ammount of work in 10s 
#using the smallest values from the previous answer
w_i = 24.0302414149468
w_r = 0.623019628307849
t = 10
A = 0.1
gamma = np.pi/8

#define the function for displacement
x = A*np.exp(w_r*t)*np.cos(w_i*t+gamma)
print ('displacement: ', x)

#find the force using the displacement
T = 1000
f = -x * T
print ('force:', f)

#------------------------------------------------------------------------------
#                                 Q2 
print('\n------ Q2. a,b)------\n')
# minimize the the integral and output one var, us ehtat var to find the root
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad

# Define the objective function using quad for numerical integration
def objective_function(p):
    integrand = lambda x: np.sin(x) * np.cos(p * x)
    integration_result, _ = quad(integrand, 0, np.pi)
    return integration_result

# Use the minimize function to find the solution
result = minimize(objective_function, x0=0.0001)

# Print the optimized results and related information
print(f"Optimization Success: {result.success}")
print(f"Number of Iterations: {result.nit}")
print("\nOptimization Results:")
print(f"Optimized p value: {result.x[0]}")
print(f"Optimized Objective Function Value: {result.fun}")

#------------------------------------------------------------------------------
#                                 Q3 
print('\n------ Q3. a)------\n')
# find the 2 lowest values for the var which satisfy the eq given
import math
import numpy as np

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
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None

    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))

# Define the function f(x) CHANGE
f = lambda x: np.cosh(x) * np.cos(x) + 1

# Find and print the solution using the Secant method CHANGE
#boundaries found using desmos or wolfram
solution1 = secant(f, 1, 2, 1000)
print('the first root of B is:', solution1)

solution2 = secant(f, 4, 5, 1000)
print('the second root of B is:', solution2)

#coefficients given in the question
m = 7850
L = 0.9
E = 200 * (10**9)
I = 3.255 * (10**-11)
B1 = solution1
B2 = solution2

# solved for f by manual re-arranging the equation given
f1 = ((((solution1**4) * E * I) / (m * (L**3)))**0.5) / (2 * np.pi)
f2 = ((((solution2**4) * E * I) / (m * (L**3)))**0.5) / (2 * np.pi)
print ('1st solution: ', f1)
print ('2nd solution: ', f2)

#------------------------------------------------------------------------------
#                                 Q4
print('\n------ Q4------\n')
# find the smallest radius of the satelite 
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# Given polar coordinates (r, theta)
r_values = np.array([6870, 6728, 6615])
theta_values = np.radians(np.array([-30, 0, 30]))

# Given equations in polar form
equations = lambda x: [
    (x[0] / (1 + x[1] * np.sin(theta + x[2])))-r
    for r, theta in zip(r_values, theta_values)
    ]

# Adjusted initial guess for C, E, and a
initial_guess = [6800, 0.02, 0.2]  # Adjusted E to have a negative sign

# Solve the system of equations
constants = fsolve(equations, initial_guess, maxfev=2000, full_output=True)

# Extracting C, E, and a
C, E, a = constants[0]
theta = np.radians(30)
R = C / (1 + E * np.sin(theta + a))

# Display the results
print(f"Constant C: {C}")
print(f"Constant E: {E}")
print(f"Constant a: {a}")

#Add sicpy optmize (minimize) to find minimum R with these coefficients because its a fucking ellipse

# Function to calculate radius for a given angle
def calculate_radius(theta):
    return C / (1 + E * np.sin(theta + a))

# Finding the minimum radius
theta_values = np.linspace(-np.pi, np.pi, 1000)
min_radius_index = np.argmin([calculate_radius(theta) for theta in theta_values])
min_radius = calculate_radius(theta_values[min_radius_index])

print(f"The minimum radius R is: {min_radius}")

#------------------------------------------------------------------------------
#                                 Q4
print('\n------ Q5------\n')
#find the value of the 3 angles that minimise PE in the system whilst satisfying the constraints

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Constants
L1 = 1.2  # Length of link 1 (meters)
L2 = 1.5  # Length of link 2 (meters)
L3 = 1    # Length of link 3 (meters)
B = 3.5   # Horizontal position constraint (meters)
H = 0     # Vertical position constraint (meters)
W1 = 20 * (10**3)  # Weight applied at joint 1 (Newtons)
W2 = 30 * (10**3)  # Weight applied at joint 2 (Newtons)

# Equations defining the mechanical system
def Eq6(W1, L1, theta1, W2, L2, theta2):
    return -W1 * L1 * np.sin(theta1) - W2 * (L1 * np.sin(theta1) + L2 * np.sin(theta2))

def Eq7a(L1, theta1, L2, theta2, L3, theta3):
    return L1 * np.cos(theta1) + L2 * np.cos(theta2) + L3 * np.cos(theta3)

def Eq7b(L1, theta1, L2, theta2, L3, theta3):
    return L1 * np.sin(theta1) + L2 * np.sin(theta2) + L3 * np.sin(theta3)

# Objective function (minimize Eq6)
def objective(theta):
    theta1, theta2, theta3 = theta
    return Eq6(W1, L1, theta1, W2, L2, theta2)

# Constraints, type eq specifies that the constraint is an equality constraint
# these constraints ensure that the solution (optimized angles) satisfy the specified conditions
constraints = (
    {'type': 'eq', 'fun': lambda theta: Eq7b(L1, theta[0], L2, theta[1], L3, theta[2]) - H},  # Equation 7b = H
    {'type': 'eq', 'fun': lambda theta: Eq7a(L1, theta[0], L2, theta[1], L3, theta[2]) - B}   # Equation 7a = B
                )

# Initial guess in radians
initial_guess = [0.8, 0.5, 0.07]

# Bounds for angles (theta1, theta2, theta3) - ensuring non-negativity
bounds = [(0, None), (0, None), (0, None)]

# Optimization with bounds
result = minimize(objective, initial_guess, constraints=constraints, bounds=bounds)

# Extracting the optimized values into a theta array that is later called
theta_optimized = result.x

# Displaying the results with units
print("Optimized values for angles:")
print(f"Theta 1: {theta_optimized[0]:.2f} radians")
print(f"Theta 2: {theta_optimized[1]:.2f} radians")
print(f"Theta 3: {theta_optimized[2]:.2f} radians")

#assigning values for theta (so its not an array)
theta1_opt, theta2_opt, theta3_opt = result.x

PE = Eq6(W1, L1, theta1_opt, W2, L2, theta2_opt) * (-1) # TO MAKE IT NON NEGATIVE
print(f'The absolute potential energy of the system is {round(abs(PE), 2)} J')
# Function to calculate positions of joints using simple geometry
def calculate_positions(theta1, theta2, theta3):
    x1, y1 = 0, 0
    x2, y2 = L1 * np.cos(theta1), L1 * np.sin(theta1)
    x3, y3 = x2 + L2 * np.cos(theta2), y2 + L2 * np.sin(theta2)
    x4, y4 = x3 + L3 * np.cos(theta3), y3 + L3 * np.sin(theta3)
    return x1, y1, x2, y2, x3, y3, x4, y4

# Calculate positions using the opimized angles 
x1, y1, x2, y2, x3, y3, x4, y4 = calculate_positions(theta1_opt, theta2_opt, theta3_opt)

# Plotting the system
plt.figure(figsize=(8, 6))
plt.scatter([0, x2, x3], [0, y2, y3], color='r', label='Joints')
plt.plot([x1, x2, x3, x4], [y1, y2, y3, y4], marker='o', linestyle='-', color='b', label='Optimized Configuration')
plt.title('Mechanical System Visualization')
plt.xlabel('X-axis (meters)')
plt.ylabel('Y-axis (meters)')
plt.legend()
plt.grid(True)
plt.show()
