# Question 3 Lab Assignment 2
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------
from math import exp, factorial
import numpy as np
from sympy import *

# functions --------------------------------------------------------------------


def f(x):
    return exp(-(x**2))


def makePoly(x0, x1):
    return np.array([x0, x1])


def secondLagrange(x0, x1, x2):
    # The given function here is exp(-x^2)
    f0, f1, f2 = f(x0), f(x1), f(x2)

    # Represents the numerator polynomial part in the form of an np array
    nl0 = np.polymul(makePoly(1, -x1), makePoly(1, -x2))
    nl1 = np.polymul(makePoly(1, -x0), makePoly(1, -x2))
    nl2 = np.polymul(makePoly(1, -x0), makePoly(1, -x1))

    # Constant portion to be multiplied with the polynomial
    cl0 = f0/((x0-x1)*(x0-x2))
    cl1 = f1/((x1-x0)*(x1-x2))
    cl2 = f2/((x2-x0)*(x2-x1))

    # multiplying the constants
    nl0 = nl0*cl0
    nl1 = nl1*cl1
    nl2 = nl2*cl2

    px = nl0+nl1+nl2
    return px


def derivative(x0, n):
    x = symbols('x')
    f = exp(-x*x)
    fn = f.diff(x, n)
    fn = lambdify(x, fn)
    return fn(x0)


def maxError(nodes, x):
    err = 1
    for n in nodes:
        err *= (x-n)
    err /= factorial(len(nodes))
    a = min(nodes)
    b = max(nodes)
    l = np.linspace(a, b, 250)
    ret = 0
    for z in l:
        der = derivative(z, len(nodes))
        ret = max(ret, abs(err*der))
    return ret


# ------------------------------------------------------------------------------
# Lagrange form of interpolating polynomial P2(x) at the nodes x0 = −1, x1 = 0 and x2 = 1
x0, x1, x2 = -1, 0, 1
px = secondLagrange(x0, x1, x2)
print('The Lagrange form of interpolating polynomial P2(x) is: \n {}\n'.format(np.poly1d(px)))

# The value of P2(0.9)
val = 0.9
print('The value of P2(0.9) is {}'.format(np.polyval(px, val)))
print('The value of P2(0.9) rounded to 6 decimal places is {}'.format(round(np.polyval(px, val), 6)))

# The true value of f(0.9)
print('The true value of f(0.9) is {}'.format(f(0.9)))

# The max error in this calculation
print('The max error in this calculation is {}'.format(maxError([x0, x1, x2], val)))
