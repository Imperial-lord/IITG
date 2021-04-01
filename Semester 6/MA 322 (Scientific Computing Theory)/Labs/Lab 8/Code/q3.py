# Lab 08, Question 03
# AB Satyaprakash, 180123062

# imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pow, pi, exp

# functions
# define these as per requirement!


def P(x):
    return -1


def Q(x):
    return 0


def R(x):
    return 1


def A(i):
    return 1-h*P(x[i])/2


def B(i):
    return -2+(pow(h, 2)*Q(x[i]))


def C(i):
    return 1+h*P(x[i])/2


def y(x):
    return 2*exp(x) - x-1


def L(n):
    LArray = np.zeros((n-1, n-1))
    for i in range(n-1):
        if i == 0:
            LArray[0][0], LArray[0][1] = B(1), C(1)
        elif i == n-2:
            LArray[n-2][n-3], LArray[n-2][n-2] = A(n-1), B(n-1)
        else:
            LArray[i][i-1], LArray[i][i], LArray[i][i +
                                                    1] = A(i+1), B(i+1), C(i+1)
    return LArray


def F(n):
    FArray = []
    for i in range(n-1):
        if i == 0:
            FArray.append((pow(h, 2)*R(x[1]))-(alpha*(1-h*P(x[1])/2)))
        elif i == n-2:
            FArray.append((pow(h, 2)*R(x[n-1]))-(beta*(1+h*P(x[n-1])/2)))
        else:
            FArray.append(pow(h, 2)*R(x[i+1]))
    return FArray


# program body
# BVP : y" = y+1. Thus P = -1, Q = 0, R = 1

a, b = 0, 1
alpha, beta = 1, 2*(exp(1)-1)
sol, err = [], []
x = []
h = 1/3
x = np.arange(a, b+h/2, h)
n = len(x)-1
LArray, FArray = L(n), F(n)
UArray = np.linalg.inv(LArray).dot(FArray)
Y = [alpha]
for u in UArray:
    Y.append(u)
Y.append(beta)
Act = []
for xi in x:
    Act.append(y(xi))

df = pd.DataFrame()
df['Nodal points'] = pd.Series(['0', '1/3', '2/3', '1'])
df['Actual'] = pd.Series(Act)
df['Approx'] = pd.Series(Y)
df['Error'] = pd.Series(np.array(Act)-np.array(Y))
print()
print(df)
print()
