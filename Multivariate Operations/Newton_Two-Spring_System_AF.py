import sympy
import numpy as np

# Define symbolic variables
x, y = sympy.symbols('x, y')

# Need the following to create functions out of symbolic expressions
from sympy.utilities.lambdify import lambdify
from sympy import Matrix, simplify, hessian, init_printing
init_printing()

# Constants and forces
ka = 9.0
kb = 2.0
La = 10.0
Lb = 10.0
F1 = 2.0
F2 = 4.0

X = Matrix([x, y])

# Define the objective function
f = Matrix([0.5 * (ka * ((x**2 + (La - y)**2)**0.5 - La)**2) +
            0.5 * (kb * ((x**2 + (Lb + y)**2)**0.5 - Lb)**2) - F1 * x - F2 * y])

print("Shape of the objective function matrix:", np.shape(f))

# Since the Hessian is 2x2, then the Jacobian should be 2x1 (for matrix multiplication)
gradf = simplify(f.jacobian(X)).transpose()

# Create a function that will take the values of x, y and return a Jacobian matrix with values
fgradf = lambdify([x, y], gradf)
print('Jacobian f:', gradf)

hessianf = simplify(hessian(f, X))

# Create a function that will return a Hessian matrix with values
fhessianf = lambdify([x, y], hessianf)
print('Hessian f:', hessianf)


def Newton_Raphson_Optimize(Grad, Hess, x, y, epsilon=0.000001, nMax=200):
    """
    Newton-Raphson optimization method for a system of equations.

    Parameters:
    - Grad: Gradient of the objective function.
    - Hess: Hessian (second derivative) of the objective function.
    - x, y: Initial guess for the minimum.
    - epsilon: Tolerance for convergence, default is 0.000001.
    - nMax: Maximum number of iterations, default is 200.

    Returns:
    - The approximate root of the system of equations.
    - Arrays of x and y values at each iteration.
    - Array of iteration counts.

    How it works:
    1. Initialize variables and parameters.
    2. Iterate until the error is below the specified tolerance or the maximum number of iterations is reached.
    3. Update the solution using the Newton-Raphson method.

    """
    print("\nNewton-Raphson Optimization:")
    print("=============================")

    # Initialization
    i = 0
    iter_x, iter_y, iter_count = np.empty(0), np.empty(0), np.empty(0)
    error = 10
    X = np.array([x, y])

    # Looping as long as the error is greater than epsilon
    while np.linalg.norm(error) > epsilon and i < nMax:
        i += 1
        iter_x = np.append(iter_x, x)
        iter_y = np.append(iter_y, y)
        iter_count = np.append(iter_count, i)

        X_prev = X
        # X had dimensions (2,) while the 2nd term (2,1), so it had to be converted to 1D
        X = X - np.matmul(np.linalg.inv(Hess(x, y)), Grad(x, y)).flatten()
        error = X - X_prev
        x, y = X[0], X[1]

    print("\nResults:")
    print("--------")
    print(f"Approximate root: x = {x:.6f}, y = {y:.6f}")
    print(f"Iterations: {i}")
    print("=============================")

    return X, iter_x, iter_y, iter_count


# Initial guess for the root
root, iter_x, iter_y, iter_count = Newton_Raphson_Optimize(fgradf, fhessianf, 1, 1)
