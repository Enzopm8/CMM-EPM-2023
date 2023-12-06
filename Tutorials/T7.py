# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math


# ------------------------------------------------------
# functions that returns dy/dx
# i.e. the equation we want to solve
def model(y,x):
    dydx = y*(1.0-y)
    return dydx
# ------------------------------------------------------

# ------------------------------------------------------
# inputs
# initial conditions
x0 = 0
y0 = math.exp(-4)/(math.exp(-4) + 1)
# total solution interval
x_final = 10
# ------------------------------------------------------

h_values = np.array([0.1, 0.5, 1, 1.5, 2])
RMQE_eul = np.zeros(len(h_values))
RMQE_rk  = np.zeros(len(h_values))

for hh in range(0,len(h_values)):

         # ------------------------------------------------------
         # step size
         h = h_values[hh]
         # number of steps
         n_step = math.ceil(x_final/h)
         # ------------------------------------------------------
         
         # ------------------------------------------------------
         # Euler method
         
         # Definition of arrays to store the solution
         x_eul = np.zeros(n_step+1)
         y_eul = np.zeros(n_step+1)
         e_eul = np.zeros(n_step+1)
         
         # Initialize first element of solution arrays 
         # with initial condition
         y_eul[0] = y0
         x_eul[0] = x0 
         
         # Populate the x array
         for i in range(n_step):
             x_eul[i+1]  = x_eul[i]  + h
         
         # Apply Euler method n_step times
         for i in range(n_step):
             # compute the slope using the differential equation
             slope = model(y_eul[i],x_eul[i]) 
             # use the Euler method
             y_eul[i+1] = y_eul[i] + h * slope 
         # ------------------------------------------------------
         
         
         # ------------------------------------------------------
         # Fourth Order Runge-Kutta method
         
         # Definition of arrays to store the solution
         x_rk = np.zeros(n_step+1)
         y_rk = np.zeros(n_step+1)
         e_rk = np.zeros(n_step+1)
         
         # Initialize first element of solution arrays 
         # with initial condition
         y_rk[0] = y0
         x_rk[0] = x0 
         
         # Populate the x array
         for i in range(n_step):
             x_rk[i+1]  = x_rk[i]  + h
         
         # Apply RK method n_step times
         for i in range(n_step):
            
             # Compute the four slopes
             x_dummy = x_rk[i]
             y_dummy = y_rk[i]
             k1 =  model(y_dummy,x_dummy)
             
             x_dummy = x_rk[i]+h/2
             y_dummy = y_rk[i] + k1 * h/2
             k2 =  model(y_dummy,x_dummy)
         
             x_dummy = x_rk[i]+h/2
             y_dummy = y_rk[i] + k2 * h/2
             k3 =  model(y_dummy,x_dummy)
         
             x_dummy = x_rk[i]+h
             y_dummy = y_rk[i] + k3 * h
             k4 =  model(y_dummy,x_dummy)
         
             # compute the slope as weighted average of four slopes
             slope = 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4 
         
             # use the RK method
             y_rk[i+1] = y_rk[i] + h * slope  
         # ------------------------------------------------------
         
         
         # ------------------------------------------------------
         # Compute error
         e_eul = y_eul - np.exp(x_eul-4)/(np.exp(x_eul-4) + 1)
         e_rk  = y_rk  - np.exp(x_rk -4)/(np.exp(x_rk -4) + 1)
         
         # Root mean square error
         RMQE_eul[hh] = (np.mean(e_eul**2.0))**0.5
         RMQE_rk[hh]  = (np.mean(e_rk **2.0))**0.5
         # ------------------------------------------------------
         
         # ------------------------------------------------------
         # very refined sampling of the exact solution c*e^(-x)
         # n_exact linearly spaced numbers
         # only needed for plotting exact solution
         
         # Definition of array to store the exact solution
         n_exact = 1000
         x_exact = np.linspace(0,x_final,n_exact+1) 
         y_exact = np.zeros(n_exact+1)
         
         # exact values of the solution
         for i in range(n_exact+1):
             y_exact[i] = math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4) + 1)
         # ------------------------------------------------------
         
         # ------------------------------------------------------
         # plot results in the loop
         plt.figure()
         plt.plot(x_eul, y_eul , 'b.-', label='Eul')
         plt.plot(x_rk, y_rk , 'g*-', label='RK4')
         plt.plot(x_exact, y_exact , 'r-', label='Exact')
         plt.xlabel('x')
         plt.ylabel('y(x)')
         st1 = 'Solution for h = '+str(h) 
         plt.legend(title=st1)
         st2 = 'Solution_h_'+str(h)+'.pdf'
         plt.savefig(st2)
         
         plt.figure()
         plt.plot(x_eul, e_eul , 'b.-', label='Eul')
         plt.plot(x_rk, e_rk , 'g*-', label='RK4')
         plt.xlabel('x')
         plt.ylabel('error(x)')
         st1 = 'Error for h = '+str(h) 
         plt.legend(title=st1)
         st2 = 'Error_h_'+str(h)+'.pdf'
         plt.savefig(st2)
         # ------------------------------------------------------


# ------------------------------------------------------
# plot outside the loop
plt.figure()
plt.loglog(h_values, RMQE_eul , 'b.', label='Eul num sol')
plt.loglog(h_values, RMQE_rk  , 'g*', label='RK4 num sol')
plt.loglog(h_values, 0.1*h_values , 'b-', label='h^1')
plt.loglog(h_values, 1e-3*h_values**4.0 , 'g--', label='h^4')
plt.xlabel('h')
plt.ylabel('RMQE')
st1 = 'Error vs h'
plt.legend(title=st1)
st2 = 'Error_vs_h.pdf'
plt.savefig(st2)

# ------------------------------------------------------

         
#plt.show()


