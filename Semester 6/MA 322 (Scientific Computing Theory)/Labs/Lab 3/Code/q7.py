# Question 7 Lab 03
# AB Satyaprakash (180123062)

# imports ----------------------------------------------------------------------
from math import factorial
from fractions import Fraction
import numpy as np
import sympy as sp
# ------------------------------------------------------------------------------
# For a function f , the Newton divided-difference formula gives the interpolating polynomial
# P(x) = 1 + 4x + 4x(x − 0.25) + (16/3)x(x − 0.25)(x − 0.5),
# on the nodes x0 = 0, x1 = 0.25, x2 = 0.5, and x3 = 0.75. Find f(0.75).

print('Using P(x) we find the following:')
print('f[x0,x1,x2,x3] = 16/3')
print('f[x0,x1,x2] = 4')
print('f[x0,x1] = 4')
print('f[x0] = 1')

print('\nUsing the above information and simple arithmetic, the divided differences table is obtained as follows:')
X = [[0, 1], [0.25, 2, 4], [0.5, 3.5, 6, 4], [0.75, 6, 10, 8, 16/3]]
print('x\tf\n-------------------------------------------------------------------')
for i in range(4):
    for j in range(5):
        if(j >= len(X[i])):
            print(" ", end="\t")
        else:
            print(X[i][j], end="\t")
    print('\n', end="")

print('\nClearly, from the above table, we get f(0.75) = 6')

# Question 7 ends --------------------------------------------------------------
