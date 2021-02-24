# Lab 05 Part (1)
# AB Satyaprakash - 180123062

# imports
from math import sqrt
from scipy.optimize import minimize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# functions


def calReturn(w):
    return np.dot(w, mu)


def calRisk(w):
    return sqrt(np.matmul(np.matmul(w, cov), np.transpose(w)))


def calEfficientFrontier(M):
    R, W, w = [], [], []
    x, y, r = 0, 0, 0
    for i in range(len(M)):
        cons = (
            {'type': 'eq', 'fun': lambda w: np.sum(w)-1},
            {'type': 'eq', 'fun': lambda w: calReturn(w)-M[i]}
        )
        res = minimize(calRisk, np.array(
            [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]), method='SLSQP', constraints=cons)
        R.append(res.fun)
        W.append(res.x)
        if (abs((M[i]-rf)/R[i]) > r):
            r = abs((M[i]-rf)/R[i])
            x = R[i]
            y = M[i]
            w = W[i]
    return W, R


# body of the program
# First read the indices of BSE and NSE monthly data obtained over a period of 5 years
bse_indices = pd.read_csv('./BSE/bsedata1.csv')
# since the 4th column is of use to us
bse_indices = bse_indices.iloc[:, 4].to_numpy()

nse_indices = pd.read_csv('./NSE/nsedata1.csv')
# since the 4th column is of use to us
nse_indices = nse_indices.iloc[:, 4].to_numpy()


# Returns are obtained as 12 times ((S[i]-S[i-1])/S[i-1])
bse_ret = []
for i in range(1, len(bse_indices)):
    bse_ret.append(12*(bse_indices[i]-bse_indices[i-1])/bse_indices[i-1])

bse_market_ret = np.mean(bse_ret)
bse_market_std = np.sqrt(np.var(bse_ret))

nse_ret = []
for i in range(1, len(nse_indices)):
    nse_ret.append(12*(nse_indices[i]-nse_indices[i-1])/nse_indices[i-1])

nse_market_ret = np.mean(nse_ret)
nse_market_std = np.sqrt(np.var(nse_ret))

print('Using BSE as index, the market portfolio obtained = ({}, {})'.format(
    bse_market_ret, bse_market_std))
print('Using NSE as index, the market portfolio obtained = ({}, {})'.format(
    nse_market_ret, nse_market_std))

# Read all the 40 differet stock prices obtained monthly over a period of 5 years.
# The cases are not in and in NIFTY and similarly in SENSEX
nse_stocks = pd.read_csv('./NSE/in_nifty.csv')
nse_stocks = nse_stocks.fillna(0)

non_nse_stocks = pd.read_csv('./NSE/not_in_nifty.csv')
non_nse_stocks = non_nse_stocks.fillna(0)

bse_stocks = pd.read_csv('./BSE/in_sensex.csv')
bse_stocks = bse_stocks.fillna(0)

non_bse_stocks = pd.read_csv('./BSE/not_in_sensex.csv')
non_bse_stocks = non_bse_stocks.fillna(0)


# Question 1.
# Efficient Frontier for BSE Stocks
asset_prices = bse_stocks.iloc[:, 1:].to_numpy()
ret = []
for i in range(len(asset_prices[0])):
    temp = []
    for j in range(1, len(asset_prices)):
        if asset_prices[j][i] == 0:
            asset_prices[j][i] = asset_prices[j-1][i]
        temp.append(
            12*(asset_prices[j][i]-asset_prices[j-1][i])/asset_prices[j-1][i])
    ret.append(temp)
mean_ret = []
for r in ret:
    mean_ret.append(np.mean(r))
cov = np.cov(ret)
mu = mean_ret
M = np.linspace(0, 1, 1000)
rf = 0.05
W, R = calEfficientFrontier(M)

plt.plot(R, M, color='red', label='Efficient Frontier')
plt.title('Efficient Frontier of BSE stocks')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.legend()
plt.show()

# Efficient Frontier for Non-BSE Stocks
asset_prices = non_bse_stocks.iloc[:, 1:].to_numpy()
ret = []
for i in range(len(asset_prices[0])):
    temp = []
    for j in range(1, len(asset_prices)):
        if asset_prices[j][i] == 0:
            asset_prices[j][i] = asset_prices[j-1][i]
        temp.append(
            12*(asset_prices[j][i]-asset_prices[j-1][i])/asset_prices[j-1][i])
    ret.append(temp)
mean_ret = []
for r in ret:
    mean_ret.append(np.mean(r))
cov = np.cov(ret)
mu = mean_ret
M = np.linspace(0, 1, 1000)
rf = 0.05
W, R = calEfficientFrontier(M)

plt.plot(R, M, color='red', label='Efficient Frontier')
plt.title('Efficient Frontier of Non BSE stocks')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.legend()
plt.show()


# Efficient Frontier for NSE Stocks
asset_prices = nse_stocks.iloc[:, 1:].to_numpy()
ret = []
for i in range(len(asset_prices[0])):
    temp = []
    for j in range(1, len(asset_prices)):
        if asset_prices[j][i] == 0:
            asset_prices[j][i] = asset_prices[j-1][i]
        temp.append(
            12*(asset_prices[j][i]-asset_prices[j-1][i])/asset_prices[j-1][i])
    ret.append(temp)
mean_ret = []
for r in ret:
    mean_ret.append(np.mean(r))
cov = np.cov(ret)
mu = mean_ret
M = np.linspace(0, 1, 1000)
rf = 0.05
W, R = calEfficientFrontier(M)

plt.plot(R, M, color='red', label='Efficient Frontier')
plt.title('Efficient Frontier of NSE stocks')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.legend()
plt.show()


# Efficient Frontier for Non NSE Stocks
asset_prices = non_nse_stocks.iloc[:, 1:].to_numpy()
ret = []
for i in range(len(asset_prices[0])):
    temp = []
    for j in range(1, len(asset_prices)):
        if asset_prices[j][i] == 0:
            asset_prices[j][i] = asset_prices[j-1][i]
        temp.append(
            12*(asset_prices[j][i]-asset_prices[j-1][i])/asset_prices[j-1][i])
    ret.append(temp)
mean_ret = []
for r in ret:
    mean_ret.append(np.mean(r))
cov = np.cov(ret)
mu = mean_ret
M = np.linspace(0, 1, 1000)
rf = 0.05
W, R = calEfficientFrontier(M)

plt.plot(R, M, color='red', label='Efficient Frontier')
plt.title('Efficient Frontier of Non NSE stocks')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.legend()
plt.show()
