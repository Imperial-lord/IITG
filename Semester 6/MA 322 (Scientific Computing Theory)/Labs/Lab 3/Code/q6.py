# Question 6 Lab 03
# AB Satyaprakash (180123062)

# imports ----------------------------------------------------------------------
from math import factorial
from fractions import Fraction
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
# The following data are given for a polynomial P(x) of unknown degree.
# P(0) = 4, P(1) = 9, P(2) = 15, P(3) = 18
# Determine the coefficient of x^3 in P(x), if all fourth-order forward differences are 1.

print('As we can simply observe, if all 4th order forward differences are 1, this means')
print('All 5th order forward differences will be 0, in other words degree of polynmial is 4')
X = [0, 1, 2, 3]
P = [4, 9, 15, 18]

px = newtonFDPoly(P, X)
# Since we also have informatio about the 4th order FD, we can add 1 more term to P(x)
term = np.polymul([1, 0], np.polymul([1, -1], np.polymul([1, -2], [1, -3])))
term = (term*1)/factorial(4)
px = np.polyadd(px, term)
print('The polynmial is thus given as \n{}'.format(np.poly1d(px)))
print('Clearly, the coefficient of x^3 is {} or {}'.format(px[1], '-11/12'))

# Question 6 ends --------------------------------------------------------------
