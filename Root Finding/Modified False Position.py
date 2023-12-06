# Recommendation:
# This code is designed for finding roots of equations using the Regula Falsi (False Position) method.
# It is recommended for functions where convergence is assured and the root is expected to be found within a reasonable number of iterations.

# Not recommended:
# The Regula Falsi method may not converge for functions with multiple roots, and it might not be as efficient for well-behaved functions with simple roots.
# Additionally, it may not work well for functions with sharp turns or near-vertical slopes.

# How to modify for a different function:
# 1. Define the new function func(x): Replace the existing function 'func' with the one corresponding to the new function.
# 2. Adjust the initial guesses ('a', 'b'): Set appropriate initial values based on the characteristics of the new function.
# 3. Modify the maximum number of iterations: Adjust 'MAX_ITER' based on the desired level of accuracy and computational resources.


MAX_ITER = 1000000

# An example function whose solution 
# is determined using Regula Falsi Method.  
# The function is x^3 - x^2 + 2 
def func(x): 
    return (x**2 + 4*x - 19) 

# Prints root of func(x) in interval [a, b] 
def regulaFalsi(a, b): 
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
      
    c = a  # Initialize result 
      
    for i in range(MAX_ITER): 
          
        # Find the point that touches x-axis 
        c = (a * 0.5*func(b) - b * func(a))/ (0.5*func(b) - func(a)) 
          
        # Check if the above-found point is the root 
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c 
    print("The value of root is:", '%.4f' % c) 
    print("Number of iterations:", i)
  
# Driver code to test above function 
# Initial values assumed 
a = -6
b = 6
regulaFalsi(a, b) 

