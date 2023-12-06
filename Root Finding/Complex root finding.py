import numpy as np

def find_roots(coefficients):
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
    
    # Print the roots
    print("Roots:")
    for i, root in enumerate(real_roots):
        print(f"{i + 1}st Root: {root}")
    
    for i, (real, imag) in enumerate(zip(complex_roots, complex_roots_imag)):
        print(f"{i + 1}st Root: {real} + {imag}i")
        print(f"{i + 2}nd Root: {real} - {imag}i")
        # Incrementing i by 1 again to skip the next iteration
        i += 1

# Example usage:
# Define coefficients of the polynomial in descending order of power of x 
coefficients = [0, 1, 2, 10, -20] 

find_roots(coefficients)
