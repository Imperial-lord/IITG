# Question 2 Lab Assignment 02
# @AB Satyaprakash, 180123062

# imports
from math import exp, sqrt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# functions ---------------------------------------------------------------------------


def isithBitSet(k, i):
    if k & (1 << (i - 1)):
        return True
    else:
        return False


def getOptionPrice(S0, K, T, r, sig, M, p, u, d, dt):
    # We are using Asian Option as the path dependent derivative
    callOptionPrice, putOptionPrice = 0, 0

    for k in range(0, 2**M):
        price = [S0]
        cnt = 0
        for i in range(1, M+1):
            val = 0
            if isithBitSet(k, i):
                cnt += 1
                val = price[-1]*u
            else:
                val = price[-1]*d
            price.append(val)
        Savg = np.mean(price)
        callPayoff = max(Savg-K, 0)
        putPayoff = max(K-Savg, 0)
        callOptionPrice += (p**cnt)*((1-p)**(M-cnt))*callPayoff
        putOptionPrice += (p**cnt)*((1-p)**(M-cnt))*putPayoff

    callOptionPrice /= exp(r*T)
    putOptionPrice /= exp(r*T)
    return callOptionPrice, putOptionPrice

# --------------------------------------------------------------------------------------


# Find the Initial prices of Asian Put and Call Options
# Given Initial Values
S0, K, T, M, r, sig = 100, 100, 1, 10, 0.08, 0.2  # We'll take M=10 because 2^100 is really large!!

dt = T/M

u1 = exp(sig*sqrt(dt))
d1 = exp(-sig*sqrt(dt))
p1 = (exp(r*dt)-d1)/(u1-d1)

u2 = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
d2 = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
p2 = (exp(r*dt)-d2)/(u2-d2)

callp1, putp1 = getOptionPrice(S0, K, T, r, sig, M, p1, u1, d1, dt)
callp2, putp2 = getOptionPrice(S0, K, T, r, sig, M, p2, u2, d2, dt)

print('The Asian Call price for set 1 is: {}'.format(callp1))
print('The Asian Put price for set 1 is: {}'.format(putp1))
print('The Asian Call price for set 2 is: {}'.format(callp2))
print('The Asian Put price for set 2 is: {}'.format(putp2))

# -------------------------------------------------------------------------------------------

# Draw 2-D Plots
# (a) S0 from 50 - 150 in steps of 5
S0 = np.arange(50, 155, 5)
callp1, putp1, callp2, putp2 = np.zeros(S0.shape[0]), np.zeros(
    S0.shape[0]), np.zeros(S0.shape[0]), np.zeros(S0.shape[0])

for i in range(S0.shape[0]):
    K, T, M, r, sig = 100, 1, 10, 0.08, 0.2
    dt = T/M

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0[i], K, T, r, sig, M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0[i], K, T, r, sig, M, p2, u2, d2, dt)

plt.plot(S0, callp1, color='red')
plt.title('Plot of Asian Call option at t=0 vs S(0) (50-150) for Set 1 ')
plt.xlabel('Stock Price at t = 0')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(S0, putp1, color='green')
plt.title('Plot of Asian Put option at t=0 vs S(0) (50-150) for Set 1 ')
plt.xlabel('Stock Price at t = 0')
plt.ylabel('Price of Asian Put option')
plt.show()

plt.plot(S0, callp2, color='red')
plt.title('Plot of Asian Call option at t=0 vs S(0) (50-150) for Set 2 ')
plt.xlabel('Stock Price at t = 0')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(S0, putp2, color='green')
plt.title('Plot of Asian Put option at t=0 vs S(0) (50-150) for Set 2 ')
plt.xlabel('Stock Price at t = 0')
plt.ylabel('Price of Asian Put option')
plt.show()

# (b) K from 50 - 150 in steps of 5
K = np.arange(50, 155, 5)
callp1, putp1, callp2, putp2 = np.zeros(K.shape[0]), np.zeros(
    K.shape[0]), np.zeros(K.shape[0]), np.zeros(K.shape[0])

for i in range(K.shape[0]):
    S0, T, M, r, sig = 100, 1, 10, 0.08, 0.2
    dt = T/M

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K[i], T, r, sig, M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K[i], T, r, sig, M, p2, u2, d2, dt)

