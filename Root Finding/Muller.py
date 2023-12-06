# Recommendation:
# This code is designed for finding roots of equations using Muller's method.
# It is recommended for functions with complex roots where other methods may fail, and the root is expected to be found within a reasonable number of iterations.

# Not recommended:
# Muller's method may not converge for functions with multiple roots, and it might not be as efficient for well-behaved functions with simple roots.
# Additionally, it may not work well for functions with sharp turns or near-vertical slopes.

# How to modify for a different function:
# 1. Define the new function f(x): Replace the existing function 'f' with the one corresponding to the new function.
# 2. Adjust the initial guesses ('a', 'b', 'c'): Set appropriate initial values based on the characteristics of the new function.
# 3. Modify the maximum number of iterations: Adjust 'MAX_ITERATIONS' based on the desired level of accuracy and computational resources.


# a function, f(x)
import math;
 
MAX_ITERATIONS = 10000;
 
# Function to calculate f(x)
def f(x):
 
    # Taking f(x) = x ^ 3 + 2x ^ 2 + 10x - 20
    # pow is used to define the exponent of x
    return (1 * pow(x, 3) + 2 * pow(x, 2) + 10 * pow(x, 1) - 20*pow(x, 0));
 
def Muller(a, b, c):
 
    res = 0;
    i = 0;
 
    while (True):
     
        # Calculating various constants 
        # required to calculate x3
        f1 = f(a); f2 = f(b); f3 = f(c);
        d1 = f1 - f3; 
        d2 = f2 - f3;
        h1 = a - c; 
        h2 = b - c;
        a0 = f3;
        a1 = (((d2 * pow(h1, 2)) -
               (d1 * pow(h2, 2))) /
              ((h1 * h2) * (h1 - h2)));
        a2 = (((d1 * h2) - (d2 * h1)) /
              ((h1 * h2) * (h1 - h2)));
        x = ((-2 * a0) / (a1 +
             abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
        y = ((-2 * a0) / (a1 -
            abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
 
        # Taking the root which is 
        # closer to x2
        if (x >= y):
            res = x + c;
        else:
            res = y + c;
 
        # checking for resemblance of x3 
        # with x2 till two decimal places
        m = res * 100;
        n = c * 100;
        m = math.floor(m);
        n = math.floor(n);
        if (m == n):
            break;
        a = b;
        b = c;
        c = res;
        if (i > MAX_ITERATIONS):
            print("Root cannot be found using", 
                            "Muller's method");
            break;
        i += 1;
    if (i <= MAX_ITERATIONS):
        print("The value of the root is",
                          round(res, 4));
 
# Driver Code
a = 0;
b = 1;
c = 2;
Muller(a, b, c);
     
# This code is contributed by mits
