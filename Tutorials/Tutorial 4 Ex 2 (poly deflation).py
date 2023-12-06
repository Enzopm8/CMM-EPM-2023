# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:08:35 2023

@author: enzop
"""
def synthetic_division(coefficients, divisor):
    n = len(coefficients)
    
    # Initialize the result list with the first coefficient
    result = [coefficients[0]]
    
    # Perform synthetic division
    for i in range(1, n):
        term = coefficients[i] + result[-1] * divisor
        result.append(term)
    
    # Calculate the remainder as the last term of the result
    remainder = result[-1]
    
    return result[:-1], remainder

# Coefficients of the polynomial f(x) = x^2 + 2x - 24
coefficients = [1, 2, -24]

# Divisor: (x - 4)
divisor = 4

# Perform synthetic division
quotient, remainder = synthetic_division(coefficients, divisor)

# Print the quotient coefficients and remainder
print("Quotient coefficients:", quotient)
print("Remainder:", remainder)


