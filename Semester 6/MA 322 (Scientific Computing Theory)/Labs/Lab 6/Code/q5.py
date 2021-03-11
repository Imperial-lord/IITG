# Question 1, Lab 6
# AB Satyaprakash, 180123062

# imports 
from sympy.abc import t,y
import numpy as np
import sympy as sp
import pandas as pd

# functions 
def getEulerApproximation(f,X,Y,h):
    for i in range(1,Y.shape[0]):
        Y[i]=Y[i-1] + (f.subs({t:X[i-1], y:Y[i-1]})*h)

def getActualValues(g,X):
    for i in range(X.shape[0]):
        Z[i]=g.subs(t,X[i])

# program body
# t belongs to [0,3] and y(0)=0, with h = 0.5
a, b, h = 0, 3, 0.5
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Z = np.zeros(X.shape[0])
Y[0] = 0

f = -20*y + sp.cos(t) + 20*sp.sin(t) # from question
g = sp.sin(t)

getEulerApproximation(f,X,Y,h)
getActualValues(g,X)
print('Approximate value of y({}) = {}'.format(3,Y[-1]))
print('The actual value of y({}) = {}'.format(3, Z[-1]))
print('The error in this case = {}'.format(abs(Y[-1]-Z[-1])))

# Error bound is nh^2Y, where Y = 1/2(max|y"(x)|) for x in {x0,x1..xn}
func = sp.sin(t)
func = sp.diff(sp.diff(func,t),t)
n = X.shape[0]-1
maxi = 0
for x in X:
    maxi=max(maxi,abs(func.subs(t,x)))
K = maxi/2
errorBound = n*(h**2)*K
print('The error bound in this case = {}'.format(errorBound))
print('Clearly, absolute error with h = 0.5 greatly exceeds the error bound computed using (I) in Q4\n')


print('If we reduce h by 10 times, i.e make it 0.05 we observe that:')
a, b, h = 0, 3, 0.05
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Z = np.zeros(X.shape[0])
Y[0] = 0
getEulerApproximation(f,X,Y,h)
getActualValues(g,X)
print('Approximate value of y({}) = {}'.format(3,Y[-1]))
print('The actual value of y({}) = {}'.format(3, Z[-1]))
print('The error in this case = {}'.format(abs(Y[-1]-Z[-1])))
