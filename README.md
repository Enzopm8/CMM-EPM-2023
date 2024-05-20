# CMM Enzo Pons

## Root Finding Methods:

1. **Bisection:**
   - Divides interval, selects subinterval with root.
   - Continuous functions, known signs.
   - Simple, reliable, closed.

2. **False Position:**
   - Linear interpolation like bisection.
   - Continuous functions, known signs.
   - Usually faster than bisection, closed.

3. **Golden Search Method:**
   - Uses golden ratio for root finding.
   - Unimodal functions in a specified interval.
   - Does not require derivative, closed.

4. **Inverse Quadratic Interpolation:**
   - Uses inverse quadratic model for root.
   - Functions difficult for other methods.
   - Can be fast, open.

5. **Modified False Position:**
   - Variation of false position.
   - Similar to false position, improved convergence.
   - Improves speed, closed.

6. **Muller:**
   - Quadratic interpolation for root finding.
   - No derivative information, general-purpose.
   - Can handle complex roots, open.

7. **Naive Line Search:**
   - Simplistic approach, stepping through values.
   - Simple unimodal functions.
   - Easy to implement, open.

8. **Newton:**
   - Iterative convergence using function and derivative.
   - Derivatives known and continuous.
   - Fast convergence, open.

9. **Secant:**
   - Approximates derivative like Newton.
   - Difficult to compute derivative.
   - Does not require explicit derivative, open.

10. **Single Fixed Point Iteration:**
    - Transforms equation into x = g(x).
    - Functions transformable into stable iteration.
    - Simple, may converge slowly, open.

11. **Horner Quartic & Synthetic Division:**
    - Efficient polynomial evaluation/root finding.

## Regression and Interpolation:

- **Linear Regression:**
  - Fitting a straight line to data.
  - Simple, provides insights into relationships.
  - Sensitive to outliers, assumes linearity.

- **Polynomial Regression:**
  - Fitting a curved line using least squares.
  - Simple and flexible for data approximation.
  - Sensitive to outliers.

- **Polynomial Interpolation & Spline Interpolation:**
  - Estimating values between known points.
  - Interpolation for precise data, spline more flexible.

## Linear Algebra:

- **Cramer Rule:**
  - Finds determinant, applies to square systems.
  - Applicable to three equations, not efficient for more.

- **Naïve Gauss Elimination:**
  - Forms augmented matrix, eliminates to upper triangle.
  - Prone to crash, accumulates errors, needs improvement.

## ODE Methods:

- **Euler Method:**
  - Linear extrapolation using slope.
  - Simple, for simple problems, may lack precision.

- **Implicit Euler, Stiff Euler, 4th Order Runge Kutta:**
  - Implicit for stiff ODEs, adaptive step size.
  - 4th Order Runge Kutta for accuracy.
  - Each method has advantages and disadvantages.

## Integration:

- **Quadrature Techniques:**
  - Rectangle/Midpoint, Trapezoidal, Composite Simpson.
  - Simpson most accurate, adaptive algorithm saves time.

## Additional Concepts:

- **Root Mean Square Error (RMSE):**
  - Measures model error in predicting quantitative data.
 
  - To solve part (b), we need to find the solution \( u(r, \theta) \) that satisfies the given boundary conditions for the non-dimensional temperature \( u \) at the inner and outer surfaces of the cylindrical pipe. The boundary conditions are:

1. \( u(1, \theta) = 0 \) for \( 0 \leq \theta < 2\pi \)
2. \( u(2, \theta) = f_b(\theta) \) for \( 0 \leq \theta < 2\pi \)

where \( f_b(\theta) \) is given by:

\[ f_b(\theta) = \begin{cases}
\frac{\pi^2}{4} - \theta^2, & -\frac{\pi}{2} \leq \theta < \frac{\pi}{2} \\
0, & \frac{\pi}{2} \leq \theta < \frac{3\pi}{2}
\end{cases} \]

We are given the form of the solution from part (a):

\[ u(r, \theta) = k \log(r) + \sum_{n=1}^{\infty} \left( a_n \cos(n\theta) + b_n \sin(n\theta) \right) \left( r^n - r^{-n} \right) \]

