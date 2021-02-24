# Question 06, Lab 04
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------
from sympy.abc import t
from sympy import evalf, integrate, sqrt, sin
from math import pi
import numpy as np
import pandas as pd

# functions --------------------------------------------------------------------------


def f(func, x):
    return func.subs(t, x)


def getX(a, b, n):
    h = (b-a)/n
    return np.arange(a, b+h/2, h)


def compositeTrapezoidalRule(func, X, mapf, count):
    sum = 0
    a, b = X[0], X[-1]
    n = X.shape[0]
    h = (b-a)/(n-1)
    cnt = count
    for i in range(X.shape[0]):
        x = X[i]
        if(mapf.get(x) == None):
            mapf[x] = f(func, x)
            val = mapf[x]
            cnt += 1
        else:
            val = mapf[x]
        if(i == 0 or i == n-1):
            sum += val/2
        else:
            sum += val
    return (h*sum), cnt


# program body
# part (a)
func = t/(1+t**2)
a, b = 0, 3
mapf = {}
n = 1
count = 0

H_2, TH_2, errorArray = [], [], []
while(True):
    h = (b-a)/n
    X = getX(a, b, n)
    Th, count = compositeTrapezoidalRule(func, X, mapf, count)
    X = getX(a, b, 2*n)
    Th_2, count = compositeTrapezoidalRule(func, X, mapf, count)
    err = abs(Th-Th_2)/abs(Th_2)
    # append values to tabulate later on
    H_2.append(h/2)
    TH_2.append(Th_2)
    errorArray.append(err)
    # error break condition
    if(err < 10**(-6)):
        break
    n *= 2

print('For part a:')
H_2, TH_2, errorArray = np.array(H_2), np.array(TH_2), np.array(errorArray)
data = np.vstack((H_2, TH_2, errorArray)).T
df = pd.DataFrame(data,
                  columns=['h/2', 'T(h/2)', '|T(h)-T(h/2)|/|T(h/2)|'])
print('\n', df.round(6), '\n')
print('Estimated value of integral is', TH_2[-1])
print('The total number of function evaluations f(x) is', count)
print('\n')


# part (b)
func = 1/(1-t)
a, b = 0, 0.95
mapf = {}
n = 1
count = 0
H_2, TH_2, errorArray = [], [], []
while(True):
    h = (b-a)/n
    X = getX(a, b, n)
    Th, count = compositeTrapezoidalRule(func, X, mapf, count)
    X = getX(a, b, 2*n)
    Th_2, count = compositeTrapezoidalRule(func, X, mapf, count)
    err = abs(Th-Th_2)/abs(Th_2)
    # append values to tabulate later on
    H_2.append(h/2)
    TH_2.append(Th_2)
    errorArray.append(err)
    # error break condition
    if(err < 10**(-6)):
        break
    n *= 2

print('For part b:')
H_2, TH_2, errorArray = np.array(H_2), np.array(TH_2), np.array(errorArray)
data = np.vstack((H_2, TH_2, errorArray)).T
df = pd.DataFrame(data,
                  columns=['h/2', 'T(h/2)', '|T(h)-T(h/2)|/|T(h/2)|'])
print('\n', df.round(6), '\n')
print('Estimated value of integral is', TH_2[-1])
print('The total number of function evaluations f(x) is', count)
print('\n')


# part (c)
M = [0.5, 0.8, 0.95]
for i in range(3):
    m = M[i]
    func = 1/sqrt(1-m*(sin(t)**2))
    a, b = 0, pi/2
    mapf = {}
    n = 1
    count = 0
    H_2, TH_2, errorArray = [], [], []
    while(True):
        h = (b-a)/n
        X = getX(a, b, n)
        Th, count = compositeTrapezoidalRule(func, X, mapf, count)
        X = getX(a, b, 2*n)
        Th_2, count = compositeTrapezoidalRule(func, X, mapf, count)
        err = abs(Th-Th_2)/abs(Th_2)
        # append values to tabulate later on
        H_2.append(h/2)
        TH_2.append(Th_2)
        errorArray.append(err)
        # error break condition
        if(err < 10**(-6)):
            break
        n *= 2

    print('For part c.{} with m = {}:'.format(i+1, m))
    H_2, TH_2, errorArray = np.array(H_2), np.array(TH_2), np.array(errorArray)
    data = np.vstack((H_2, TH_2, errorArray)).T
    df = pd.DataFrame(data,
                      columns=['h/2', 'T(h/2)', '|T(h)-T(h/2)|/|T(h/2)|'])
    print('\n', df, '\n')
    print('Estimated value of integral is', TH_2[-1])
    print('The total number of function evaluations f(x) is', count)
    print('\n')
