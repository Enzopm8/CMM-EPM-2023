# Recommendation:
# This code provides three different methods for polynomial evaluation: Horner's Method, Naive Polynomial Evaluation, and Iterative Polynomial Evaluation.
# The choice of method depends on the specific requirements and characteristics of the polynomial being evaluated.

# Not recommended:
# While all three methods are valid, Horner's Method is generally recommended for its efficiency and numerical stability compared to the naive and iterative methods.

# How to modify for a different polynomial or method:
# 1. Define a new set of polynomial coefficients 'A' based on the polynomial you want to evaluate.
# 2. Choose the appropriate method (Horner's, Naive, or Iterative) based on your requirements.
# 3. Adjust the value of 'x' based on the point at which you want to evaluate the polynomial.


# Horner's Method for Polynomial Evaluation
def poly_horner(A, x):
    # Initialize the result as the last coefficient
    result = A[-1]
    for coefficient in reversed(A[:-1]):  # Iterate through the coefficients using Horner's method
        result = result * x + coefficient  # Evaluate the polynomial using Horner's method
    return result  # Return the final evaluated polynomial value

# Naive Polynomial Evaluation
def poly_naive(A, x):
    result = 0  # Initialize result as 0
    for i, coefficient in enumerate(A):  # Iterate through each coefficient
        result += coefficient * (x ** i)  # Evaluate the polynomial using the naive method
    return result  # Return the final evaluated polynomial value

# Iterative Polynomial Evaluation
def poly_iter(A, x):
    result = 0  # Initialize result as 0
    xn = 1  # Initialize x^n
    for coefficient in A:  # Iterate through each coefficient
        result += coefficient * xn  # Evaluate the polynomial iteratively
        xn *= x  # Update x^n for the next iteration
    return result  # Return the final evaluated polynomial value

# Test polynomial coefficients and x value
# in ascending powers of x e.g A[1,2,3,4,5] is 1(x**0) + 2(x**1) + 3(x**2)...
A = [1, -2, -3, 5, 1]
x = 0.59

# Display results of all three polynomial evaluation methods
print(f"Horner's Method Result: {poly_horner(A, x)}")
print(f"Naive Polynomial Result: {poly_naive(A, x)}")
print(f"Iterative Polynomial Result: {poly_iter(A, x)}")
