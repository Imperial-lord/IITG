# Lab 08, Question 01
# AB Satyaprakash, 180123062

# imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pow, pi, cos, sin

# functions
# define these as per requirement!


def P(x):
    return 0


def Q(x):
    return 1


def R(x):
    return 1 + x


def A(i):
    return 1-h*P(x[i])/2


def B(i):
    return -2+(pow(h, 2)*Q(x[i]))


def C(i):
    return 1+h*P(x[i])/2


def y(x):
    return 1+x-cos(x)-(sin(x)*(1+pi/2))


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
# BVP : y' + y = 1 + x. Thus P = 1, Q = 1, R = 1 + x

a, b = 0, pi/2
alpha, beta = 0, 0
act = [y(1/2)]*5
sol, err, errratio = [], [], []
# dummy values
x = []
h = 0

HArray = [1/4, 1/8, 1/16, 1/32, 1/64]
for i in range(len(HArray)):
    h = HArray[i]
    x = np.arange(a, b+h/2, h)
    n = len(x)-1
    LArray, FArray = L(n), F(n)
    UArray = np.linalg.inv(LArray).dot(FArray)
    sol.append(UArray[int(1/(2*h))-1])
    err.append(abs(sol[i]-act[i]))
    errratio.append(abs(err[i]/sol[i]))

df = pd.DataFrame()
df['h'] = pd.Series(HArray)
df['y(1/2)'] = pd.Series(act)
df['f.d. solution at  1/2'] = pd.Series(sol)
df['error'] = pd.Series(err)
df['ratio of error (absolute)'] = pd.Series(errratio)
print()
print(df)
print()

# plot graph
h = 1/64
x = np.arange(a, b+h/2, h)
n = len(x)-1
LArray, FArray = L(n), F(n)
UArray = np.linalg.inv(LArray).dot(FArray)
UArray = np.append([0], UArray)
UArray = np.append(UArray, [0])
Act = []
for val in x:
    Act.append(y(val))


plt.plot(x, UArray, label='Finite Differences Solution')
plt.plot(x, Act, label='Exact Solution')
plt.xlabel('Value of x')
plt.ylabel('Exact Value / FD Value')
plt.title('Exact Solution and Finite Differences Solution for h = 1/64')
plt.legend()
plt.show()
