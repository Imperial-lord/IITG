# Lab 08, Question 02
# AB Satyaprakash, 180123062

# imports
import numpy as np
import pandas as pd
from math import sin, pi
import matplotlib.pyplot as plt

# functions


def f(x):
    return sin(x)


def P(x):
    return 0


def Q(x):
    return 0


def A(xi, h):
    return (1 - h*P(xi)/2)


def B(xi, h):
    return (-2 + h*h*Q(xi))


def C(xi, h):
    return (1 + h*P(xi)/2)


def L(x, h):

    n = len(x)-1

    LArray = []
    for i in range(1, n):

        temp = [0]*(n-1)
        if i == 1:
            temp[i] = C(x[i], h)
            temp[i-1] = B(x[i], h)

        elif i < n-1:
            temp[i] = C(x[i], h)
            temp[i-1] = B(x[i], h)
            temp[i-2] = A(x[i], h)

        else:

            temp[i-1] = B(x[i], h)
            temp[i-2] = A(x[i], h)

        LArray.append(temp)

    return LArray


def F(x, h):

    n = len(x)-1

    FArray = []
    for i in range(1, n):
        term = -h*h*(f(x[i]) + (f(x[i-1]) - 2*f(x[i]) + f(x[i+1]))/12)
        FArray.append(term)

    return FArray


def getX(a, b, n):
    return np.linspace(a, b, n)


# program body
N = [10, 20, 40, 80, 160, 320]

a, b = 0, 2*pi
alpha, beta = 0, 0

max_errors = []
l2_errors = []

for n in N:
    x = getX(a, b, n)
    h = (b-a)/n

    LArray = L(x, h)
    FArray = F(x, h)

    V = np.linalg.inv(LArray).dot(FArray)

    V = np.append(alpha, V)
    V = np.append(V, beta)

    U = [f(xi) for xi in x]
    U = np.array(U)

    err = abs(U - V)
    max_error = np.max(err)
    l2_error = np.sum(err**2)

    max_errors.append(max_error)
    l2_errors.append(l2_error)


df = pd.DataFrame(
    {'Grid Points': N, 'Max Error': max_errors, 'L2 Norm Error': l2_errors})
print()
print(df)
print()


plt.plot(N, max_errors, color='blue')
plt.xlabel('Number of Grid Points')
plt.ylabel('Max Error')
plt.title('Max error plot vs N')
plt.show()


plt.loglog()
plt.plot(N, max_errors, color='orange')
plt.xlabel('Number of Grid Points')
plt.ylabel('Max Error')
plt.title('Max error plot vs N (log-log)')
plt.show()


plt.plot(N, l2_errors, color='blue')
plt.xlabel('Number of Grid Points')
plt.ylabel('L2 Error')
plt.title('L2 error plot vs N')
plt.show()


plt.loglog()
plt.plot(N, l2_errors, color='orange')
plt.xlabel('Number of Grid Points')
plt.ylabel('L2 Error')
plt.title('L2 error plot vs N (log-log)')
plt.show()
