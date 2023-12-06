# Tutorial 9
#------------------------------------------------------------------------------
import numpy as np

def f(x):
    return x**2 + 4*x - 12

N_values = np.arange(10, 1000, 10) 

# Define the integration limits
a = -10
b = 10
#------------------------------------------------------------------------------
# Exerise 1

import matplotlib.pyplot as plt

def calculate_dx(a, b, n):
    return (b - a) / float(n)

def rect_rule(f, a, b, n):
    total = 0.0
    dx = calculate_dx(a, b, n)

    for k in range(0, n):
        total = total + f((a + (k * dx)))

    return dx * total

# Example usage:
result_rect = rect_rule(f, a, b, 1000)
print(f"The rectangular approximation of the integral is: {result_rect:.6f}")

#------------------------------------------------------------------------------
# Exercise 2

def trapz(f, a, b, N):
    x = np.linspace(a, b, N+1)
    y = f(x)
    y_right = y[1:]
    y_left = y[:-1]
    dx = (b - a) / N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

# Execute the Trapezoid Rule
result_trapz = trapz(f, a, b, 1000)

# Print the result
print(f"The trapezoid integration result is: {result_trapz:.6f}")

#------------------------------------------------------------------------------
# Exercise 3

import numpy as np

def simps(f, a, b, N):

    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    S = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S

result_simps1 = simps(f, a, b, 1000)
print(f"The Simpsons 1/3 integration result is: {result_simps1:.6f}")
    
#------------------------------------------------------------------------------
# Exercise 4

import numpy as np

# Function to perform calculations 
def calculate(lower_limit, upper_limit, interval_limit): 

    interval_size = (float(upper_limit - lower_limit) / interval_limit) 
    sum = f(lower_limit) + f(upper_limit)

    # Calculates value till integral limit 
    for i in range(1, interval_limit): 
        if (i % 3 == 0): 
            sum = sum + 2 * f(lower_limit + i * interval_size) 
        else: 
            sum = sum + 3 * f(lower_limit + i * interval_size) 

    return ((float(3 * interval_size) / 8) * sum) 


#Calculate for a set N
result_simps3 = calculate(a, b, 1000)

# Rounding the final answer to 6 decimal places  
print(f"The Simpsons 3/8 integration result is: {round(result_simps3, 6)}")
    
#------------------------------------------------------------------------------
# Exercise 5
exact_sol = 1280/3

error_rect = (result_rect-exact_sol) / exact_sol
error_trap = (result_trapz-exact_sol) / exact_sol
error_simps1 = (result_simps1 - exact_sol) / exact_sol
error_simps3 = (result_simps3 - exact_sol) / exact_sol

print ('Rect error', error_rect)
print ('trapz Error:', error_trap)
print ('Simpsons 1/3 error:', error_simps1)
print ('Simpsons 3/8 error:', error_simps3)


integral_values_rect = []
integral_values_trapezoid = []
integral_values_simpsons1 = []
integral_values_simpsons3 = []

for N in N_values:
    result_rect = rect_rule(f, a, b, N)
    integral_values_rect.append(result_rect)
    
    result_trapezoid = trapz(f, a, b, N)
    integral_values_trapezoid.append(result_trapezoid)
    
    result_simpsons1 = simps(f, a, b, N)
    integral_values_simpsons1.append(result_simpsons1)
    
    result_simpsons3 = calculate(a, b, N)
    integral_values_simpsons3.append(result_simpsons3)

# Plotting
plt.plot(N_values, integral_values_rect, label='Rectangular Rule')
plt.plot(N_values, integral_values_trapezoid, label='Trapezoid Rule')
plt.plot(N_values, integral_values_simpsons1, label='Simpson 1/3')
plt.plot(N_values, integral_values_simpsons3, label='Simpson 3/8')
plt.xlabel('Number of Intervals (N)')
plt.ylabel('Integral Value')
plt.title('Evolution of Integral Value with Number of Intervals')
plt.legend()
plt.show()

