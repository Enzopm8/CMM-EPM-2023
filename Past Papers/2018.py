# December 2018 Past Paper
#------------------------------------------------------------------------------
#                                 Q1 
# optimize for 2 values given initial conditions and one equation
print('\n------ Q1. a)------\n')

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Constants given in the eq
w_cost = 0.7       # $/kg
d_cost = 0.9       # $/m
E = 200 * (10**9)  # Pa
H = 2.75           # m
rho = 7800         # kg/m^3 
P = 20 * (10**3)   # N
d_range = [1, 10]  # cm
t_range = [0.1, 1] # cm
pi = 3.14159

# Equations defining the mechanical system
def EqA(pi, E, I, H, d, t):
    return -(pi * E * I) / ((H**2) * d * t)  # Negate to maximize

def I(pi, d, t):
    return pi * ((d + t)**4 - (d**4)) / 64    #find the MOI of the pipe

# Objective function 
def objective(x):
    d, t = x      #now x[0] is d and x[1] is t
    return EqA(pi, E, I(pi, d, t), H, d, t)    #remember I is a function that needs parameters to be called

# Constraints, type eq specifies that the constraint is an equality constraint
# these constraints ensure that the solution satisfies the specified conditions
constraints = (
    {'type': 'eq', 'fun': lambda x: EqA(pi, E, I(pi, x[0], x[1]), H, x[0], x[1])},  # Equation A replacing d and t for their x
                )

# Initial guess, around half the range
initial_guess = [5, 0.5]

# Bounds for (d, t) provided by the question
bounds = [(1, 10), (0.1, 1)]

# Perform optimization to maximize EqA, -ve minimization = maximization
result = minimize(objective, initial_guess, bounds=bounds, constraints=constraints)

# Extract the optimal values
maximal_d, maximal_t = result.x

# Calculate 80% of the maximized buckling stress, negative because we modified the function to maximize but now we want to mimimize
target_stress = -0.8 * EqA(pi, E, I(pi, maximal_d, maximal_t), H, maximal_d, maximal_t)

# Objective function for 80% of maximized buckling stress
def stress_objective(x):
    d, t = x
    return EqA(pi, E, I(pi, d, t), H, d, t) - target_stress

# Perform optimization to find d and t for 80% of maximized buckling stress
result_stress = minimize(stress_objective, initial_guess, bounds=bounds, constraints=constraints)

# Extract the values for 80% of maximized buckling stress
target_d, target_t = result_stress.x

#create functions to calculate density and volume
V = lambda R, r, H: pi * (R**2 - r**2) * H
w = lambda rho, V: rho * V

# Calculate cost based on the given parameters
R_optimal = (target_d / 2) + target_t
r_optimal = target_d / 2
V_optimal = V(R_optimal, r_optimal, H)
w_optimal = w(rho, V_optimal)
cost = w_optimal * w_cost + target_d * d_cost

print(f"Maximized values: d = {maximal_d} cm, t = {maximal_t} cm")
print(f"For 80% of maximized buckling stress: d = {target_d} cm, t = {target_t} cm")
print(f"Optimal cost: ${cost}")


print('\n------ Q1. b)------\n')
# write the taylor series expansion of ln(1+x) for 3 terms
import sympy as sym

# Define the vars
x = sym.Symbol('x')

# Define the function y(x)
y = sym.ln( 1 + x )

#solve the epansion of y func w.r.t x for 3 terms and print
taylor = y.series(x, n=3)
print('taylor series of s(x): ', taylor)

print('\n------ Q1. c)------\n')
#calculate the value of y for 7 sig. fig when x=0.1

expr = round ( (y.subs({x:0.1})), 7) 

print ('At x=0.1, f(x) = ', expr)

#------------------------------------------------------------------------------
#                                 Q2 
print('\n------ Q2. a)------\n')
#Prove that C is the general solution to B
import sympy as sym

# Define the variables
x, y, w, TA, y0 = sym.symbols('x y w TA y0')

# Define the equation C
C = (TA / w) * sym.cosh((w / TA) * x) + y0 - (TA / w)

# Differentiate equation_C with respect to x
dydx = sym.diff(C, x)