plt.plot(K, callp1, color='red')
plt.title('Plot of Asian Call option at t=0 vs K (50-150) for Set 1 ')
plt.xlabel('Strike Price (K)')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(K, putp1, color='green')
plt.title('Plot of Asian Put option at t=0 vs K (50-150) for Set 1 ')
plt.xlabel('Strike Price (K)')
plt.ylabel('Price of Asian Put option')
plt.show()

plt.plot(K, callp2, color='red')
plt.title('Plot of Asian Call option at t=0 vs K (50-150) for Set 2 ')
plt.xlabel('Strike Price (K)')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(K, putp2, color='green')
plt.title('Plot of Asian Put option at t=0 vs K (50-150) for Set 2 ')
plt.xlabel('Strike Price (K)')
plt.ylabel('Price of Asian Put option')
plt.show()


# (c) r from 0 to 0.2 in steps of 0.01
r = np.arange(0, 0.21, 0.01)
callp1, putp1, callp2, putp2 = np.zeros(r.shape[0]), np.zeros(
    r.shape[0]), np.zeros(r.shape[0]), np.zeros(r.shape[0])

for i in range(r.shape[0]):
    S0, K, T, M, sig = 100, 100, 1, 10, 0.2
    dt = T/M

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r[i]*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    p2 = (exp(r[i]*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K, T, r[i], sig, M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K, T, r[i], sig, M, p2, u2, d2, dt)

plt.plot(r, callp1, color='red')
plt.title('Plot of Asian Call option at t=0 vs r (0-0.2) for Set 1 ')
plt.xlabel('Interest Rate (r)')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(r, putp1, color='green')
plt.title('Plot of Asian Put option at t=0 vs r (0-0.2) for Set 1 ')
plt.xlabel('Interest Rate (r)')
plt.ylabel('Price of Asian Put option')
plt.show()

plt.plot(r, callp2, color='red')
plt.title('Plot of Asian Call option at t=0 vs r (0-0.2) for Set 2 ')
plt.xlabel('Interest Rate (r)')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(r, putp2, color='green')
plt.title('Plot of Asian Put option at t=0 vs r (0-0.2) for Set 2 ')
plt.xlabel('Interest Rate (r)')
plt.ylabel('Price of Asian Put option')
plt.show()


# (d) sig from 0.1 to 0.3 in steps of 0.01
sig = np.arange(0.1, 0.31, 0.01)  # avoid getting sigma = 0 exactly as it'd lead to div by 0
callp1, putp1, callp2, putp2 = np.zeros(sig.shape[0]), np.zeros(
    sig.shape[0]), np.zeros(sig.shape[0]), np.zeros(sig.shape[0])

for i in range(sig.shape[0]):
    S0, K, T, M, r = 100, 100, 1, 10, 0.08
    dt = T/M

    u1 = exp(sig[i]*sqrt(dt))
    d1 = exp(-sig[i]*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    d2 = exp(-sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K, T, r, sig[i], M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K, T, r, sig[i], M, p2, u2, d2, dt)

plt.plot(sig, callp1, color='red')
plt.title('Plot of Asian Call option at t=0 vs sig (0.1-0.3) for Set 1 ')
plt.xlabel('Value of Sigma')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(sig, putp1, color='green')
plt.title('Plot of Asian Put option at t=0 vs sig (0.1-0.3) for Set 1 ')
plt.xlabel('Value of Sigma')
plt.ylabel('Price of Asian Put option')
plt.show()

plt.plot(sig, callp2, color='red')
plt.title('Plot of Asian Call option at t=0 vs sig (0.1-0.3) for Set 2 ')
plt.xlabel('Value of Sigma')
plt.ylabel('Price of Asian Call option')
plt.show()

plt.plot(sig, putp2, color='green')
plt.title('Plot of Asian Put option at t=0 vs sig (0.1-0.3) for Set 2 ')
plt.xlabel('Value of Sigma')
plt.ylabel('Price of Asian Put option')
plt.show()


# (e) M from 1-10 in steps of 1, and K for 3 values 95, 100 and 105
K = np.arange(95, 110, 5)
M = np.arange(1, 11, 1)

for j in range(K.shape[0]):
    callp1, putp1, callp2, putp2 = np.zeros(M.shape[0]), np.zeros(
        M.shape[0]), np.zeros(M.shape[0]), np.zeros(M.shape[0])

    for i in range(M.shape[0]):
        S0, T, r, sig = 100, 1, 0.08, 0.2
        dt = T/M[i]

        u1 = exp(sig*sqrt(dt))
        d1 = exp(-sig*sqrt(dt))
        p1 = (exp(r*dt)-d1)/(u1-d1)

        u2 = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
        d2 = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
        p2 = (exp(r*dt)-d2)/(u2-d2)

        callp1[i], putp1[i] = getOptionPrice(S0, K[j], T, r, sig, M[i], p1, u1, d1, dt)
        callp2[i], putp2[i] = getOptionPrice(S0, K[j], T, r, sig, M[i], p2, u2, d2, dt)

    plt.plot(M, callp1, color='red')
    plt.title('Plot of Asian Call option at t=0 vs M (1-10) for Set 1 and K = {} '.format(K[j]))
    plt.xlabel('No. of Steps (M)')
    plt.ylabel('Price of Asian Call option')
    plt.show()

    plt.plot(M, putp1, color='green')
    plt.title('Plot of Asian Put option at t=0 vs M (1-10) for Set 1 and K = {} '.format(K[j]))
    plt.xlabel('No. of Steps (M)')
    plt.ylabel('Price of Asian Put option')
    plt.show()

    plt.plot(M, callp2, color='red')
    plt.title('Plot of Asian Call option at t=0 vs M (1-10) for Set 2 and K = {} '.format(K[j]))
    plt.xlabel('No. of Steps (M)')
    plt.ylabel('Price of Asian Call option')
    plt.show()

    plt.plot(M, putp2, color='green')
    plt.title('Plot of Asian Put option at t=0 vs M (1-10) for Set 2 and K = {} '.format(K[j]))
    plt.xlabel('No. of Steps (M)')
    plt.ylabel('Price of Asian Put option')
    plt.show()

# -------------------------------------------------------------------------------------------

# Draw 3-D Plots
# We'll have C(5,2) = 10 cases taking 2 parameters at a time and then plotting 4 graphs for each case.

# (a) S0 and K taken together
# Generate 600 uniform discrete random numbers in range 1 - 300
S0 = np.random.randint(1, 300+1, 600)
K = np.random.randint(1, 300+1, 600)

callp1, putp1, callp2, putp2 = np.zeros(S0.shape[0]), np.zeros(
    S0.shape[0]), np.zeros(S0.shape[0]), np.zeros(S0.shape[0])

for i in range(S0.shape[0]):
    T, M, r, sig = 1, 10, 0.08, 0.2
    dt = T/M

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0[i], K[i], T, r, sig, M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0[i], K[i], T, r, sig, M, p2, u2, d2, dt)

plt.close()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, K, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and K (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Strike Price (K)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, K, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and K (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Strike Price (K)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, K, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and K (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Strike Price (K)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, K, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and K (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Strike Price (K)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (b) S0 and r taken together
# Generate 600 uniform discrete random numbers in range 1 - 300 and in range 0 to 0.2

S0 = np.random.randint(1, 300+1, 600)
r = np.random.uniform(0, 0.2, 600)

callp1, putp1, callp2, putp2 = np.zeros(S0.shape[0]), np.zeros(
    S0.shape[0]), np.zeros(S0.shape[0]), np.zeros(S0.shape[0])

for i in range(S0.shape[0]):
    K, T, M, sig = 100, 1, 10, 0.2
    dt = T/M

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r[i]*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    p2 = (exp(r[i]*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0[i], K, T, r[i], sig, M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0[i], K, T, r[i], sig, M, p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, r, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and r (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, r, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and r (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, r, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and r (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, r, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and r (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (c) S0 and sigma taken together
# Generate 600 uniform discrete random numbers in range 1 - 300 and in range 0 to 0.2

S0 = np.random.randint(1, 300+1, 600)
sig = np.random.uniform(0.1, 0.3, 600)

callp1, putp1, callp2, putp2 = np.zeros(S0.shape[0]), np.zeros(
    S0.shape[0]), np.zeros(S0.shape[0]), np.zeros(S0.shape[0])

for i in range(S0.shape[0]):
    K, T, M, r = 100, 1, 10, 0.08
    dt = T/M

    u1 = exp(sig[i]*sqrt(dt))
    d1 = exp(-sig[i]*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    d2 = exp(-sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0[i], K, T, r, sig[i], M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0[i], K, T, r, sig[i], M, p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, sig, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and sig (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, sig, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and sig (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, sig, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and sig (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, sig, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and sig (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (d) S0 and M taken together
# Generate 600 uniform discrete random numbers in range 1 - 300
S0 = np.random.randint(1, 300+1, 600)
M = np.random.randint(1, 10+1, 600)

callp1, putp1, callp2, putp2 = np.zeros(S0.shape[0]), np.zeros(
    S0.shape[0]), np.zeros(S0.shape[0]), np.zeros(S0.shape[0])

for i in range(S0.shape[0]):
    T, K, r, sig = 1, 100, 0.08, 0.2
    dt = T/M[i]

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0[i], K, T, r, sig, M[i], p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0[i], K, T, r, sig, M[i], p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, M, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and M (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, M, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and M (Set 1)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, M, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and M (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(S0, M, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with S(0) and M (Set 2)')
ax.set_xlabel('Stock Price at t=0 - S(0)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (e) K and r taken together
# Generate 600 uniform discrete random numbers in range 1 - 300 and in range 0 to 0.2

K = np.random.randint(1, 300+1, 600)
r = np.random.uniform(0, 0.2, 600)

callp1, putp1, callp2, putp2 = np.zeros(K.shape[0]), np.zeros(
    K.shape[0]), np.zeros(K.shape[0]), np.zeros(K.shape[0])

for i in range(K.shape[0]):
    S0, T, M, sig = 100, 1, 10, 0.2
    dt = T/M

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r[i]*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    p2 = (exp(r[i]*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K[i], T, r[i], sig, M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K[i], T, r[i], sig, M, p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, r, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with K and r (Set 1)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, r, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with K and r (Set 1)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, r, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with K and r (Set 2)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, r, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with K and r (Set 2)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (f) K and sig taken together
# Generate 600 uniform discrete random numbers in range 1 - 300 and in range 0 to 0.3

K = np.random.randint(1, 300+1, 600)
sig = np.random.uniform(0.1, 0.3, 600)

callp1, putp1, callp2, putp2 = np.zeros(K.shape[0]), np.zeros(
    K.shape[0]), np.zeros(K.shape[0]), np.zeros(K.shape[0])

for i in range(K.shape[0]):
    S0, T, M, r = 100, 1, 10, 0.08
    dt = T/M

    u1 = exp(sig[i]*sqrt(dt))
    d1 = exp(-sig[i]*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    d2 = exp(-sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K[i], T, r, sig[i], M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K[i], T, r, sig[i], M, p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, sig, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with K and sig (Set 1)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, sig, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with K and sig (Set 1)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, sig, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with K and sig (Set 2)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, sig, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with K and sig (Set 2)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (g) K and M taken together
# Generate 600 uniform discrete random numbers in range 1 - 300
K = np.random.randint(1, 300+1, 600)
M = np.random.randint(1, 10+1, 600)

callp1, putp1, callp2, putp2 = np.zeros(K.shape[0]), np.zeros(
    K.shape[0]), np.zeros(K.shape[0]), np.zeros(K.shape[0])

for i in range(K.shape[0]):
    T, S0, r, sig = 1, 100, 0.08, 0.2
    dt = T/M[i]

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K[i], T, r, sig, M[i], p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K[i], T, r, sig, M[i], p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, M, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with K and M (Set 1)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, M, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with K and M (Set 1)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, M, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with K and M (Set 2)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(K, M, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with K and M (Set 2)')
ax.set_xlabel('Strike Price (K)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (h) r and sig taken together
# Generate 600 uniform discrete random numbers in range 0 to 0.2 and in range 0 to 0.3

r = np.random.uniform(0, 0.2, 600)
sig = np.random.uniform(0.1, 0.3, 600)

callp1, putp1, callp2, putp2 = np.zeros(r.shape[0]), np.zeros(
    r.shape[0]), np.zeros(r.shape[0]), np.zeros(r.shape[0])

for i in range(r.shape[0]):
    S0, K, T, M = 100, 100, 1, 10
    dt = T/M

    u1 = exp(sig[i]*sqrt(dt))
    d1 = exp(-sig[i]*sqrt(dt))
    p1 = (exp(r[i]*dt)-d1)/(u1-d1)

    u2 = exp(sig[i]*sqrt(dt)+(r[i]-sig[i]*sig[i]/2)*dt)
    d2 = exp(-sig[i]*sqrt(dt)+(r[i]-sig[i]*sig[i]/2)*dt)
    p2 = (exp(r[i]*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K, T, r[i], sig[i], M, p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K, T, r[i], sig[i], M, p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, sig, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with r and sig (Set 1)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, sig, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with r and sig (Set 1)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, sig, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with r and sig (Set 2)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, sig, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with r and sig (Set 2)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('Value of Sigma')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

# (i) r and M taken together
# Generate 600 uniform discrete random numbers in range 0 to 0.2 and in range 1 to 300

r = np.random.uniform(0, 0.2, 600)
M = np.random.randint(1, 11, 600)

callp1, putp1, callp2, putp2 = np.zeros(r.shape[0]), np.zeros(
    r.shape[0]), np.zeros(r.shape[0]), np.zeros(r.shape[0])

for i in range(r.shape[0]):
    S0, K, T, sig = 100, 100, 1, 0.2
    dt = T/M[i]

    u1 = exp(sig*sqrt(dt))
    d1 = exp(-sig*sqrt(dt))
    p1 = (exp(r[i]*dt)-d1)/(u1-d1)

    u2 = exp(sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    d2 = exp(-sig*sqrt(dt)+(r[i]-sig*sig/2)*dt)
    p2 = (exp(r[i]*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K, T, r[i], sig, M[i], p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K, T, r[i], sig, M[i], p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, M, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with r and M (Set 1)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, M, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with r and M (Set 1)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, M, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with r and M (Set 2)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(r, M, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with r and M (Set 2)')
ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# (j) sig and M taken together
# Generate 600 uniform discrete random numbers in range 0 to 0.3 and in range 1 to 300

sig = np.random.uniform(0.1, 0.3, 600)
M = np.random.randint(1, 11, 600)

callp1, putp1, callp2, putp2 = np.zeros(sig.shape[0]), np.zeros(
    sig.shape[0]), np.zeros(sig.shape[0]), np.zeros(sig.shape[0])

for i in range(sig.shape[0]):
    S0, K, T, r = 100, 100, 1, 0.08
    dt = T/M[i]

    u1 = exp(sig[i]*sqrt(dt))
    d1 = exp(-sig[i]*sqrt(dt))
    p1 = (exp(r*dt)-d1)/(u1-d1)

    u2 = exp(sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    d2 = exp(-sig[i]*sqrt(dt)+(r-sig[i]*sig[i]/2)*dt)
    p2 = (exp(r*dt)-d2)/(u2-d2)

    callp1[i], putp1[i] = getOptionPrice(S0, K, T, r, sig[i], M[i], p1, u1, d1, dt)
    callp2[i], putp2[i] = getOptionPrice(S0, K, T, r, sig[i], M[i], p2, u2, d2, dt)


fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(sig, M, callp1, c='r')
ax.set_title('Scatter Plot of Initial Option Price with sig and M (Set 1)')
ax.set_xlabel('Value of Sigma')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(sig, M, putp1, c='g')
ax.set_title('Scatter Plot of Initial Option Price with sig and M (Set 1)')
ax.set_xlabel('Value of Sigma')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(sig, M, callp2, c='r')
ax.set_title('Scatter Plot of Initial Option Price with sig and M (Set 2)')
ax.set_xlabel('Value of Sigma')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Call Option')
ax.invert_yaxis()
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
ax.scatter(sig, M, putp2, c='g')
ax.set_title('Scatter Plot of Initial Option Price with sig and M (Set 2)')
ax.set_xlabel('Value of Sigma')
ax.set_ylabel('No. of Steps (M)')
ax.set_zlabel('Price of Asian Put Option')
ax.invert_yaxis()
plt.show()


# -------------------------------------------------------------------------------------------
# Question 2 complete
