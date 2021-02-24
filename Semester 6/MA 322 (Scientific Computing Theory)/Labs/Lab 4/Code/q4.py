# Question 04, Lab 04
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------
from sympy.abc import t
from sympy import evalf, integrate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# functions --------------------------------------------------------------------------


def f(x):
    return 1/(x+2)


def compositeTrapezoidalRule(X):
    sum = 0
    a, b = X[0], X[-1]
    n = X.shape[0]
    h = (b-a)/(n-1)
    for i in range(X.shape[0]):
        x = X[i]
        if(i == 0 or i == n-1):
            sum += f(x)/2
        else:
            sum += f(x)
    return (h*sum)


def compositeSimpsonRule(X):
    sum = 0
    a, b = X[0], X[-1]
    n = X.shape[0]
    h = (b-a)/(n-1)
    for i in range(X.shape[0]):
        x = X[i]
        if(i == 0 or i == n-1):
            sum += f(x)
        else:
            if(i % 2 == 0):
                sum += 2*f(x)
            else:
                sum += 4*f(x)
    return (h*sum)/3


# program body
func = 1/(t+2)
a, b = -1, 1

# Using sympy to integrate and evaluate the actual values before plotting!
I = integrate(func, (t, a, b)).evalf()
print('Actual value of integral is', I)

maxN = 30
actualArray, trapezoidalArray, simpsonArray, N = np.zeros(
    maxN), np.zeros(maxN), np.zeros(maxN), np.zeros(maxN)

for i in range(maxN):
    N[i] = i+1
    X = np.arange(a, b+0.0001, (b-a)/N[i])
    actualArray[i] = I
    trapezoidalArray[i] = compositeTrapezoidalRule(X)
    if(i == 0):
        simpsonArray[i] = np.NaN
    else:
        simpsonArray[i] = compositeSimpsonRule(X)

plt.plot(N, actualArray, label='Actual')
plt.plot(N, trapezoidalArray, label='Trapezoidal')
plt.plot(N, simpsonArray, label='Simpson')
plt.title('Comparing results for varying n')
plt.xlabel('Value of n')
plt.ylabel('Evaluated value of integral by different methods')
plt.legend()
plt.show()

data = np.vstack((N, trapezoidalArray, simpsonArray)).T

df = pd.DataFrame(data,
                  columns=['N-value', 'Trapezoidal', 'Simpson']).round(6)
df.set_index('N-value', inplace=True)
print('\n', df, '\n')


# Plotting the various curves from [-1,1]
# The original curve is given as 1/x+2

# Trapezoidal rule forms a trapezoid joining the points (-1,f(-1)) and (1, f(1))
# y = -1/3 x + 2/3

# Simpson rule forms a parabola joining the points (-1, f(-1)), (0,f(0)) and (1,f(1))
# y = 1/6 x^2 − 1/3 x + 1/2

X = np.arange(-1, 1, 0.01)
actualArray, trapezoidalArray, simpsonArray = [], [], []
for x in X:
    actualArray.append(1/(x+2))
    trapezoidalArray.append((-1/3)*x + (2/3))
    simpsonArray.append((1/6)*(x**2) - (1/3)*x + 1/2)

plt.plot(X, actualArray, color='blue')
plt.plot(X, trapezoidalArray, color='orange')
plt.fill_between(X, actualArray, 0, color='blue', alpha=0.2, label='Actual')
plt.fill_between(X, trapezoidalArray, 0, color='orange',
                 alpha=0.3, label='Trapezoidal')
plt.title('Actual vs Trapezoidal')
plt.ylabel('Area under curve for different rules')
plt.xlabel('Value of x from [-1, 1]')
plt.legend()
plt.show()

plt.plot(X, actualArray, color='blue')
plt.plot(X, simpsonArray, color='orange')
plt.fill_between(X, actualArray, 0, color='blue', alpha=0.2, label='Actual')
plt.fill_between(X, simpsonArray, 0, color='orange',
                 alpha=0.3, label='Simpson')
plt.title('Actual vs Simpson')
plt.ylabel('Area under curve for different rules')
plt.xlabel('Value of x from [-1, 1]')
plt.legend()
plt.show()
