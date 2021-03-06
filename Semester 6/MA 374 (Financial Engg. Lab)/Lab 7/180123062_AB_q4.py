# Question 04, Lab 07
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
# We will consider Strike Price (K), sigma(σ), rate (r) and Final Time (T)
# 2D Plots
# Varying with Strike Price:

T, S, r, sig = 1, 1, 0.05, 0.6
t = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
K = np.arange(0.05, 1.55, 0.05)

callPrices = np.zeros(shape=(t.shape[0], K.shape[0]))
putPrices = np.zeros(shape=(t.shape[0], K.shape[0]))

for i in range(t.shape[0]):
    for j in range(K.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T, K[j], S, r, sig, t[i])

for i in range(t.shape[0]):
    plt.plot(K, callPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Strike Price')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Call Prices vs K')
plt.legend()
plt.show()

for i in range(t.shape[0]):
    plt.plot(K, putPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Strike Price')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Put Prices vs K')
plt.legend()
plt.show()


# Varying with Volatility (sigma):

T, S, r, K = 1, 1, 0.05, 1
t = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
sig = np.arange(0.05, 1.0, 0.05)

callPrices = np.zeros(shape=(t.shape[0], sig.shape[0]))
putPrices = np.zeros(shape=(t.shape[0], sig.shape[0]))

for i in range(t.shape[0]):
    for j in range(sig.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T, K, S, r, sig[j], t[i])

for i in range(t.shape[0]):
    plt.plot(sig, callPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Volatility')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Call Prices vs Sigma')
plt.legend()
plt.show()

for i in range(t.shape[0]):
    plt.plot(sig, putPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Volatility')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Put Prices vs Sigma')
plt.legend()
plt.show()


# Varying with Rate (r):

T, S, sig, K = 1, 1, 0.6, 1
t = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
r = np.arange(0.05, 1.0, 0.05)

callPrices = np.zeros(shape=(t.shape[0], r.shape[0]))
putPrices = np.zeros(shape=(t.shape[0], r.shape[0]))

for i in range(t.shape[0]):
    for j in range(r.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T, K, S, r[j], sig, t[i])

for i in range(t.shape[0]):
    plt.plot(r, callPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Rate')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Call Prices vs r')
plt.legend()
plt.show()

for i in range(t.shape[0]):
    plt.plot(r, putPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Rate')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Put Prices vs r')
plt.legend()
plt.show()


# Varying with Final Time (T):

r, S, sig, K = 0.05, 1, 0.6, 1
t = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
T = np.arange(1.05, 5, 0.05)

callPrices = np.zeros(shape=(t.shape[0], T.shape[0]))
putPrices = np.zeros(shape=(t.shape[0], T.shape[0]))

for i in range(t.shape[0]):
    for j in range(T.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T[j], K, S, r, sig, t[i])

for i in range(t.shape[0]):
    plt.plot(T, callPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Expiry Time')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Call Prices vs T')
plt.legend()
plt.show()

for i in range(t.shape[0]):
    plt.plot(T, putPrices[i], label='t = {}'.format(t[i]))
plt.xlabel('Expiry Time')
plt.ylabel('Option Prices')
plt.title('Sensitivity of Put Prices vs T')
plt.legend()
plt.show()


# 3D Plots -
# We will consider Strike Price (K), sigma(σ), rate (r) and Final Time (T) 2 at a time!
# Fix t =0.5

# K and sigma
T, S, r, t = 1, 1, 0.05, 0.5
K = np.arange(0.05, 1.5, 0.05)
sig = np.arange(0.05, 1.0, 0.05)

callPrices = np.zeros(shape=(K.shape[0], sig.shape[0]))
putPrices = np.zeros(shape=(K.shape[0], sig.shape[0]))

for i in range(K.shape[0]):
    for j in range(sig.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T, K[i], S, r, sig[j], t)

callPricesT = np.matrix.transpose(callPrices)
putPricesT = np.matrix.transpose(putPrices)


x, y = np.meshgrid(K, sig)

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, callPricesT, cmap='inferno')
ax.set_title('Surface Plot of Call Option Prices vs K and sigma')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Sigma')
ax.set_zlabel('Price of European Call Option')
plt.show()


fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, putPricesT, cmap='inferno')
ax.set_title('Surface Plot of Put Option Prices vs K and sigma')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Sigma')
ax.set_zlabel('Price of European Put Option')
plt.show()


# K and rate
T, S, sig, t = 1, 1, 0.6, 0.5
K = np.arange(0.05, 1.5, 0.05)
r = np.arange(0.05, 1.0, 0.05)

callPrices = np.zeros(shape=(K.shape[0], r.shape[0]))
putPrices = np.zeros(shape=(K.shape[0], r.shape[0]))

for i in range(K.shape[0]):
    for j in range(r.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T, K[i], S, r[j], sig, t)

callPricesT = np.matrix.transpose(callPrices)
putPricesT = np.matrix.transpose(putPrices)


