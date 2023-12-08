#------------------------------------------------------------------------------
#                         Ex 1: Find sum of 1st 20 odd numbers

# Recommendation:
# The code calculates the sum of the squares of the first n odd natural numbers.
# It uses a loop to iterate through the odd numbers and accumulate their squares.

# Not recommended:
# The code is straightforward for its purpose. However, for better efficiency, consider using a formula to directly compute the sum.

# How to modify for a different value of n:
# Change the value of 'n' to the desired number of odd natural numbers.

# Improved code with informative output:

# Function that returns the sum of the squares of the first n odd natural numbers
def squaresum_odd(n):
    # Initialize the sum to 0
    sum_odd_squares = 0
    # Iterate i from 1 to n, checking if i is odd before adding its square to the sum
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if i is odd
            sum_odd_squares += i * i  # Calculate the square of i and add it to the sum
    return sum_odd_squares

# Main Program
# Specify the number of odd natural numbers, n
n = 20
# Call the function squaresum_odd
result = squaresum_odd(n)
# Print the result with informative output
print(f"The sum of the squares of the first {n} odd natural numbers is: {result}")

#------------------------------------------------------------------------------
#        Ex 2: Create a random array of 20 values and print >5 and <6 
import numpy as np

array = np.empty(20)
print (array)

array_new = np.random.randint(0,11,20)
print (array_new)

selected_values = array_new[(array_new > 5)]
print (selected_values)

#------------------------------------------------------------------------------
#   Ex 3: Create a random array of equispaced coordinates between 0 and 2pi
import matplotlib.pyplot as plt 
 
end = 2 * np.pi
x_values = np.linspace(0, end)
y_values = np.sin(x_values)


# plotting the points  
plt.plot(x_values, y_values) 
  
# naming the x axis 
plt.xlabel('X') 
# naming the y axis 
plt.ylabel('Y') 
  
# giving a title to my graph 
plt.title('Sine Graph') 
  
# function to show the plot 
plt.show() 

#------------------------------------------------------------------------------
#                              Ex 4: truncated  Series
import numpy as np
import matplotlib.pyplot as plt

# Number of iterations
N = 10

# Initialize variables
s = 0
pi_n = np.zeros(N)
nn = np.zeros(N)
error_true = np.zeros(N)
error_ext = np.zeros(N)

# Main loop for computation
for i in range(1, N + 1):
    pi_old = (s * 6.0) ** 0.5
    s = s + 1.0 / i**2.0
    pi_n[i - 1] = (s * 6.0) ** 0.5
    nn[i - 1] = i 
    error_true[i - 1] = np.absolute(pi_n[i - 1] - np.pi)
    error_ext[i - 1]  = np.absolute(pi_n[i - 1] - pi_old) 
    
    # Output results for each iteration
    print(f"Iteration {i}: Approximation = {pi_n[i - 1]}, True Error = {error_true[i - 1]}, Extrapolation Error = {error_ext[i - 1]}")

# Plotting
plt.figure()
plt.plot(nn, pi_n)
plt.title("Approximation of π over Iterations")
plt.xlabel("Number of Iterations")
plt.ylabel("Approximated π")

plt.figure()
plt.loglog(nn, error_true, '-b', label='True Error')
plt.loglog(nn, error_ext, '.r', label='Extrapolation Error')
plt.title("Error Analysis")
plt.xlabel("Number of Iterations (log scale)")
plt.ylabel("Error (log scale)")
plt.legend()

plt.show()