### Step-by-Step Solution

1. **Boundary Condition at \( r = 1 \):**

   At \( r = 1 \),

   \[ u(1, \theta) = 0 \]

   Substituting \( r = 1 \) in the general solution:

   \[ 0 = k \log(1) + \sum_{n=1}^{\infty} \left( a_n \cos(n\theta) + b_n \sin(n\theta) \right) \left( 1 - 1 \right) \]

   Since \( \log(1) = 0 \) and \( 1 - 1 = 0 \), this condition is automatically satisfied.

2. **Boundary Condition at \( r = 2 \):**

   At \( r = 2 \),

   \[ u(2, \theta) = f_b(\theta) \]

   Substituting \( r = 2 \) in the general solution:

   \[ f_b(\theta) = k \log(2) + \sum_{n=1}^{\infty} \left( a_n \cos(n\theta) + b_n \sin(n\theta) \right) \left( 2^n - 2^{-n} \right) \]

   We need to expand \( f_b(\theta) \) into a Fourier series to match the form of the solution:

   \[ f_b(\theta) = \sum_{n=0}^{\infty} \left( c_n \cos(n\theta) + d_n \sin(n\theta) \right) \]

   For the given piecewise function \( f_b(\theta) \):

   \[ f_b(\theta) = \begin{cases}
   \frac{\pi^2}{4} - \theta^2, & -\frac{\pi}{2} \leq \theta < \frac{\pi}{2} \\
   0, & \frac{\pi}{2} \leq \theta < \frac{3\pi}{2}
   \end{cases} \]

3. **Fourier Series Expansion of \( f_b(\theta) \):**

   To find the Fourier coefficients \( c_n \) and \( d_n \), we use the standard Fourier series formulas:

   \[
   c_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f_b(\theta) \cos(n\theta) \, d\theta
   \]
   \[
   d_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f_b(\theta) \sin(n\theta) \, d\theta
   \]

   Given the symmetry and the fact that \( f_b(\theta) \) is an even function, \( d_n \) will be zero for all \( n \). Thus, we only need to compute \( c_n \):

   For \( n = 0 \),

   \[
   c_0 = \frac{1}{2\pi} \int_{-\pi}^{\pi} f_b(\theta) \, d\theta = \frac{1}{2\pi} \left( \int_{-\pi/2}^{\pi/2} \left( \frac{\pi^2}{4} - \theta^2 \right) \, d\theta \right)
   \]

   This integral evaluates to \( c_0 = \frac{\pi^2}{16} \).

   For \( n \geq 1 \),

   \[
   c_n = \frac{1}{\pi} \left( \int_{-\pi/2}^{\pi/2} \left( \frac{\pi^2}{4} - \theta^2 \right) \cos(n\theta) \, d\theta \right)
   \]

   These integrals can be computed using integration by parts or standard Fourier coefficient techniques.

4. **Matching the Fourier Series with the Solution:**

   Finally, match the Fourier coefficients from \( f_b(\theta) \) with the solution's Fourier series:

   \[
   k \log(2) = c_0, \quad a_n (2^n - 2^{-n}) = c_n, \quad b_n = 0
   \]

   Substituting the coefficients \( c_n \) into the solution form:

   \[
   k = \frac{\pi^2}{16 \log 2}
   \]

   \[
   a_n = \frac{c_n}{2^n - 2^{-n}}
   \]

   Since \( b_n = 0 \) for all \( n \), the final solution is:

   \[
   u(r, \theta) = \frac{\pi^2}{16 \log 2} \log(r) + \sum_{n=1}^{\infty} \left( \frac{c_n}{2^n - 2^{-n}} \cos(n\theta) \right) \left( r^n - r^{-n} \right)
   \]

This is the final solution for \( u(r, \theta) \) that satisfies the given boundary conditions.


- **Truncation Error and Stiff Equations:**
  - Truncation error in finite series, stiff equations need small steps for stability.

*Note: Provided summaries are highly condensed, feel free to inquire for more detailed information.*
