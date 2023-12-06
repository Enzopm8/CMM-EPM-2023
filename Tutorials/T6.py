# Tutorial 6
#------------------------------------------------------------------------------
#Ex1

def Para_1():
    M = 70  #kg
    D = 10  #kg/s
    return M, D



def Para_2():
    M = 60  #kg
    D = 14  #kg/s
    return M, D

def Para_3():
    M = 40  #kg
    D = 17  #kg/s
    return M, D

V = 5

#calculate the tension in each cord and the acceleration of the group
# Import the NumPy library for numerical operations
import numpy as np

# Function to solve a system of linear equations using Gaussian Elimination
def linearsolver(A, b):
    """
    Solves a system of linear equations Ax = b using Gaussian Elimination with Backward Substitution.

    Parameters:
    A (numpy.ndarray): Coefficient matrix of the linear system.
    b (numpy.ndarray): Column vector on the right-hand side of the linear system.

    Returns:
    numpy.ndarray: Solution vector x.

    Usage Example:
    A = np.array([[70., 1., 0], [60., -1., 1.], [40, 0, -1]])
    b = np.array([[636.7, 518.6, 307.4]])
    print(linearsolver(A, b))
    """
    n = len(A)

    # Initialise solution vector as an array of zeros
    x = np.zeros(n)

    # Augment matrix A with vector b to form an augmented coefficient matrix M
    M = np.concatenate((A, b.T), axis=1)

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[[k, i]] = M[[i, k]]
            else:
                pass
                for j in range(k+1, n):
                    q = M[j][k] / M[k][k]
                    for m in range(n + 1):
                        M[j][m] += -q * M[k][m]

    # Calculate the solution by back-substitution
    x[n - 1] = M[n - 1][n] / M[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        z = M[i][n]
        for j in range(i + 1, n):
            z = z - M[i][j] * x[j]
        x[i] = z / M[i][i]

    return x

# Example usage:
# Define matrices A (left) and b (right) for solving the system of linear equations
#x1 is m, x2 is T and x3 ir R 

A = np.array([[70., 1., 0], [60., -1., 1.], [40, 0, -1]])
b = np.array([[636.7, 518.6, 307.4]])

# Print the original system of linear equations
print("Original System of Linear Equations:")
for i in range(len(A)):
    equation = f"{A[i][0]}x1 + {A[i][1]}x2 + {A[i][2]}x3 = {b[0][i]}"
    print(equation)

# Solve the linear system using the linearsolver function
solution = linearsolver(A, b)

# Print the solution vector
print("\nSolution Vector (x):")
for i, value in enumerate(solution):
    print(f"x{i+1} = {value}")