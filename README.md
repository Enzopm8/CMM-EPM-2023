# Computational Methods and Modelling

This readme provides a concise overview of various numerical methods and analysis techniques for solving mathematical problems commonly encountered in engineering and scientific disciplines.

## Root Finding Methods

### Bisection
- **Description:** Divides an interval in half and selects the subinterval in which a root must lie.
- **When to Use:** Continuous functions with known signs at the interval ends.
- **Disadvantages:** Slow convergence for some functions.
- **Advantages:** Simple and reliable.
- **Open/Close:** Closed

### False Position
- **Description:** Similar to bisection but uses linear interpolation.
- **When to Use:** Continuous functions with known signs at the interval ends.
- **Disadvantages:** Can converge slowly if one endpoint always yields the same sign.
- **Advantages:** Usually faster than bisection.
- **Open/Close:** Closed

### Golden Search Method
- **Description:** Uses the golden ratio to find minima/maxima, applicable for root finding by reformulating the problem.
- **When to Use:** Unimodal functions in a specified interval.
- **Disadvantages:** Slower compared to other methods for function optimization.
- **Advantages:** Does not require derivative information.
- **Open/Close:** Closed

### Inverse Quadratic Interpolation
- **Description:** Uses an inverse quadratic model to approximate the root.
- **When to Use:** Functions that are difficult for other methods due to oscillation or slow convergence.
- **Disadvantages:** Complex and can diverge if not properly applied.
- **Advantages:** Can be very fast for some functions.
- **Open/Close:** Open

### Modified False Position
- **Description:** A variation of the false position method with adjusted interval selection criteria.
- **When to Use:** Similar to false position when the standard method converges slowly.
- **Disadvantages:** Requires more computation per iteration than standard false position.
- **Advantages:** Improves convergence speed compared to standard false position.
- **Open/Close:** Closed

### Muller
- **Description:** Uses a quadratic interpolation for root finding.
- **When to Use:** Functions where derivative information is not available or unreliable.
- **Disadvantages:** Can be less stable.
- **Advantages:** General-purpose and can handle complex roots.
- **Open/Close:** Open

### Naive Line Search
- **Description:** A simplistic approach, often involving stepping through a range of values.
- **When to Use:** Simple unimodal functions.
- **Disadvantages:** Inefficient and not precise.
- **Advantages:** Easy to implement.
- **Open/Close:** Open

### Newton
- **Description:** Uses function and derivative to iteratively converge to the root.
- **When to Use:** Functions where derivatives are known and continuous.
- **Disadvantages:** Requires derivative, can diverge if the initial guess is poor.
- **Advantages:** Fast convergence for well-behaved functions.
- **Open/Close:** Open

### Secant
- **Description:** Similar to Newton but approximates the derivative.
- **When to Use:** When the derivative is difficult to compute.
- **Disadvantages:** Can fail to converge for poor initial guesses.
- **Advantages:** Does not require an explicit derivative.
- **Open/Close:** Open

### Single Fixed Point Iteration
- **Description:** Transforms the equation into x = g(x) and iteratively solves.
- **When to Use:** Functions that can be transformed into a stable fixed-point iteration.
- **Disadvantages:** Can converge very slowly or diverge.
- **Advantages:** Simple to understand and implement.
- **Open/Close:** Open

### Horner Quartic
- **Description:** Efficient polynomial evaluation and root finding method, often used in combination with other methods.

### Synthetic Division Poly
- **Description:** Used for polynomial root finding by iteratively reducing polynomial order.

### Bisection Step by Step, False Position, Newton Raphson, Secant
- **Comparison:** Secant vs False Position.

## Regression + Interpolation

### Linear Regression Analytical Method

**Equation (1):**
- **Slope (a1):** Calculates the slope of the best-fit line, representing the average change in y for each unit change in x, based on the covariance of x and y relative to the variance of x.

**Equation (2):**
- **Intercept (a0):** Determines the y-intercept of the best-fit line, which is the expected value of y when x is zero, calculated by adjusting the mean of y by the slope times the mean of x.

**Equation (3):**
- **Linear Equation:** Represents the linear equation y=a0+a1x that represents the best-fit line, allowing for the prediction of y from any value of x using the intercept and slope derived from the data.

### Summary

In summary, these formulas are used to find the line of best fit in a set of data, where the line has the equation y=a0+a1x. The line minimizes the distances (errors) between the actual data points and the predictions made by the linear model.

### Polynomial Regression

- **Description:** Fitting a curved line to data using the method of least squares.
- **When to Use:** Suitable for fitting data that exhibits a polynomial trend.
- **Advantages:** Fit complex curves by using higher-degree polynomials.
- **Disadvantages:** Sensitive to outliers.

### Polynomial Interpolation

- **Description:** Sample Equation at two locations, estimating intermediate values.
- **Advantages:** Smaller interval provides better approximation.
- **Disadvantages:** Not always the best; second order is more accurate.

### Spline Interpolation

