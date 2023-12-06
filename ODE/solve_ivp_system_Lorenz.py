# Recommended Usage:
# This code is recommended for solving and visualizing solutions 
# of systems of ordinary differential equations (ODEs) using the 
# solve_ivp method. It's suitable for dynamical systems described 
# by ODEs, especially those exhibiting chaotic behavior.

# Not Recommended:
# This code might not be suitable for extremely stiff ODEs or 
# systems with discontinuities. For such cases, consider using 
# specialized methods or adjusting solver parameters.

# ------------------------------------------------------
# Importing necessary modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ------------------------------------------------------
# Define the system of ODEs
def model(x, y):
    # System parameters
    sigma = 10.0
    beta = 8.0 / 3.0
    rho = 28.0
    
    # Variables
    y_1, y_2, y_3 = y
    
    # ODEs
    f_1 = sigma * (y_2 - y_1)
    f_2 = rho * y_1 - y_2 - y_1 * y_3
    f_3 = -beta * y_3 + y_1 * y_2
    
    return [f_1, f_2, f_3]

# ------------------------------------------------------
# Set initial conditions and solution interval
x0 = 0
y0 = [5, 5, 5]  # Initial values for y_1, y_2, y_3
t_final = 30

# ------------------------------------------------------
# Apply solve_ivp method to solve the ODEs
t_eval = np.linspace(0, t_final, num=5000)
y = solve_ivp(model, [0, t_final], y0, t_eval=t_eval)

# ------------------------------------------------------
# Plot the results

# Plot y_1, y_2, y_3 as functions of time
plt.figure(1)
plt.plot(y.t, y.y[0, :], 'b-', label='y_1')
plt.plot(y.t, y.y[1, :], 'r-', label='y_2')
plt.plot(y.t, y.y[2, :], 'g-', label='y_3')
plt.xlabel('Time (t)')
plt.ylabel('Values')
plt.legend()

# Plot y_2 as a function of y_1
plt.figure(2)
plt.plot(y.y[0, :], y.y[1, :], '-')
plt.xlabel('y_1')
plt.ylabel('y_2')

# Plot y_3 as a function of y_1
plt.figure(3)
plt.plot(y.y[0, :], y.y[2, :], '-')
plt.xlabel('y_1')
plt.ylabel('y_3')

# ------------------------------------------------------
'''
# print results in a text file (for later use if needed)
file_name= 'output.dat' 
f_io = open(file_name,'w') 
n_step = len(y.t)
for i in range(n_step):
    s1 = str(i)
    s2 = str(y.t[i])
    s3 = str(y.y[0,i])
    s4 = str(y.y[1,i])
    s5 = str(y.y[2,i])
    s_tot = s1 + ' ' + s2 + ' ' + s3  + ' ' + s4 + ' ' + s5
    f_io.write(s_tot + '\n')
f_io.close()

# ------------------------------------------------------
# Print the results directly in the kernel

# Print header
print(f"{'Index': <6} {'Time (t)': <12} {'y_1': <12} {'y_2': <12} {'y_3': <12}")
print("=" * 56)  # Separator line

# Print data
for i, (t_i, y_1_i, y_2_i, y_3_i) in enumerate(zip(y.t, y.y[0, :], y.y[1, :], y.y[2, :])):
    print(f"{i: <6} {t_i: <12.4f} {y_1_i: <12.4f} {y_2_i: <12.4f} {y_3_i: <12.4f}")
'''
#--------------------------------------------
plt.show()
# ------------------------------------------------------
