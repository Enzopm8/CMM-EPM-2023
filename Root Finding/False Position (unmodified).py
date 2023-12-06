# Recommendation:
# This code implements the False Position (Regula Falsi) method for solving equations.
# While the method is valid, it is often outperformed by the more robust and efficient methods like Newton-Raphson or the Secant method.

# Not recommended:
# False Position method may not be the most efficient choice for solving equations due to its slow convergence in some cases.

# How to modify for a different function or interval:
# 1. Define a new function 'func(x)' based on the equation you want to solve.
# 2. Adjust the initial values 'a' and 'b' to set the interval in which you want to search for a solution.

# Python3 implementation of False Position 
# Method for solving equations

MAX_ITER = 1000000

# An example function whose solution 
# is determined using False Position Method.  
# The function is x**2 + 4*x - 19 
def func(x): 
    return x**2 + 4*x - 19

# Prints the root of func(x) in the interval [a, b] 
def regulaFalsi(a, b): 
    # Check if the initial values have the same sign
    if func(a) * func(b) >= 0: 
        print("Initial values 'a' and 'b' must have opposite signs.") 
        return -1
      
    c = a  # Initialize the result 
      
    for i in range(MAX_ITER): 
        # Find the point that touches the x-axis 
        c = (a * func(b) - b * func(a)) / (func(b) - func(a)) 
          
        # Check if the above found point is a root 
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c 

    print("The value of the root is: {:.4f}".format(c)) 
    print("Number of iterations:", i)

# Driver code to test the function 
# Initial values assumed 
a = -6
b = 6
regulaFalsi(a, b) 
