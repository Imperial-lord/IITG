# Question 01, Lab 05
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


def getFuncValA(x):
    return (x**2)*log(x)


def getFuncValB(x):
    return 2/(x**2 - 4)


def getFuncValC(x):
    return (x**2)*sin(x)


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


def getGaussian(roots, W, limits, case):
    a, b = limits
    I = 0
    for x, w in zip(roots, W):
        I += w*f(x, a, b, case)
    return I


def f(x, a, b, case):
    c1, c2 = (b-a)/2, (b+a)/2
    x = c1*x + c2
    if(case == 0):
        return c1*getFuncValA(x)
    elif(case == 1):
        return c1*getFuncValB(x)
    else:
        return c1*getFuncValC(x)


# program body
# Using Gaussian Quadrature rule with n=2!
n = 3
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

# Part (a) ∫x**2(lnx)dx from 1 to 1.5
print("(a) Using Gaussian Quadrature with n = 2")
limits = (1, 1.5)
result = getGaussian(roots, W, limits, 0)
print("Approximate value of integral is {}".format(result))

expr = (t**2)*sp.log(t)
integratedVal = sp.integrate(expr, (t, 1, 1.5))
print("Exact value of the integral is {}".format(integratedVal))
print("Error in estimation is {}\n".format(abs(integratedVal-result)))


# Part (b) ∫2/(x^2-4)dx from 0 to 0.35
print("(b) Using Gaussian Quadrature with n = 2")
limits = (0, 0.35)
result = getGaussian(roots, W, limits, 1)
print("Approximate value of integral is {}".format(result))

expr = 2/(t**2 - 4)
integratedVal = sp.integrate(expr, (t, 0, 0.35))
print("Exact value of the integral is {}".format(integratedVal))
print("Error in estimation is {}\n".format(abs(integratedVal-result)))


# Part (c) ∫(x^2)sinxdx from 0 to pi/4
print("(c) Using Gaussian Quadrature with n = 2")
limits = (0, pi/4)
result = getGaussian(roots, W, limits, 2)
print("Approximate value of integral is {}".format(result))

expr = (t**2)*sp.sin(t)
integratedVal = sp.integrate(expr, (t, 0, pi/4))
print("Exact value of the integral is {}".format(integratedVal))
print("Error in estimation is {}\n".format(abs(integratedVal-result)))
