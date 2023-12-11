import numpy as np
import math as math

def gsection(ftn, xl, xm, xr, tol=1e-9):
    """
    Golden Section Search algorithm for optimizing a unimodal function.

    Parameters:
    - ftn: Function to be optimized.
    - xl: Initial left endpoint of the interval.
    - xm: Initial guess for the minimum within the interval.
    - xr: Initial right endpoint of the interval.
    - tol: Tolerance for convergence, default is 1e-9.

    Returns:
    - The approximate minimum of the function.

    How it works:
    1. Initialize points xl, xm, and xr.
    2. Evaluate function values at xl, xm, and xr (fl, fm, fr).
    3. Refine xl, xm, and xr iteratively until the interval is within tolerance.

    """
    gr1 = 1 + (1 + np.sqrt(5))/2

    # Successively refine xl, xr, and xm
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)

    while ((xr - xl) > tol):
        if ((xr - xm) > (xm - xl)):
            y = xm + (xr - xm)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm - (xm - xl)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy

    min_value = ftn(xm)
    print(f"Minimum value of the function: {min_value:.6f} at x = {xm:.6f}")
    return xm

xl = 0
xm = 5
xr = 10

def ftn(x):
    return 2 * math.sin(x) - (x**2/10)

print(gsection(ftn, xl, xm, xr, tol=1e-9))
