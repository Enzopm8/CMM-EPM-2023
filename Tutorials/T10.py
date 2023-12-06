# Tutorial 10
#------------------------------------------------------------------------------
# Exercise 1

import sympy as sym

# Define some symbols
x = sym.Symbol('x')
a = sym.Symbol('a')
c = sym.Symbol('c')

# Define the function y(x)
y = c * sym.sin(a * x)

# Calculate the derivative dy/dx
dydx = sym.diff(y, x)

# Print them
print('Function y(x):     ', y)
print('First derrivative w.r.t x:  ', dydx)

#------------------------------------------------------------------------------
# Exercise 2
d2yd2x = sym.diff(dydx, x)
print('Second Derivative w.r.t x:  ', d2yd2x)

# Define the function z(x)
z = dydx + d2yd2x
print('z(x):  ', z)

# Define the function s(x)
s = 1/y * dydx
print('z(x):  ', s)

#simplify the function
s_simp = s.simplify()
print('s(x) simplified:  ', s_simp)

taylor = s_simp.series(x)
print('taylor series of s(x): ', taylor)