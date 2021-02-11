# Question 2 Lab Assignment 2
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------
# none needed for this question

# functions --------------------------------------------------------------------


def f(x):
    # for (i)
    if x == 8.1:
        return 16.94410
    if x == 8.3:
        return 17.56492
    if x == 8.6:
        return 18.50515
    if x == 8.7:
        return 18.82091

    # for (ii)
    if x == -0.75:
        return -0.07181250
    if x == -0.5:
        return -0.02475000
    if x == -0.25:
        return 0.33493750
    if x == 0:
        return 1.10100000


def linearLagrange(x0, x1, val):
    f0, f1 = f(x0), f(x1)

    # compute l0(x) with x = val
    l0 = (val-x1)/(x0-x1)
    l1 = (val-x0)/(x1-x0)
    px = f0*l0 + f1*l1
    return px


def secondLagrange(x0, x1, x2, val):
    f0, f1, f2 = f(x0), f(x1), f(x2)

    # compute l0(x) with x = val
    l0 = ((val-x1)*(val-x2))/((x0-x1)*(x0-x2))
    l1 = ((val-x0)*(val-x2))/((x1-x0)*(x1-x2))
    l2 = ((val-x0)*(val-x1))/((x2-x0)*(x2-x1))
    px = f0*l0 + f1*l1 + f2*l2
    return px


def thirdLagrange(x0, x1, x2, x3, val):
    f0, f1, f2, f3 = f(x0), f(x1), f(x2), f(x3)

    # compute l0(x) with x = val
    l0 = ((val-x1)*(val-x2)*(val-x3))/((x0-x1)*(x0-x2)*(x0-x3))
    l1 = ((val-x0)*(val-x2)*(val-x3))/((x1-x0)*(x1-x2)*(x1-x3))
    l2 = ((val-x0)*(val-x1)*(val-x3))/((x2-x0)*(x2-x1)*(x2-x3))
    l3 = ((val-x0)*(val-x1)*(val-x2))/((x3-x0)*(x3-x1)*(x3-x2))
    px = f0*l0 + f1*l1 + f2*l2 + f3*l3
    return px


# ------------------------------------------------------------------------------
# (i) Approximate f(8.4) if f(8.1) = 16.94410, f(8.3) = 17.56492, f(8.6) = 18.50515, f(8.7) = 18.82091
x0, x1, x2, x3, val = 8.1, 8.3, 8.6, 8.7, 8.4
resLin = linearLagrange(x1, x2, val)  # since 8.4 is between 8.3 and 8.6
resSec = secondLagrange(x0, x1, x2, val)
resThi = thirdLagrange(x0, x1, x2, x3, val)
print('Approximation of f(8.4) using the  Lagrange interpolating polynomials of degrees one, two, and three are:')
print('Degree 1 = {}'.format(resLin))
print('Degree 2 = {}'.format(resSec))
print('Degree 3 = {}'.format(resThi))

print('\n')
# (ii) Approximate f(-1/3) if f(−0.75) = −0.07181250, f(−0.5) = −0.02475000, f(−0.25) = 0.33493750, f(0) = 1.10100000
x0, x1, x2, x3, val = -0.75, -0.5, -0.25, 0, (-1/3)
resLin = linearLagrange(x1, x2, val)  # since -1/3 is between -0.5 and -0.25
resSec = secondLagrange(x0, x1, x2, val)
resThi = thirdLagrange(x0, x1, x2, x3, val)
print('Approximation of f(-1/3) using the  Lagrange interpolating polynomials of degrees one, two, and three are:')
print('Degree 1 = {}'.format(resLin))
print('Degree 2 = {}'.format(resSec))
print('Degree 3 = {}'.format(resThi))
