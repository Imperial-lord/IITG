# Question 02, Lab 07
# AB Satyaprakash - 180123062

# imports
from math import sqrt, log, exp
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# functions


def calEurCallPutPrices(T, K, S, r, σ, t):
    if(T == t):
        putp = max(K-S, 0)
        callp = max(S-K, 0)
        return [callp, putp]

    d1 = (log(S/K)+(r+(σ**2/2))*(T-t))/(σ*sqrt(T-t))
    d2 = d1-σ*sqrt(T-t)

    putp = K*exp(-r*(T-t))*norm.cdf(-d2) - S*norm.cdf(-d1)
    callp = S*norm.cdf(d1)-K*norm.cdf(d2)*exp(-r*(T-t))
    return [callp, putp]


# program body
# Given data
T, K, r, sig = 1, 1, 0.05, 0.6
t = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
S = np.arange(0.05, 3.05, 0.05)

# Fill 2-D arrays will zeros for storing prices
callPrices = np.zeros(shape=(t.shape[0], S.shape[0]))
putPrices = np.zeros(shape=(t.shape[0], S.shape[0]))

for i in range(t.shape[0]):
    for j in range(S.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T, K, S[j], r, sig, t[i])

for i in range(t.shape[0]):
    plt.plot(S, callPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Stock Prices')
plt.ylabel('Option Prices')
plt.title('Plot of C(t,s) vs s')
plt.legend()
plt.show()

for i in range(t.shape[0]):
    plt.plot(S, putPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Stock Prices')
plt.ylabel('Option Prices')
plt.title('Plot of P(t,s) vs s')
plt.legend()
plt.show()


callPricesT = np.matrix.transpose(callPrices)
putPricesT = np.matrix.transpose(putPrices)

tx, Sy = np.meshgrid(t, S)

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.scatter3D(tx, Sy, callPricesT, c='g')
ax.set_title('Scatter Plot of C(t,x) vs t and x')
ax.set_xlabel('Stock Prices')
ax.set_ylabel('Time')
ax.set_zlabel('Price of European Call Option')
plt.show()

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.scatter3D(tx, Sy, putPricesT, c='r')
ax.set_title('Scatter Plot of P(t,x) vs t and x')
ax.set_xlabel('Stock Prices')
ax.set_ylabel('Time')
ax.set_zlabel('Price of European Put Option')
plt.show()
