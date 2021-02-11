# Question 1 Lab Assignment 2
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------
from math import exp

# functions --------------------------------------------------------------------


def f(x):
    return exp(x)


def linearLagrange(x0, x1, val):
    # The given function here is exp(x)
    f0, f1 = f(x0), f(x1)

    # compute l0(x) with x = val
    l0 = (val-x1)/(x0-x1)
    l1 = (val-x0)/(x1-x0)
    px = f0*l0 + f1*l1
    return px


def secondLagrange(x0, x1, x2, val):
    # The given function here is exp(x)
    f0, f1, f2 = f(x0), f(x1), f(x2)

    # compute l0(x) with x = val
    l0 = ((val-x1)*(val-x2))/((x0-x1)*(x0-x2))
    l1 = ((val-x0)*(val-x2))/((x1-x0)*(x1-x2))
    l2 = ((val-x0)*(val-x1))/((x2-x0)*(x2-x1))
    px = f0*l0 + f1*l1 + f2*l2
    return px


# ------------------------------------------------------------------------------
# Getting the actual values at 0.25 and 0.75
f_25, f_75 = f(0.25), f(0.75)

# (i) For x0 = 0, x1 =0.5, find f(0.25), or val = 0.25
x0, x1, val = 0, 0.5, 0.25
res = linearLagrange(x0, x1, val)
errorlin_25 = abs(f_25-res)
print('Approximation of f(0.25) using linear Lagrange interpolation with x0 = 0 and x1 = 0.5 is {}'.format(res))

# (ii) For x0 = 0.5, x1 =1, find f(0.75), or val = 0.75
x0, x1, val = 0.5, 1, 0.75
res = linearLagrange(x0, x1, val)
errorlin_75 = abs(f_75-res)
print('Approximation of f(0.75) using linear Lagrange interpolation with x0 = 0.5 and x1 = 1 is {}'.format(res))

# (iii) For x0 = 0, x1 = 1, and x2 = 2, find f(0.25) and f(0.75)
x0, x1, x2 = 0, 1, 2
# Case A: val = 0.25
val = 0.25
res = secondLagrange(x0, x1, x2, val)
errorsec_25 = abs(f_25-res)
print('Approximation of f(0.25) using second Lagrange interpolating polynomial with x0 = 0, x1 = 1, and x2 = 2 is {}'.format(res))

# Case B: val = 0.75
val = 0.75
res = secondLagrange(x0, x1, x2, val)
errorsec_75 = abs(f_75-res)
print('Approximation of f(0.75) using second Lagrange interpolating polynomial with x0 = 0, x1 = 1, and x2 = 2 is {}'.format(res))

# (iv)  Which approximations are better and why?
# We find the difference between actual and obtained values at 0.25 and 0.75 to see which is a better approximation
print('\n')
print('Error for linear approximation of f(0.25) is {}'.format(errorlin_25))
print('Error for linear approximation of f(0.75) is {}'.format(errorlin_75))
print('Error for second polynomial approximation of f(0.25) is {}'.format(errorsec_25))
print('Error for second polynomial approximation of f(0.75) is {}'.format(errorsec_75))
print('Clearly, linear Lagrange interpolation gives a better approximation to obtain f(0.25) and f(0.75)')
