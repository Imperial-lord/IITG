# Question 1, Lab 6
# AB Satyaprakash, 180123062

# imports 
from sympy.abc import t,y
import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

# functions 
def getEulerApproximation(f,X,Y,h):
    for i in range(1,Y.shape[0]):
        Y[i]=Y[i-1] + (f.subs({t:X[i-1], y:Y[i-1]})*h)

def getActualValues(g,X):
    for i in range(X.shape[0]):
        Z[i]=g.subs(t,X[i])

def phi(n, k, x, z):

    prod = 1
    for i in range(n):
        if i != k:
            prod = prod * (z - x[i])
    
    return prod 

def lagrangeInterpolation(z, x, fx):

    n = len(x)
    l = np.empty(n)
    for i in range(n):
        l[i] = phi(n,i,x,z)/phi(n,i,x,x[i])

    ans = np.dot(l, fx)

    return ans

# program body
# t belongs to [1,2] and y(1)=-1, with h = 0.05
a, b, h = 1, 2, 0.05
X = np.arange(a,b+h/2,h)
Y = np.zeros(X.shape[0])
Z = np.zeros(X.shape[0])
Y[0] = -1

f = 1/(t**2) - y/t - (y**2) # from question
g = -1/t

getEulerApproximation(f,X,Y,h)
getActualValues(g,X)

print('(a)')
table={'Evaluate':[], 'Approx':[], 'Actual':[], 'Error':[]}

for i in range(X.shape[0]):
    table['Evaluate'].append('y({})'.format(round(X[i],2)))
    table['Approx'].append(Y[i])
    table['Actual'].append(Z[i])
    table['Error'].append(abs(Y[i]-Z[i]))

df = pd.DataFrame(table,columns=['Evaluate', 'Approx', 'Actual','Error'])
print(df)

print('\n(b)')
print('(I)')
x = 1.052
intepolatedVal = lagrangeInterpolation(x,X,Y)
print('Estimated value of y({}) from interpolation ={}'.format(x,intepolatedVal))
print('Actual value of y = {}'.format(g.subs(t,x)))
print('The error between them = {}'.format(abs(intepolatedVal-g.subs(t,x))))

print('(II)')
x = 1.555
intepolatedVal = lagrangeInterpolation(x,X,Y)
print('Estimated value of y({}) from interpolation ={}'.format(x,intepolatedVal))
print('Actual value of y = {}'.format(g.subs(t,x)))
print('The error between them = {}'.format(abs(intepolatedVal-g.subs(t,x))))

print('(III)')
x = 1.978
intepolatedVal = lagrangeInterpolation(x,X,Y)
print('Estimated value of y({}) from interpolation ={}'.format(x,intepolatedVal))
print('Actual value of y = {}'.format(g.subs(t,x)))
print('The error between them = {}'.format(abs(intepolatedVal-g.subs(t,x))))

# plotting the values in the table.
plt.plot(X,Y, label='Euler Approximation')
plt.plot(X,Z, label='Actual value')
plt.xlabel('Value of t')
plt.ylabel('Value of y')
plt.title('Comparision between Euler Approx and Actual values of y')
plt.legend()
plt.show()
