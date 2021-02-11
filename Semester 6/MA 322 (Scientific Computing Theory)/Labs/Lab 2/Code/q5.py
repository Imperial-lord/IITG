# Question 5 Lab Assignment 2
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------
from math import erf, pow
import numpy as np
import matplotlib.pyplot as plt

# functions --------------------------------------------------------------------


def f(x):
    return erf(x)


def monomialBasis(X, F):
    xArrayNN = []
    for x in X:
        row = []
        for i in range(X.shape[0]):
            row.append(pow(x, i))
        xArrayNN.append(row)
    xArrayNN = np.array(xArrayNN)
    A = np.linalg.solve(xArrayNN, F)
    A = np.flip(A)
    return A


def lagrangeBasis(X, F):
    L = []  # to store a list of all li(x) polynomials
    for x in X:
        l = np.array([1])
        for i in range(X.shape[0]):
            if(X[i] != x):
                l = np.polymul(l, np.array([1, -X[i]]))
                const = x-X[i]
                l = l/const
        L.append(l)
    A = L[0]*F[0]
    for i in range(1, len(L)):
        A += L[i]*F[i]
    return A


def newtonBasis(X, F):
    N = []  # to store a list of all Nj(x) polynomials
    temp = np.array([1])
    for i in range(X.shape[0]):
        N.append(temp)
        temp = np.polymul(temp, np.array([1, -X[i]]))

    xArrayNN = []
    for j in range(X.shape[0]):
        row = []
        for i in range(X.shape[0]):
            if(i > j):
                row.append(0)
            else:
                row.append(np.polyval(N[i], X[j]))
        xArrayNN.append(row)
    xArrayNN = np.array(xArrayNN)
    A = np.linalg.solve(xArrayNN, F)

    newtonPoly = A[0]*N[0]
    for i in range(1, A.shape[0]):
        newtonPoly = np.polyadd(newtonPoly, A[i]*N[i])
    return newtonPoly


# ------------------------------------------------------------------------------
# Prepare the inputs X and F. Here X = [x0,x1,...,xn] and F = [f0,f1,...,fn]
# Given X = [1,1.2,1.4...,3] in question
X = np.arange(1, 3.2, 0.2)
F = np.zeros(X.shape[0])
for i in range(X.shape[0]):
    F[i] = f(X[i])

# Compute the interpolating polynomial P(f[x1, . . . , xn]) using:
# (i) Monomial basis
pxMonomial = monomialBasis(X, F)
print('The interpolating polynomial using monomial basis is \n{}\n'.format(np.poly1d(pxMonomial)))

# (ii) Lagrange basis
pxLagrange = lagrangeBasis(X, F)
print('The interpolating polynomial using lagrange basis is \n{}\n'.format(np.poly1d(pxLagrange)))

# (iii) Newton basis
pxNewton = newtonBasis(X, F)
print('The interpolating polynomial using newton basis is \n{}\n'.format(np.poly1d(pxNewton)))

# Plot the error for each of the 3 cases with z = (0 : 0.01 : 4) (here, 0.01 is step size)
Z = np.arange(0, 4.01, 0.01)
errMonomial, errLagrange, errNewton = [], [], []
for z in Z:
    errMonomial.append(abs(f(z)-np.polyval(pxMonomial, z)))
    errLagrange.append(abs(f(z)-np.polyval(pxLagrange, z)))
    errNewton.append(abs(f(z)-np.polyval(pxNewton, z)))

plt.plot(Z, errMonomial, color='red')
plt.title('Error between erf and the interpolating polynomial using Monomial Basis vs Z values')
plt.xlabel('Z values - 0: 0.01 : 4')
plt.ylabel('Error between erf and the interpolating polynomial')
plt.show()

plt.plot(Z, errLagrange, color='green')
plt.title('Error between erf and the interpolating polynomial using Lagrange Basis vs Z values')
plt.xlabel('Z values - 0: 0.01 : 4')
plt.ylabel('Error between erf and the interpolating polynomial')
plt.show()

plt.plot(Z, errNewton, color='blue')
plt.title('Error between erf and the interpolating polynomial using Newton Basis vs Z values')
plt.xlabel('Z values - 0: 0.01 : 4')
plt.ylabel('Error between erf and the interpolating polynomial')
plt.show()

print(
    'As we can see from the plots, the error value becomes very high as we move out of the range [1 3] - especially towards 4')
print(
    'So it is not recommended to use polynomial interpolation to approximate erf at points outside [1 3]')

# Error between Monomial and Newton bases
errMonoNewton = []
Z = np.arange(1, 3.001, 0.001)
for z in Z:
    errMonoNewton.append(abs(np.polyval(pxMonomial, z)-np.polyval(pxNewton, z)))
plt.plot(Z, errMonoNewton)
plt.title('Error of the interpolating polynomial between using Monomial and Newton Bases vs Z values')
plt.xlabel('Z values - 1: 0.001 : 3')
plt.ylabel('Error the interpolating polynomials')
plt.show()

# Error between Lagrange and Newton bases
errLangNewton = []
Z = np.arange(1, 3.001, 0.001)
for z in Z:
    errLangNewton.append(abs(np.polyval(pxLagrange, z)-np.polyval(pxNewton, z)))
plt.plot(Z, errLangNewton)
plt.title('Error of the interpolating polynomial between using Lagrange and Newton Bases vs Z values')
plt.xlabel('Z values - 1: 0.001 : 3')
plt.ylabel('Error the interpolating polynomials')
plt.show()

# Find the one with max errors
Z = np.arange(1, 3.001, 0.001)
errMonomial, errLagrange, errNewton = [], [], []
for z in Z:
    errMonomial.append(abs(f(z)-np.polyval(pxMonomial, z)))
    errLagrange.append(abs(f(z)-np.polyval(pxLagrange, z)))
    errNewton.append(abs(f(z)-np.polyval(pxNewton, z)))
