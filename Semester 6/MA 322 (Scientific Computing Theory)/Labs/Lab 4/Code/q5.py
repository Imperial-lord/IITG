# Question 05, Lab 04
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------
from sympy.abc import t
from sympy import evalf, integrate
from math import ceil, sqrt
import numpy as np

# functions --------------------------------------------------------------------------


def f(x):
    return 1/(x+4)


def errorCompositeTrapezoidal(a, b):
    err = 10**(-5)
    d2fmax = 1/32
    val = (1/err)*(b-a)*(b-a)*(b-a)*(1/12)*d2fmax
    n = ceil(sqrt(val))
    print("Constraints :", "h <=", (b-a)/sqrt(val), "and n >=", n)
    return n


def errCompositeSimpson(a, b):
    err = 10**(-5)
    d4fmax = 24/(4**5)
    val = (1/err)*pow(b-a, 5)*(1/180)*d4fmax
    n = ceil(sqrt(sqrt(val)))
    if n % 2 == 0:
        print("Constraints :", "h <=", (b-a) /
              sqrt(sqrt(val)), "and n >=", n)
        return n
    else:
        print("Constraints :", "h <=", (b-a) /
              sqrt(sqrt(val)), "and n >=", n+1)
        return n+1


def errCompositeMidpoint(a, b):
    err = 10**(-5)
    d2fmax = 1/32
    val = (1/err)*(b-a)*(b-a)*(b-a)*(1/6)*d2fmax
    n = ceil(sqrt(val))
    if n % 2 == 0:
        print("Constraints :", "h <=", (b-a)/sqrt(val), "and n >=", n)
        return n
    else:
        print("Constraints :", "h <=", (b-a)/sqrt(val), "and n >=", n+1)
        return n+1


def compositeTrapezoidalRule(X):
    sum = 0
    a, b = X[0], X[-1]
    n = X.shape[0]
    h = (b-a)/(n-1)
    for i in range(n):
        x = X[i]
        if(i == 0 or i == n-1):
            sum += f(x)/2
        else:
            sum += f(x)
    return (h*sum)


def compositeSimpsonRule(X):
    sum = 0
    a, b = X[0], X[-1]
    n = X.shape[0]
    h = (b-a)/(n-1)
    for i in range(n):
        x = X[i]
        if(i == 0 or i == n-1):
            sum += f(x)
        else:
            if(i % 2 == 0):
                sum += 2*f(x)
            else:
                sum += 4*f(x)
    return (h*sum)/3


def compositeMidpointRule(X):
    a, b = X[0], X[-1]
    n = X.shape[0]-1
    h = (b-a)/(n)
    sum = 0
    for i in range(n):
        xi = a+i*h
        xi_nex = a+(i+1)*h
        pt = (xi+xi_nex)/2
        sum += f(pt)
    return h*sum


# program body
func = 1/(t+4)
a, b = 0, 2


I = integrate(func, (t, a, b)).evalf()
print('Actual value of integral is', I)

print("\nFor part a: (Trapezoidal Rule)")
n = errorCompositeTrapezoidal(a, b)
h = (b-a)/n
X = np.arange(a, b+h/2, h)
estimatedIntegral = compositeTrapezoidalRule(X)
print('Required tuple (n,h) with error < 0.00001 is ({}, {})'.format(n, h))
print('Estimated value of integral is', estimatedIntegral)
print('Error in this case is', abs(estimatedIntegral-I))

print("\nFor part b: (Simpson Rule)")
n = errCompositeSimpson(a, b)
h = (b-a)/n
X = np.arange(a, b+h/2, h)
estimatedIntegral = compositeSimpsonRule(X)
print('Required tuple (n,h) with error < 0.00001 is ({}, {})'.format(n, h))
print('Estimated value of integral is', estimatedIntegral)
print('Error in this case is', abs(estimatedIntegral-I))

print("\nFor part c: (Midpoint Rule)")
n = errCompositeMidpoint(a, b)
h = (b-a)/n
X = np.arange(a, b+h/2, h)
estimatedIntegral = compositeMidpointRule(X)
print('Required tuple (n,h) with error < 0.00001 is ({}, {})'.format(n, h))
print('Estimated value of integral is', estimatedIntegral)
print('Error in this case is', abs(estimatedIntegral-I))
