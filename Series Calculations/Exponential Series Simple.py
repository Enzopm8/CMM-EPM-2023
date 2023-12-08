# Recommendation:
# The code approximates the value of e^x using a Taylor series expansion.
# It demonstrates the iterative process to calculate the exponential function.

# Not recommended:
# The code is suitable for its purpose. However, for more precise results, consider using specialized functions provided by the math module.

# How to modify for a different value of x or more iterations:
# 1. Change the value of 'x' to the desired exponent.
# 2. Adjust the value of 'n' to specify the number of iterations for the Taylor series expansion.

import math

# Set the values for x and n
x = 0.5
n = 5

# Get the exact value using the intrinsic python function
exact_value = math.exp(x)

# Initialize the sum
e_to_x = 0

# Perform the iteration n times (from i=0 to i=n-1)
for i in range(n):
    e_to_x += x**i / math.factorial(i)
    relative_error = (e_to_x - exact_value) / exact_value
    print(f'Iteration {i}: Approximation = {e_to_x:.6f}, Relative Error = {relative_error:.6f}')

# Display the final results
print('\nFinal Results:')
print(f'Numerical Result (Approximation): {e_to_x:.6f}')
print(f'Exact Value: {exact_value:.6f}')
print(f'True Relative Error: {relative_error:.6f}')
