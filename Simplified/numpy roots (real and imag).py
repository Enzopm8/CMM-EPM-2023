# Print section header for Question 1a
print('\n------ Q1. a)------\n')

# Import NumPy library
import numpy as np

# Define a function to find the roots of a polynomial given its coefficients
def find_roots(coefficients, num_roots_to_find):
    # Find roots using NumPy's roots function
    roots = np.roots(coefficients)
    
    # Separate real and complex roots
    real_roots = roots[np.isreal(roots)].real
    complex_roots = roots[np.iscomplex(roots)].real
    complex_roots_imag = roots[np.iscomplex(roots)].imag
    
    # Print the polynomial equation
    print("Polynomial Equation:")
    equation_str = " + ".join([f"{coeff}x^{power}" if power > 0 else f"{coeff}" for power, coeff in enumerate(coefficients[::-1]) if coeff != 0])
    print(f"P(x) = {equation_str}\n")
    
    # Print the real roots
    print("Real Roots:")
    for i, root in enumerate(real_roots[:num_roots_to_find]):
        print(f"{i + 1}st Real Root: {root}")
    
    # Print the complex roots
    # Print the complex roots
    print("\nComplex Roots:")
    for i in range(0, num_roots_to_find * 2, 2):
        real = complex_roots[i]
        imag = complex_roots_imag[i]
        print(f"{i // 2 + 1}st Complex Root: {real} + {imag}i")
        print(f"{i // 2 + 1}nd Complex Root: {real} - {imag}i")

        # Incrementing i by 1 again to skip the next iteration
        i += 1

# Example usage:
# Define coefficients of the polynomial in descending order of power of x 
s = 1500
c = 12
coefficients = [1, 2*c, 3*s,  s*c, s**2]

# Specify the number of roots to find
num_roots_to_find = 2

# Call the function to find and print the specified number of roots
find_roots(coefficients, num_roots_to_find)
