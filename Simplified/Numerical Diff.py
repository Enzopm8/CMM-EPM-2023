#                         Differentiation Using Sympy
# you want to prove that C is the general solution to B
print('\n------ Differentiation------\n')

import sympy as sym

# Define the variables
x, y, w, TA, y0 = sym.symbols('x y w TA y0')

# Define the equation C
C = (TA / w) * sym.cosh((w / TA) * x) + y0 - (TA / w)

# Differentiate equation_C with respect to x
dydx = sym.diff(C, x)

# Calculate the second derivative
d2yd2x = sym.diff(dydx, x)

# Substitute 1st term into second term (cosh--> sinh), can also be used to insert numbers like XXX.subs({w: 0.05, TA:___, ....})
d2yd2x_sub = d2yd2x.subs(sym.cosh(w / TA * x), sym.sqrt(1 + sym.sinh(w / TA * x)**2))

# Define the RHS of Equation B
B = (w / TA) * sym.sqrt(1 + (dydx**2))

# Display the results
print("Equation C:")
print(C)
print("\n1st Derivative of Equation C with respect to x:")
print(dydx)
print("\n2nd Derivative of Equation C with respect to x:")
print(d2yd2x_sub)
print("\nRight-hand side of Equation B:")
print(B)

# Simplify the expressions for comparison
d2yd2x_simp = sym.simplify(d2yd2x_sub)
B_simp = sym.simplify(B)

# Check if the second derrivative of C is equal to the RHS of B
is_equal = sym.simplify(d2yd2x_simp - B_simp) == 0

print("\nIs Equation C the general solution to Equation B?")
print(is_equal)

'''
#Solve function B for w
inst_freq = sym.solve(B, w)

# Convert the symbolic expression B to a numerical function w.r.t var w in the numpy form 
f_numeric = sym.lambdify(w, B, 'numpy')

#get the taylor expansion of the function w.r.t x
taylor = B_simp.series(x)
print('taylor series of s(x): ', taylor)
'''
