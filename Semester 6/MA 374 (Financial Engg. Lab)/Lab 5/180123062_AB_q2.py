# Lab 05 Part (2)
# AB Satyaprakash - 180123062

# imports
from math import sqrt
from scipy.optimize import minimize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# functions


def showBetaTable(beta, stockName):
    data = {'Stock': stockName, 'Beta-value': beta}
    df = pd.DataFrame(data, columns=['Stock', 'Beta-value'])
    print(df)
    print('\n')


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


# Plot SMLs taking the risk free rate to be 5%
rf = 0.05
# FOR BSE -----------------------------------------------------------------------------------
X = np.linspace(-1, 3, 1000)
Y = rf + (bse_market_ret-rf)*X
plt.plot(X, Y, color='black', label='BSE SML')

stock_name_bse = bse_stocks.iloc[:, 1:].columns
bse_stocks_data = np.transpose(bse_stocks.iloc[:, 1:].to_numpy())
betaArray = []
for i in range(10):
    ret = []
    for j in range(1, len(bse_stocks_data[i])):
        if bse_stocks_data[i][j] == 0:
            bse_stocks_data[i][j] = bse_stocks_data[i][j-1]
        ret.append(
            12*(bse_stocks_data[i][j]-bse_stocks_data[i][j-1])/bse_stocks_data[i][j-1])
    mean_ret = np.mean(ret)
    cov = np.cov(ret, bse_ret)
    beta = cov[0][1]/(bse_market_std**2)
    plt.scatter(beta, mean_ret, marker='X',
                color='red', label=stock_name_bse[i])
    betaArray.append(beta)
print('BSE Stock')
showBetaTable(betaArray, stock_name_bse)


stock_name_non_bse = non_bse_stocks.iloc[:, 1:].columns
non_bse_stocks_data = np.transpose(non_bse_stocks.iloc[:, 1:].to_numpy())
betaArray = []
for i in range(10):
    ret = []
    for j in range(1, len(non_bse_stocks_data[i])):
        if non_bse_stocks_data[i][j] == 0:
            non_bse_stocks_data[i][j] = non_bse_stocks_data[i][j-1]
        ret.append(
            12*(non_bse_stocks_data[i][j]-non_bse_stocks_data[i][j-1])/non_bse_stocks_data[i][j-1])
    mean_ret = np.mean(ret)
    cov = np.cov(ret, bse_ret)
    beta = cov[0][1]/(bse_market_std**2)
    plt.scatter(beta, mean_ret, color='blue',
                label=stock_name_non_bse[i])
    betaArray.append(beta)
print('Non BSE Stock')
showBetaTable(betaArray, stock_name_non_bse)

plt.title("Security Market Line BSE Index")
plt.xlabel("Beta(β)")
plt.ylabel("Mean Return")
plt.legend()
plt.show()


# FOR NSE ---------------------------------------------------------------------------------------------
X = np.linspace(-1, 3, 1000)
Y = rf + (nse_market_ret-rf)*X
plt.plot(X, Y, color='black', label='NSE SML')

stock_name_nse = nse_stocks.iloc[:, 1:].columns
nse_stocks_data = np.transpose(nse_stocks.iloc[:, 1:].to_numpy())
betaArray = []
for i in range(10):
    ret = []
    for j in range(1, len(nse_stocks_data[i])):
        if nse_stocks_data[i][j] == 0:
            nse_stocks_data[i][j] = nse_stocks_data[i][j-1]
        ret.append(
            12*(nse_stocks_data[i][j]-nse_stocks_data[i][j-1])/nse_stocks_data[i][j-1])
    mean_ret = np.mean(ret)
    cov = np.cov(ret, nse_ret)
    beta = cov[0][1]/(nse_market_std**2)
    plt.scatter(beta, mean_ret, marker='X',
                color='red', label=stock_name_nse[i])
    betaArray.append(beta)
print('NSE Stock')
showBetaTable(betaArray, stock_name_nse)

stock_name_non_nse = non_nse_stocks.iloc[:, 1:].columns
non_nse_stocks_data = np.transpose(non_nse_stocks.iloc[:, 1:].to_numpy())
betaArray = []
for i in range(10):
    ret = []
    for j in range(1, len(non_nse_stocks_data[i])):
        if non_nse_stocks_data[i][j] == 0:
            non_nse_stocks_data[i][j] = non_nse_stocks_data[i][j-1]
        ret.append(
            12*(non_nse_stocks_data[i][j]-non_nse_stocks_data[i][j-1])/non_nse_stocks_data[i][j-1])
    mean_ret = np.mean(ret)
    cov = np.cov(ret, nse_ret)
    beta = cov[0][1]/(nse_market_std**2)
    plt.scatter(beta, mean_ret, color='blue',
                label=stock_name_non_nse[i])
    betaArray.append(beta)
print('Non NSE Stock')
showBetaTable(betaArray, stock_name_non_nse)

plt.title("Security Market Line NSE Index")
plt.xlabel("Beta(β)")
plt.ylabel("Mean Return")
plt.legend()
plt.show()
