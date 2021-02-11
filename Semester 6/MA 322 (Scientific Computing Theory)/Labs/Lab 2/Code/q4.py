# Question 4 Lab Assignment 2
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------
from math import log, tan, factorial
from sympy import *
import numpy as np

# functions --------------------------------------------------------------------


def f(x):
    return log(tan(x))/log(10)


def thirdLagrange(x0, x1, x2, x3, val):
    # Using the values given in the quesiton
    f0, f1, f2, f3 = 0.1924, 0.2414, 0.2933, 0.3492

    # compute l0(x) with x = val
    l0 = ((val-x1)*(val-x2)*(val-x3))/((x0-x1)*(x0-x2)*(x0-x3))
    l1 = ((val-x0)*(val-x2)*(val-x3))/((x1-x0)*(x1-x2)*(x1-x3))
    l2 = ((val-x0)*(val-x1)*(val-x3))/((x2-x0)*(x2-x1)*(x2-x3))
    l3 = ((val-x0)*(val-x1)*(val-x2))/((x3-x0)*(x3-x1)*(x3-x2))
    px = f0*l0 + f1*l1 + f2*l2 + f3*l3
    return px


def derivative(x0, n):
    x = symbols('x')
    f = log(tan(x), 10)
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
# Use the following values and four-digit rounding arithmetic to construct a third Lagrange polynomial approximation to f(1.09).
# The function being approximated is f(x) = log10(tan x). Use this knowledge to find a bound for the error in the approximation.
# f(1.00) = 0.1924, f(1.05) = 0.2414, f(1.10) = 0.2933, f(1.15) = 0.3492.
# Using f(1.00) = 0.1924, f(1.05) = 0.2414, f(1.10) = 0.2933, f(1.15) = 0.3492
# and four-digit rounding arithmetic to construct a third Lagrange polynomial approximation for f(1.09)
x0, x1, x2, x3, val = 1, 1.05, 1.1, 1.15, 1.09
res = thirdLagrange(x0, x1, x2, x3, val)
print('The third Lagrange polynomial approximation for f(1.09) is {}'.format(res))
print('The third Lagrange polynomial approximation for f(1.09) rounded to 4 decimal places is {}'.format(round(res, 4)))

# The bound for error in approximation:
print('The bound for the error in this approximation is {}'.format(maxError([x0, x1, x2, x3], val)))
