# Lab 08, Question 04
# AB Satyaprakash, 180123062

# imports
import numpy as np
import pandas as pd
from math import exp
import matplotlib.pyplot as plt

# functions


def P(x):
    return -10


def Q(x):
    return 0


def R(x):
    return 0


def y(x):
    return (exp(10*x)-1)/(exp(10)-1)


def genCentralMatrix():
    L = []
    xi = a+h
    n = int((b-a)/h) - 1
    for i in range(1, n+1):
        L1 = [0]*n
        if i-2 >= 0:
            L1[i-2] = 1 - h*P(xi)/2
        L1[i-1] = -2 + h*h*Q(xi)
        if i < n:
            L1[i] = 1+h*P(xi)/2
        L.append(L1)
        xi += h
    return np.array(L)


def genCentralVector():
    F = []
    xi = a+h
    n = int((b-a)/h) - 1
    for i in range(1, n+1):
        f = h*h*R(xi)
        if i == 1:
            f -= alpha*(1 - h*P(xi)/2)
        if i == n:
            f -= beta*(1 + h*P(xi)/2)
        F.append(f)
        xi += h
    return np.array(F)


def genBackwardMatrix():
    L = []
    xi = a+h
    n = int((b-a)/h) - 1
    for i in range(1, n+1):
        L1 = [0]*n
        if i-2 >= 0:
            L1[i-2] = 1 - h*P(xi)
        L1[i-1] = -2 + h*h*Q(xi) + h*P(xi)
        if i < n:
            L1[i] = 1
        L.append(L1)
        xi += h
    return np.array(L)


def genBackwardVector():
    F = []
    xi = a+h
    n = int((b-a)/h) - 1
    for i in range(1, n+1):
        f = h*h*R(xi)
        if i == 1:
            f -= alpha*(1 - h*P(xi))
        if i == n:
            f -= beta
        F.append(f)
        xi += h
    return np.array(F)


def genForwardMatrix():
    L = []
    xi = a+h
    n = int((b-a)/h) - 1
    for i in range(1, n+1):
        L1 = [0]*n
        if i-2 >= 0:
            L1[i-2] = 1
        L1[i-1] = -2 + h*h*Q(xi) - h*P(xi)
        if i < n:
            L1[i] = 1 + h*P(xi)
        L.append(L1)
        xi += h
    return np.array(L)


def genForwardVector():
    F = []
    xi = a+h
    n = int((b-a)/h) - 1
    for i in range(1, n+1):
        f = h*h*R(xi)
        if i == 1:
            f -= alpha
        if i == n:
            f -= beta*(1 + h*P(xi))
        F.append(f)
        xi += h
    return np.array(F)


# program body
# BVP : y" - 10y' = 0. Thus P = -10, Q = 0, R = 0
a, b = 0, 1
alpha, beta = 0, 1
h = 1/4

L = genCentralMatrix()
F = genCentralVector()
U = np.linalg.inv(L).dot(F)
Y_c = [alpha]
for u in U:
    Y_c.append(u)
Y_c.append(beta)
Y1 = [y(a+i*h) for i in range(len(Y_c))]
df = pd.DataFrame()
df['Nodal points'] = pd.Series(['0', '1/4', '2/4', '3/4', '1'])
df['Actual'] = pd.Series(Y1)
df['Central Approximation'] = pd.Series(Y_c)
df['Central Error'] = pd.Series(abs(np.array(Y1)-np.array(Y_c)))

L = genBackwardMatrix()
F = genBackwardVector()
U = np.linalg.inv(L).dot(F)
Y_b = [alpha]
for u in U:
    Y_b.append(u)
Y_b.append(beta)
df['Backward Approximation'] = pd.Series(Y_b)
df['Backward Error'] = pd.Series(abs(np.array(Y1)-np.array(Y_b)))

L = genForwardMatrix()
F = genForwardVector()
U = np.linalg.inv(L).dot(F)
Y_f = [alpha]
for u in U:
    Y_f.append(u)
Y_f.append(beta)
df['Forward Approximation'] = pd.Series(Y_f)
df['Forward Error'] = pd.Series(abs(np.array(Y1)-np.array(Y_f)))
print()
print(df)
print()

NodalPoints = [0, 1/4, 2/4, 3/4, 1]
plt.plot(NodalPoints, df['Central Error'], label='Central Scheme')
plt.plot(NodalPoints, df['Backward Error'], label='Backward Scheme')
plt.plot(NodalPoints, df['Forward Error'], label='Forward Scheme')
plt.xlabel('Nodal Points')
plt.ylabel('Error Magnitude')
plt.title('Errors using different schemes for dy/dx')
plt.legend()
plt.show()
