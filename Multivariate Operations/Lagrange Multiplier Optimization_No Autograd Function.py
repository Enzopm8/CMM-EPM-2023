# -*- coding: utf-8 -*-
"""
Created on Sat Nov 7 12:25:44 2020

@author: emc1977
"""

import numpy as np
from scipy.optimize import minimize

# This code uses the scipy minimize function to optimize an objective function
# under a constraint defined by the equation '2 * x - y + z - 3 = 0'.
# The objective function is the sum of squares of x, y, and z.

# Objective function without any constraints inserted yet.
# Function F below combines this objective function with the constraint in eq
# to form an Augmented Lagrange Function.
def objective(X):
    x, y, z = X
    return x ** 2 + y ** 2 + z ** 2

# Constraint function with lambda as a coefficient.
def eq(X):
    x, y, z = X
    return 2 * x - y + z - 3

# Use the minimize function to find the solution
sol = minimize(objective, [1, 4, 5], constraints={'type': 'eq', 'fun': eq})

# Print the optimized results and related information
print(f"Optimization Success: {sol.success}")
print(f"Number of Iterations: {sol.nit}")
print("\nOptimization Results:")
print(f"Optimized values (x, y, z): {sol.x}")
print(f"Optimized Objective Function Value: {sol.fun}")
print(f"Constraint Value at Optimized Solution: {eq(sol.x)}")

