import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

# Define the objective function
def Function(x, y):
    return (1 + x)**2 + 100*(y - x**2)**2

# Define the gradient of the objective function
def Grad(x, y):
    g1 = -400*x*y + 400*x**3 + 2*x - 2
    g2 = 200*y - 200*x**2
    return np.array([g1, g2])

# Define the Hessian matrix of the objective function
def Hessian(x, y):
    h11 = -400*y + 1200*x**2 + 2
    h12 = -400 * x
    h21 = -400 * x
    h22 = 200
    return np.array([[h11, h12], [h21, h22]])

# Define the Newton-Raphson optimization method
def Newton_Raphson_Optimize(Grad, Hess, x, y, epsilon=0.000001, nMax=200):
    # Initialization
    i = 0
    iter_x, iter_y, iter_count = np.empty(0), np.empty(0), np.empty(0)
    error = 10
    X = np.array([x, y])
    
    print(f"Iteration | X values")
    
    # Looping as long as the error is greater than epsilon
    while np.linalg.norm(error) > epsilon and i < nMax:
        i += 1
        iter_x = np.append(iter_x, x)
        iter_y = np.append(iter_y, y)
        iter_count = np.append(iter_count, i)   
        
        print(f"    {i}     | {X}") 
        
        X_prev = X
        X = X - np.linalg.inv(Hess(x, y)) @ Grad(x, y)
        error = X - X_prev
        x, y = X[0], X[1]
    
    print("\nOptimization Result:")
    print(f"Roots found at X = {X}")
    print(f"Objective Function Value at the Root: {Function(X[0], X[1])}")      
    
    return X, iter_x, iter_y, iter_count

# Apply Newton-Raphson optimization and get the results
root, iter_x, iter_y, iter_count = Newton_Raphson_Optimize(Grad, Hessian, -2, 2)
