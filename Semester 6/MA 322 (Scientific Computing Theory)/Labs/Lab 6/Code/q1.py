# Question 1, Lab 6
# AB Satyaprakash, 180123062

# imports 
from sympy.abc import t,y
import numpy as np
import sympy as sp

# functions 
def getEulerApproximation(f,X,Y,h):
    for i in range(1,Y.shape[0]):
        Y[i]=Y[i-1] + (f.subs({t:X[i-1], y:Y[i-1]})*h)

# program body
# Case (A):
# t belongs to [0,1] and y(0)=1, with h = 0.5
a, b, h = 0, 1, 0.5
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Y[0] = 1

f = sp.exp(t-y) # from question
getEulerApproximation(f,X,Y,h)
print('(a)')
print('The approx solution in this case is given as:')
for i in range(X.shape[0]):
    print('y({}) = {}'.format(X[i],Y[i]))



# Case (B):
# t belongs to [1,2] and y(1)=2, with h = 0.5
a, b, h = 1, 2, 0.5
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Y[0] = 2

f = (1+t)/(1+y) # from question
getEulerApproximation(f,X,Y,h)
print('(b)')
print('The approx solution in this case is given as:')
for i in range(X.shape[0]):
    print('y({}) = {}'.format(X[i],Y[i]))



# Case (C):
# t belongs to [2,3] and y(2)=2, with h = 0.25
a, b, h = 2, 3, 0.25
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Y[0] = 2

f = -y+(t*sp.sqrt(y)) # from question
getEulerApproximation(f,X,Y,h)
print('(c)')
print('The approx solution in this case is given as:')
for i in range(X.shape[0]):
    print('y({}) = {}'.format(X[i],Y[i]))



# Case (D):
# t belongs to [1,2] and y(1)=2, with h = 0.25
a, b, h = 1, 2, 0.25
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Y[0] = 2

f = (sp.sin(2*t)-(2*t*y))/(t*t) # from question
getEulerApproximation(f,X,Y,h)
print('(d)')
print('The approx solution in this case is given as:')
for i in range(X.shape[0]):
    print('y({}) = {}'.format(X[i],Y[i]))