- **Description:** Special type of piecewise polynomial, fits low-degree polynomial to a small subset of values.
- **When to Use:** Flexible and powerful interpolation, avoids oscillatory behavior that occurs with a single high-order polynomial.

## Linear Algebra

### Cramer Rule

- **How it Works:** Arrange formula Ax=b, find the Determinant. If det = 0, the system is singular; Cramer can't be applied.
- **When to Use:** Three equations where a solution exists, applicable only to a square system.
- **Advantages:** Applicable when a solution exists.
- **Disadvantages:** Not computationally efficient when more than 3 equations.

### Naïve Gauss Elimination

1. Form Augmented Matrix.
2. Forward Elimination to make the matrix an upper triangle.
3. Backwards substitute, finding coefficients where the rest is 0.

- **When to Use:** System of linear equations.
- **Advantages:** Can accumulate inaccuracies due to round-off error.
- **Disadvantages:** Will crash if unable to handle division by 0; ill-conditioned systems are not suited.

### Solutions to Improve

- Use more significant figures.
- Use partial or full pivoting.

## Ordinary Differential Equations (ODE)

### Euler

- **How it Works:** Given dy/dx=f(x,y) with initial conditions y(x0)=y0, approximates the solution by linearly extrapolating the slope of the curve.
- **When to Use:** Simple problems where precision is not needed.
- **Advantages:** Simple, easy to understand and implement.
- **Disadvantages:** Can be inaccurate, especially for stiff ODEs or when large step sizes are used.

### Implicit or Backwards Euler Method

- **How it Works:** Implicit because yi is on both sides of the equation. Invert the formula to find its roots.
- **When to Use:** For all stiff ODE (when stability is more important than precision).
- **Advantages:** Euler overshoots the exact solution, implicit undershoots the exact solution, high computational cost per step.

### Stiff Euler

- **How it Works:** Euler method but with adaptive step size, changes the step size h for different intervals of x, depending on fast or slow parts of the function.
- **When to Use:** For stiff ODE (but can be bad for severe stiff ODE).
- **Advantages:** Allows larger steps in smoother regions of the solution, reducing computation time without losing accuracy.

### 4th Order Runge-Kutta Method

- **How it Works:** Improves accuracy of Euler method by calculating multiple slopes (k values) at different points within each step and then takes the average of the slopes for the final result.
- **When to Use:** For more complex ODE, to be more accurate.
- **Advantages:** More accurate even with a bigger step size; does not require the calculation of higher-order derivatives.
- **Disadvantages:** More complex to program.

### Root Mean Square Error (RMSE)

Measure error of model when predicting quantitative data – good for comparing different models.

Where:
- yi = numerical solution at the location xi.
- yexact(xi) is the analytical solution at xi.
- Nsteps are the number of steps performed in each method.

### Truncation Error

The difference between the exact value of the function and the value obtained from the finite series, if we truncate the series after a finite number of terms.

### Stiff Equation

A differential equation where certain components of the solution change much more rapidly than others, leading to a mix of very fast and very slow dynamics in the system.

## Integration

Four main variations of quadrature for numerical integration.

### Quadrature Techniques

Integration of a function by calculating the area under the curve.

**Accuracy of Methods:**

### Rectangle/Midpoint Rule

- **How it Works:** Divide into sections and approximate the area using rectangles.
- **Visual Representation:** Least Accurate.
- **Accuracy:** Least Accurate.

### Trapezoidal Rule

- **How it Works:** Approximate area under the curve using a series of trapezoids instead of rectangles.
- **Visual Representation:** Least Accurate.
- **Accuracy:** Least Accurate.

### Composite Simpson Rule

- **How it Works:** Divide the interval into even segments, apply quadratic parabola to segments, and calculate the area under the polynomial.
- **Visual Representation:** Most Accurate.
- **Accuracy:** Most Accurate.

**Main Quadrature Techniques:**

- **Simpson:** Uses quadratic polynomials to approximate the function in each subinterval. Higher-order approximation makes it smoother. Error depends on the fourth derivative of the function.

- **Midpoint:** Uses the value at the middle of each interval, often provides a better fit than the Trapezoidal Rule for non-linear functions. Error depends on the second derivative.

- **Trapezoidal:** Uses linear interpolation between the endpoints of each interval.

### Three Eights Simpson Rule

- **Variation:** Used when intervals are divided into odd n segments.
- **Accuracy:** More accurate than the trapezoidal rule for well-approximated polynomials. Accuracy depends on the nature of the function and the size of segments.

### Adaptive Algorithm

Numerical Method – Allows intervals to be subdivided if accuracy is not achieved after n steps. Can be applied to any approach, saving computation time.

### Simpson to Simpson Adaptive

# Conclusion

This readme provides a comprehensive guide to various numerical methods and analysis techniques, covering root finding, regression, interpolation, linear algebra, ordinary differential equations, and integration. Each method's description, use cases, advantages, and disadvantages are outlined for easy reference.
