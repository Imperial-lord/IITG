# Question 2, Lab 6
# AB Satyaprakash, 180123062

# imports 
from sympy.abc import t,y
import numpy as np
import sympy as sp

# functions 
def getEulerApproximation(f,X,Y,h):
    for i in range(1,Y.shape[0]):
        Y[i]=Y[i-1] + f.subs({t:X[i-1], y:Y[i-1]})*h

def getActualValues(g,X):
    for i in range(X.shape[0]):
        Z[i]=g.subs(t,X[i])


# program body
# Case (A):
# t belongs to [0,1] and y(0)=1, with h = 0.5
a, b, h = 0, 1, 0.5
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Z = np.zeros(X.shape[0])
Y[0] = 1

f = sp.exp(t-y) # from question
g = sp.log(sp.exp(t)+sp.exp(1)-1)

getEulerApproximation(f,X,Y,h)
getActualValues(g,X)
print('(a)')
print('Approx Sol: {}'.format(Y))
print('Exact Sol: {}'.format(Z))
for i in range(X.shape[0]):
    print('Error for y({}) = {}'.format(X[i],abs(Y[i]-Z[i])))



# Case (B):
# t belongs to [1,2] and y(1)=2, with h = 0.5
a, b, h = 1, 2, 0.5
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Z = np.zeros(X.shape[0])
Y[0] = 2

f = (1+t)/(1+y) # from question
g = sp.sqrt(t*t + 2*t +6)-1

getEulerApproximation(f,X,Y,h)
getActualValues(g,X)

print('(b)')
print('Approx Sol: {}'.format(Y))
print('Exact Sol: {}'.format(Z))
for i in range(X.shape[0]):
    print('Error for y({}) = {}'.format(X[i],abs(Y[i]-Z[i])))



# Case (C):
# t belongs to [2,3] and y(2)=2, with h = 0.25
a, b, h = 2, 3, 0.25
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Z = np.zeros(X.shape[0])
Y[0] = 2

f = -y+(t*sp.sqrt(y)) # from question
g = (t-2+(sp.sqrt(2)*sp.exp(1)*sp.exp(-t/2)))**2

getEulerApproximation(f,X,Y,h)
getActualValues(g,X)

print('(c)')
print('Approx Sol: {}'.format(Y))
print('Exact Sol: {}'.format(Z))
for i in range(X.shape[0]):
    print('Error for y({}) = {}'.format(X[i],abs(Y[i]-Z[i])))



# Case (D):
# t belongs to [1,2] and y(1)=2, with h = 0.25
a, b, h = 1, 2, 0.25
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Z = np.zeros(X.shape[0])
Y[0] = 2

f = (sp.sin(2*t)-(2*t*y))/(t*t) # from question
g = (4+sp.cos(2)-sp.cos(2*t))/(2*(t**2))

getEulerApproximation(f,X,Y,h)
getActualValues(g,X)

print('(d)')
print('Approx Sol: {}'.format(Y))
print('Exact Sol: {}'.format(Z))
for i in range(X.shape[0]):
    print('Error for y({}) = {}'.format(X[i],abs(Y[i]-Z[i])))
