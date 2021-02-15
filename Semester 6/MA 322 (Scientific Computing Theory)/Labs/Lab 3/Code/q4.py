# Question 4 Lab 03
# AB Satyaprakash (180123062)

# imports ----------------------------------------------------------------------
from math import factorial
import numpy as np
import sympy as sp
# ------------------------------------------------------------------------------
# functions --------------------------------------------------------------------


def forwardDiff(fArray):
    sz = len(fArray)
    fdArray = [fArray]
    for i in range(1, sz):
        temp = []
        for j in range(sz-i):
            temp.append(fdArray[i-1][j+1]-fdArray[i-1][j])
        fdArray.append(temp)
    return fdArray


def newtonFDPoly(fArray, xArray):
    x0, x1 = xArray[0], xArray[1]
    h = x1-x0
    u = np.array([1/h, -x0/h])
    fdArray = forwardDiff(fArray)
    sz = len(fArray)
    px = np.array([0])

    for i in range(sz):
        term = np.array([1])
        for j in range(i):
            term = np.polymul(term, np.polyadd(u, np.array([-j])))
            term = term/(j+1)
        term = term*fdArray[i][0]
        px = np.polyadd(px, term)
    return px


# ------------------------------------------------------------------------------
# g(x) = sin(x)/(x^2). Calculate g(0.25)
# (a) By direct interpolation
X = [0.1, 0.2, 0.3, 0.4, 0.5]
G = [9.9833, 4.9667, 3.2836, 2.4339, 1.9177]

# Construct a degree 3 polynomial to appproximate g(0.25)
px = newtonFDPoly(G[:4], X[:4])
print('Thus, the approximation of g(0.25) using direct interpolation = P(0.25) = {}'.format(np.polyval(px, 0.25)))
# ((x−0.1)(x−0.2)(x−0.3)(x−0.4)*Δ_4(f0))/4!(0.1)^4 is used to find the error!
Δ4_f0 = forwardDiff(G)[4][0]
x = sp.Symbol('x')
errorExpression = ((x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*Δ4_f0)/(factorial(4)*(0.1**4))
errorValue = abs(errorExpression.subs(x, 0.25))
print('The error term is at x = 0.25 is', errorValue)

# (b) By first tabulating xg(x) and then forward difference interpolating in that table
for i in range(5):
    G[i] *= X[i]
px = newtonFDPoly(G[:4], X[:4])
print('\n\nThus, the approximation of g(0.25) using interpolation on xg(x) table = P(0.25) = {}'.format(
    np.polyval(px, 0.25)*4))
Δ4_f0 = forwardDiff(G)[4][0]
x = sp.Symbol('x')
errorExpression = ((x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*Δ4_f0)/(factorial(4)*(0.1**4))
errorValue = abs(errorExpression.subs(x, 0.25)*4)
print('The error term is at x = 0.25 is', errorValue)

# (c) Explain the difference between the results in (i) and (ii) respectively.
print('\nSince the differences in (i) are oscillating and are not decreasing fast, the resulting error in interpolation would be large.')
print('However, the differences in (ii) tend to become smaller in magnitude, we expect more accurate results in this case.')

# Question 4 ends --------------------------------------------------------------