# Calculate the second derivative
d2yd2x = sym.diff(dydx, x)

# Express cosh in terms of sinh
d2yd2x_sub = d2yd2x.subs(sym.cosh(w / TA * x), sym.sqrt(1 + sym.sinh(w / TA * x)**2))

# Define the RHS of Equation B
B = (w / TA) * sym.sqrt(1 + (dydx**2))

# Display the results
print("Equation C:")
print(C)
print("\n1st Derivative of Equation C with respect to x:")
print(dydx)
print("\n2nd Derivative of Equation C with respect to x:")
print(d2yd2x_sub)
print("\nRight-hand side of Equation B:")
print(B)

# Simplify the expressions for comparison
d2yd2x_simp = sym.simplify(d2yd2x_sub)
B_simp = sym.simplify(B)

# Check if the second derrivative of C is equal to the RHS of B
is_equal = sym.simplify(d2yd2x_simp - B_simp) == 0

print("\nIs Equation C the general solution to Equation B?")
print(is_equal)


print('\n------ Q2. b)------\n')
#use a root finding techique to calc tension with initial conditions
import math

def bisection(f, a, b, N):

    if f(a) * f(b) >= 0:
        print("Initial values 'a' and 'b' must have opposite signs.")
        return None

    a_n = a
    b_n = b

    for n in range(1, N + 1):
        m_n = (a_n + b_n) / 2
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
            print("Bisection method fails.")
            return None

    return (a_n + b_n) / 2

# constants provided in the question
y = 15
x = 50
y0 = 5
w = 10

#function set to = 0 so we can find the root
f = lambda TA: (TA / w) * math.cosh((w / TA) * x) + y0 - (TA / w) - y

# Attempt to find the root using the bisection method
# guesses were found using desmos
TA = bisection(f, 1250, 1300, 100)
print("Approximate Tension:", TA)


print('\n------ Q2. c)------\n')
# use fixed point iteration to determine the porosity using a given eq
# Importing math to use sqrt function
import math

# Input Section
x0 = 0.38  # Initial guess
e = 0.001  # Tolerable error
N = 20  # Maximum iterations
scale_factor = 0.01  # Scaling factor to reduce step size

# Converting x0, e, and scale_factor to float
x0 = float(x0)
e = float(e)
scale_factor = float(scale_factor)

# Define the function f(x) to find its root
def f(x):
    return 200 * (x**3) - 3 * (-x + 1)**2 - 17.5 * (-x + 1)

# Re-writing f(x) = 0 to x = g(x)
def g(x):
    return ((20 * x**3) / (1 - x) - 2.05) / (-3/10)

# Implementing Modified Fixed Point Iteration Method with smaller step sizes
def modifiedFixedPointIteration(x0, e, N, scale_factor):
    print('*** MODIFIED FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    
    while condition:
        x1 = g(x0)
        '''
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        '''
        x0 = x0 + scale_factor * (x1 - x0)  # Introduce scaling factor to reduce step size
        step = step + 1
        
        if step > N or x1 < 0:  # Added condition to stop if x becomes negative
            flag = 0
            break
        
        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Starting Modified Fixed Point Iteration Method with smaller step sizes
modifiedFixedPointIteration(x0, e, N, scale_factor)

#------------------------------------------------------------------------------
#                                 Q3 
print('\n------ Q3. a)------\n')
#factorise a second order poly and find the roots

x = sym.Symbol('x')
y = x**2 + 10*x + 25
factors = y.factor()
print('the factorisation is:', factors)
roots = sym.solve(factors, x)
print ('the roots therefore are x =', roots)

print('\n------ Q3. b)------\n')
#use poly deflation to find the roots of a 4th order poly

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
f = lambda x: x**4 + 5*(x**3) + 15*(x**2) + 3*x -10

#the number of real solutions was found 1st by using desmos / wolfram and then the boundaries were adjusted

# Find and print the solution using the Secant method CHANGE
solution1 = secant(f, -2, 0, 1000)
print('the first root of x is:', solution1)

solution2 = secant(f, 0, 1, 1000)
print('the second root of x is:', solution2)
