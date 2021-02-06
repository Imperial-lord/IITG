# Question 1 Lab Assignment 03
# @AB Satyaprakash, 180123062

# imports
from math import exp, sqrt
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# functions ---------------------------------------------------------------------------


def isithBitSet(k, i):
    if k & (1 << (i - 1)):
        return True
    else:
        return False


def getLoopbackOptionPrice(S0, T, r, sig, M, p, u, d, dt):
    # return initial price of the option for M
    loopbackOptionPrice = 0

    # Notice that this has a time-complexity of O(2^M)!!
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
        Smax = np.max(price)
        payoff = Smax-price[-1]
        loopbackOptionPrice += (p**cnt)*((1-p)**(M-cnt))*payoff

    loopbackOptionPrice /= exp(r*T)
    return loopbackOptionPrice


def getIntermediateOptionPrice(S0, M, u, d):
    optionPrices = [[[S0, S0]]]
    for i in range(M):
        val = []
        for j in range(len(optionPrices[i])):
            S = optionPrices[i][j][0]*u
            Smax = max(optionPrices[i][j][1], S)
            val.append([S, Smax])

            S = optionPrices[i][j][0] * d
            Smax = max(optionPrices[i][j][1], S)
            val.append([S, Smax])
        optionPrices.append(val)
    return optionPrices


# -------------------------------------------------------------------------------------
# Given Initial Values
S0, T, r, sig = 100, 1, 0.08, 0.2

# (a) Get initial option prices
# M takes values [5, 10, 25, 50] -- but we won't take 25 and 50 due to the complexity!
Mlist = [5, 10]

for M in Mlist:
    dt = T/M

    u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p = (exp(r*dt)-d)/(u-d)

    loopbackOptionPrice = getLoopbackOptionPrice(S0, T, r, sig, M, p, u, d, dt)
    print('The initial loopback option price for M = {} is {}'.format(M, loopbackOptionPrice))

print('Due to complexity constraints, the initial value of the loopback option price cannot be calculated using the basic binomial algorithm for the case M = 25 and 50')
print('We will handle them in question 2')

# (b) Compare the initial option prices for the different values of M in part (a)
# We will plot a graph of initial option prices vs M for M values upto 15.
Mlist = np.arange(1, 16, 1)
loopbackOptionPriceList = np.zeros(Mlist.shape[0])

for i in range(Mlist.shape[0]):
    M = Mlist[i]
    dt = T/M

    u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p = (exp(r*dt)-d)/(u-d)

    loopbackOptionPriceList[i] = getLoopbackOptionPrice(S0, T, r, sig, M, p, u, d, dt)

plt.plot(Mlist, loopbackOptionPriceList)
plt.title('Plot of initial loopback option prices vs M - for M values upto 15')
plt.xlabel('Value of M')
plt.ylabel('Initial Price of Loopback Option Price')
plt.show()


# (c) For the value of M = 5, we'll tabulate option value at all intermediate points.
intermediateTimeSteps = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
intermediateOptionPrices = []

M = 5  # we are taking the case of M = 5
dt = T/M

u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
p = (exp(r*dt)-d)/(u-d)
optionPrices = getIntermediateOptionPrice(S0, M, u, d)
payoffs = []

for price in optionPrices[-1]:
    payoffs.append(price[1]-price[0])

for timeStep in intermediateTimeSteps:
    intermediateOptionPrices.append(payoffs)
    val = []
    for i in range((int)(len(payoffs)/2)):
        val.append((p*payoffs[2*i]+(1-p)*payoffs[2*i+1])*exp(-r*dt))
    payoffs = val

# reverse the list to be in accordance with intermediateTimeSteps list
intermediateOptionPrices.reverse()

# print everything as a table using pandas DataFrame
tableRows = []

for i in range(32):
    row = []
    for j in range(6):
        if(i < len(intermediateOptionPrices[j])):
            row.append((str)(round(intermediateOptionPrices[j][i], 4)))
        else:
            row.append(" ")
    tableRows.append(row)

df = pd.DataFrame(tableRows, columns=intermediateTimeSteps)
print('\n\nTable with Option Prices at all intermediate time points for M=5')
display(df)


# Test computation time for M = 15: ------------------------------------------------
dt = T/M

u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
p = (exp(r*dt)-d)/(u-d)

start = time.time()
timeTempPrice = getLoopbackOptionPrice(S0, T, r, sig, 15, p, u, d, dt)
end = time.time()

print('Computational time for M = 15 is {}s'.format(end-start))

# Question 1 ends ----------------------------------------------------------------------
