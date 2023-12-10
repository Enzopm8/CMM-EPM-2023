import numpy as np
import matplotlib.pyplot as plt

# Generate grid points for x1 and x2
x1_a = np.linspace(-10, 10, 100)
x2_a = np.linspace(-10, 10, 100)
x1, x2 = np.meshgrid(x1_a, x2_a, indexing='ij')

# Parameters and forces
ka = 9.
kb = 2.
La = 10.
Lb = 10.
F1 = 2.
F2 = 4.

# Potential Energy (PE) calculation
PE = 0.5 * (ka * ((x1**2 + (La - x2)**2)**0.5 - La)**2) + 0.5 * \
     (kb * ((x1**2 + (Lb + x2)**2)**0.5 - Lb)**2) - F1 * x1 - F2 * x2

# Plotting the contour of the Potential Energy
plt.figure()
plt.contour(x1, x2, PE, 100)
plt.colorbar()
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.savefig('PE.png')
plt.show()