x, y = np.meshgrid(K, r)

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, callPricesT, cmap='inferno')
ax.set_title('Surface Plot of Call Option Prices vs K and r')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Rate')
ax.set_zlabel('Price of European Call Option')
plt.show()


fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, putPricesT, cmap='inferno')
ax.set_title('Surface Plot of Put Option Prices vs K and r')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Rate')
ax.set_zlabel('Price of European Put Option')
plt.show()


# K and Expiry Time (T)
r, S, sig, t = 0.05, 1, 0.6, 0.5
K = np.arange(0.05, 1.5, 0.05)
T = np.arange(1.05, 5.0, 0.05)

callPrices = np.zeros(shape=(K.shape[0], T.shape[0]))
putPrices = np.zeros(shape=(K.shape[0], T.shape[0]))

for i in range(K.shape[0]):
    for j in range(T.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T[j], K[i], S, r, sig, t)

callPricesT = np.matrix.transpose(callPrices)
putPricesT = np.matrix.transpose(putPrices)


x, y = np.meshgrid(K, T)

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, callPricesT, cmap='inferno')
ax.set_title('Surface Plot of Call Option Prices vs K and T')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Expiry Time')
ax.set_zlabel('Price of European Call Option')
plt.show()


fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, putPricesT, cmap='inferno')
ax.set_title('Surface Plot of Put Option Prices vs K and T')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Expiry Time')
ax.set_zlabel('Price of European Put Option')
plt.show()

# Sigma and T
r, S, K, t = 0.05, 1, 1, 0.5
sig = np.arange(0.05, 1, 0.05)
T = np.arange(1.05, 5.0, 0.05)

callPrices = np.zeros(shape=(sig.shape[0], T.shape[0]))
putPrices = np.zeros(shape=(sig.shape[0], T.shape[0]))

for i in range(sig.shape[0]):
    for j in range(T.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T[j], K, S, r, sig[i], t)

callPricesT = np.matrix.transpose(callPrices)
putPricesT = np.matrix.transpose(putPrices)


x, y = np.meshgrid(sig, T)

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, callPricesT, cmap='inferno')
ax.set_title('Surface Plot of Call Option Prices vs sig and T')
ax.set_xlabel('Sigma')
ax.set_ylabel('Expiry Time')
ax.set_zlabel('Price of European Call Option')
plt.show()


fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, putPricesT, cmap='inferno')
ax.set_title('Surface Plot of Put Option Prices vs sig and T')
ax.set_xlabel('Sigma')
ax.set_ylabel('Expiry Time')
ax.set_zlabel('Price of European Put Option')
plt.show()

# Sigma and Rate
T, S, K, t = 1, 1, 1, 0.5
sig = np.arange(0.05, 1, 0.05)
r = np.arange(1.05, 1.5, 0.05)

callPrices = np.zeros(shape=(sig.shape[0], r.shape[0]))
putPrices = np.zeros(shape=(sig.shape[0], r.shape[0]))

for i in range(sig.shape[0]):
    for j in range(r.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T, K, S, r[j], sig[i], t)

callPricesT = np.matrix.transpose(callPrices)
putPricesT = np.matrix.transpose(putPrices)


x, y = np.meshgrid(sig, r)

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, callPricesT, cmap='inferno')
ax.set_title('Surface Plot of Call Option Prices vs sig and r')
ax.set_xlabel('Sigma')
ax.set_ylabel('Rate')
ax.set_zlabel('Price of European Call Option')
plt.show()

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, putPricesT, cmap='inferno')
ax.set_title('Surface Plot of Put Option Prices vs sig and r')
ax.set_xlabel('Sigma')
ax.set_ylabel('Rate')
ax.set_zlabel('Price of European Put Option')
plt.show()


# Time and Rate
sig, S, K, t = 0.6, 1, 1, 0.5
T = np.arange(1.05, 5, 0.05)
r = np.arange(1.05, 1.5, 0.05)

callPrices = np.zeros(shape=(T.shape[0], r.shape[0]))
putPrices = np.zeros(shape=(T.shape[0], r.shape[0]))

for i in range(T.shape[0]):
    for j in range(r.shape[0]):
        [callPrices[i][j], putPrices[i][j]] = calEurCallPutPrices(
            T[i], K, S, r[j], sig, t)

callPricesT = np.matrix.transpose(callPrices)
putPricesT = np.matrix.transpose(putPrices)


x, y = np.meshgrid(T, r)

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, callPricesT, cmap='inferno')
ax.set_title('Surface Plot of Call Option Prices vs sig and r')
ax.set_xlabel('Expiry Time')
ax.set_ylabel('Rate')
ax.set_zlabel('Price of European Call Option')
plt.show()

fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
ax.plot_surface(x, y, putPricesT, cmap='inferno')
ax.set_title('Surface Plot of Put Option Prices vs sig and r')
ax.set_xlabel('Expiry Time')
ax.set_ylabel('Rate')
ax.set_zlabel('Price of European Put Option')
plt.show()
