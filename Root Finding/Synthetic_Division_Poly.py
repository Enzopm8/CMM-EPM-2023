# Recommendation:
# This code is designed for performing synthetic division of polynomials, specifically extended synthetic division.
# It is suitable for quick and efficient polynomial division when dividing non-monic polynomials.

# Not recommended:
# This code may not be suitable for dividing polynomials with complex roots or for situations where division by zero is a concern.
# Additionally, for large degree polynomials, it might be more efficient to use specialized libraries for polynomial manipulation.

# How to modify for other polynomials:
# 1. Update the 'dividend' and 'divisor' lists: Replace these lists with coefficients of the polynomials you want to divide.
# 2. Adjust the normalization: If the divisor is monic, you can skip the normalization step.
# 3. Modify the output format: Adjust the print statements to display the results in a way that suits your needs.

def extended_synthetic_division(dividend, divisor):
   
    # Example usage:
    # dividend = [1, -2, -3, 5, 1]
    # divisor = [1, -1.5]
    # output:  Quotient: [1.0, -0.5, -3.75, -0.625]
             # Remainder: [0.0625]
             
    out = list(dividend)  # Copy the dividend
    normalizer = divisor[0]
    
    for i in range(len(dividend) - (len(divisor) - 1)):
        out[i] /= normalizer  # For general polynomial division (when polynomials are non-monic),
                              # we need to normalize by dividing the coefficient with the divisor's first coefficient
        coef = out[i]
        if coef != 0:  # Useless to multiply if coef is 0
            for j in range(1, len(divisor)):  # In synthetic division, we always skip the first coefficient of the divisor,
                                               # because it's only used to normalize the dividend coefficients
                out[i + j] += -divisor[j] * coef
 
    separator = -(len(divisor) - 1)
    quotient, remainder = out[:separator], out[separator:]  # Quotient and remainder.
    return quotient, remainder
 
if __name__ == '__main__':
    print("POLYNOMIAL SYNTHETIC DIVISION")
    N = [1, -2, -3, 5, 1]  #modify this with the quotients of your function
    D = [1, -1.5]          #modify this with the quotient of your divisor function
    quotient, remainder = extended_synthetic_division(N, D)
    
    # Output
    print(f"  Dividend: {N}")
    print(f"  Divisor : {D}")
    print(f"  Quotient: {quotient}")
    print(f"  Remainder: {remainder}")