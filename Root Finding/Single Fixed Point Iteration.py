# Recommendation:
# This code is designed for solving equations using the Fixed Point Iteration method.
# It is recommended for well-behaved functions where convergence is assured and for cases where the derivative
# of the function is challenging or computationally expensive to obtain.

# Not recommended:
# This method may not converge for functions with multiple roots, and the convergence can be slow for certain functions.
# Additionally, it is not suitable for functions with sharp turns or near-vertical slopes where the derivative is close to zero.

# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

# Input Section
x0 = 0
e = 1e-3
N = 1000

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Define the function f(x) to find its root
def f(x):
    return x**2 + 4*x - 12

# Re-writing f(x) = 0 to x = g(x)
def g(x):
    return 0.25 * (12 - x**2)
    
# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

# Note: You can combine the above three sections like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Fixed Point Iteration Method
fixedPointIteration(x0, e, N)
