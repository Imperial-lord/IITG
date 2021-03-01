# Question 06, Lab 05
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------
from math import cos, log, sin, pi
from sympy.abc import t
import numpy as np
import pandas as pd
import sympy as sp
from scipy.integrate import quad

# global dictionaries ----------------------------------------------------------------
phi = {-1: 0, 0: 1}
alpha = {}
beta = {0: 0}

# functions --------------------------------------------------------------------------


def getFuncVal(x):
    # cosx log(sinx)/(1 + sin^2(x))
    return (cos(x)*log(sin(x))/(1+sin(x)**2))


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


def getGaussian(f, roots, W, limits):
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
table = []
for k in range(1, 6):
    n = k+1
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

    limits = (0, pi/2)
    result = getGaussian(f, roots, W, limits)
    table.append([k, round(result, 2)])


df = pd.DataFrame(
    table, columns=['N', 'Evaluated value using N+1 point Gaussian Quadrature'])
print(df)


ans, _ = quad(getFuncVal, 0, pi/2)
print("The actual value of the integral is", ans)
