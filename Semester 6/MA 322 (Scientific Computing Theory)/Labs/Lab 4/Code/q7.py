# Question 07(b), Lab 04
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------
import random
import numpy as np
import matplotlib.pyplot as plt

# functions --------------------------------------------------------------------------


def f(x):
    return (x**3) + (0.01*random.random())


def compositeTrapezoidalRule(X):
    sum = 0
    a, b = X[0], X[-1]
    n = X.shape[0]
    h = (b-a)/(n-1)
    for i in range(n):
        x = X[i]
        if(i == 0 or i == n-1):
            sum += f(x)/2
        else:
            sum += f(x)
    return (h*sum)


# program body
errorArray = []
for i in range(30, 5000):
    h = (1-0)/i
    X = np.arange(0, 1+h/2, h)
    errorArray.append(abs(0.25-(compositeTrapezoidalRule(X))))

h = 1/5000
X = np.arange(0, 1+h/2, h)
print('Using inexact function evaluations')
print('Approximate value of integral for h=0.0002 is', compositeTrapezoidalRule(X))
print('Error in the process:', abs(0.25-compositeTrapezoidalRule(X)))

plt.title("Error vs n")
plt.xlabel("n")
plt.ylabel("error in estimation")
plt.plot(range(30, 5000), errorArray)
plt.xticks(range(30, 5000, 500))
plt.show()
