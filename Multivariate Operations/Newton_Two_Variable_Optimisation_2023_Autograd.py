# Summary: Optimization Script
# This script defines an objective function and a constraint function. 
# It uses the Augmented Lagrange function to optimize the objective 
# function under the given constraint using the fsolve function.

from autograd import grad

# Objective function
def objective(X):
    # The objective function is a product of powers of its variables.
    x, y = X
    return (160*x**0.66)*(y**0.33)

# Constraint function
def eq(X):
    # This is the constraint function that has lambda as a coefficient.
    x, y = X
    return 20*x + 0.15*y - 20000.

# Augmented Lagrange function
def F(L):
    # The augmented Lagrange function combines the objective and 
    # constraint functions with a Lagrange multiplier.
    x, y, _lambda = L
    return objective([x, y]) + _lambda * eq([x, y])

# Gradients of the Lagrange function
dfdL = grad(F, 0)

# Find L that returns all zeros in this function.
def obj(L):
    # The objective here is to find the roots of the Lagrange gradients,
    # representing the optimal values of x, y, and lambda.
    x, y, _lambda = L
    dFdx, dFdy, dFdlam = dfdL(L)
    return [dFdx, dFdy, eq([x, y])]

from scipy.optimize import fsolve

# Solve for the optimal values using fsolve
x, y, _lam = fsolve(obj, [1., 1., 1.0])
print(f'The answer is at {x, y}')
