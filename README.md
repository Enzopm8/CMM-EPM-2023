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

- **Truncation Error and Stiff Equations:**
  - Truncation error in finite series, stiff equations need small steps for stability.

*Note: Provided summaries are highly condensed, feel free to inquire for more detailed information.*
