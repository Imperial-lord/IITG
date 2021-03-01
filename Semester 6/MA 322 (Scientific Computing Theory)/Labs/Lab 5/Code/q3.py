# Question 03, Lab 05
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------
from math import log, sin, pi
from sympy.abc import t
import numpy as np
import pandas as pd
import sympy as sp

# global dictionaries ----------------------------------------------------------------
phi = {-1: 0, 0: 1}
alpha = {}
beta = {0: 0}

# functions --------------------------------------------------------------------------


def trapezoidalRule(f, a, b):
    return (((b-a)/2)*(f.subs(t, a)+f.subs(t, b))).evalf()


def simpsonRule(f, a, b):
    return (((b-a)/6)*(f.subs(t, a)+4*f.subs(t, (a+b)/2)+f.subs(t, b))).evalf()


def getFuncVal(x):
    return 1/(x+2)


def getInnerProduct(a, b):
    poly = np.poly1d(np.polyint(np.polymul(a, b)))
    return poly(1) - poly(-1)


def getPhi(n):
    # The value of ϕ(n) = (x-α(n-1))ϕ(n-1) - β(n)ϕ(n-2)
    if n in phi:
        return phi[n]

    a = getAlpha(n-1)
    b = getBeta(n-1)
    phi_n_1 = getPhi(n-1)
    phi_n_2 = getPhi(n-2)

    secondTerm = np.polymul([b], phi_n_2)
    firstTerm = np.polymul(np.polysub([1, 0], a), phi_n_1)
    phi[n] = np.polysub(firstTerm, secondTerm)
    return phi[n]


def getAlpha(n):
    # The value of α(n) = <xϕ(n), ϕ(n)>/<ϕ(n) , ϕ(n)>
    if n in alpha:
        return alpha[n]

    phi_n = getPhi(n)
    xphi_n = np.polymul([1, 0], phi_n)
    num = getInnerProduct(xphi_n, phi_n)
    denom = getInnerProduct(phi_n, phi_n)
    alpha[n] = num/denom

    return alpha[n]


def getBeta(n):
    # The value of β(n) = <ϕ(n), ϕ(n)>/<ϕ(n-1) , ϕ(n-1)>
    if n in beta:
        return beta[n]

    phi_n = getPhi(n)
    phi_n_1 = getPhi(n-1)
    num = getInnerProduct(phi_n, phi_n)
    denom = getInnerProduct(phi_n_1, phi_n_1)
    beta[n] = num/denom

    return beta[n]


def getGaussian(roots, W, limits):
    a, b = limits
    I = 0
    for x, w in zip(roots, W):
        I += w*f(x, a, b)
    return I


def f(x, a, b):
    c1, c2 = (b-a)/2, (b+a)/2
    x = c1*x + c2
    return c1*getFuncVal(x)


# program body
# using 2 point Gaussian Quadrature rule!
n = 2
poly = np.poly1d(getPhi(n))
roots = poly.r
roots.sort()
temp = [[1] + [0]*(i) for i in range(n)]

output = []
for P in temp:
    P = (np.polyint(P))
    P = np.poly1d(P)
    I = P(1) - P(-1)
    output.append(I)

X = []
for i in range(n):
    temp = [x**i for x in roots]
    X.append(temp)
X_ = np.linalg.inv(X)
W = np.dot(X_, output)

# Given integral = ∫1/(x+2) from -1 to 1
limits = (-1, 1)
result = getGaussian(roots, W, limits)
print("Using 2 point Gaussian Quadrature rule approx. value of integral is {}".format(result))

func = 1/(t+2)
trapezoidalValue = trapezoidalRule(func, -1, 1)
simpsonValue = simpsonRule(func, -1, 1)
print("Using Trapezoidal rule approximate value of the integral is {}".format(
    trapezoidalValue))
print("Using Simpson's rule approximate value of the integral is {}".format(simpsonValue))


actualIntegratedValue = sp.integrate(func, (t, -1, 1)).evalf()
print("Actual value of integral is {}".format(
    actualIntegratedValue))

print('\n------------------------------------------------------------\n')
print("Error in estimation for Gaussain Quadrature rule = {}".format(
    abs(actualIntegratedValue-result)))
print("Error in estimation for Trapezoidal rule = {}".format(
    abs(actualIntegratedValue-trapezoidalValue)))
print("Error in estimation for Simpson's rule = {}".format(
    abs(actualIntegratedValue-simpsonValue)))
