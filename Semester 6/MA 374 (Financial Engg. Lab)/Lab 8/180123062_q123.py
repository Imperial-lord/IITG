# Question 01, 02, 03 Lab 08
# AB Satyaprakash, 180123062

# imports
from scipy.stats import norm
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:.6f}'.format

# functions


def get_data_stocks(file):
    df = pd.read_csv(file).iloc[:, 1:]
    df.fillna(method='ffill', inplace=True)
    df = df.astype(float)
    for i in range(len(df)-1):
        df.iloc[i, :] = (df.iloc[i+1, :] - df.iloc[i, :])/df.iloc[i, :]

    S0 = df.iloc[-1, :]
    df = df.iloc[:-1]
    return S0, df


def get_data_indices(file):
    df = pd.read_csv(file).iloc[:, 1:]
    df.fillna(method='ffill', inplace=True)
    df = df.astype(float)
    for i in range(len(df)-1):
        df.iloc[i, :] = (df.iloc[i+1, :] - df.iloc[i, :])/df.iloc[i, :]

    S0 = df['Adj Close'][1231]
    df = df.iloc[:-1]
    return S0, df['Adj Close'].values


def N(x):
    return norm.cdf(x)


def BSM(x, sigma, K, t=0.5, r=0.05):
    if t == 0:
        call = max(0, x - K)
        put = max(0, K - x)
    else:
        d1 = (np.log(x/K) + (r + sigma**2/2)*t)/(sigma * np.sqrt(t))
        d2 = d1 - sigma * np.sqrt(t)
        call = N(d1)*x - N(d2)*K*np.exp(-r*t)
        put = call + K*np.exp(-r*t) - x

    return call, put


def get_sigma(returns):
    return np.sqrt(np.var(returns)*252)


def get_option_price(returns, S0, A):
    sigma = get_sigma(returns)
    K = A*S0
    C, P = BSM(S0, sigma, K)
    return C, P, sigma


# program body
# FOR BSE Stocks
file = 'BSE/bsedata1.csv'
BSECompanies = np.array(pd.read_csv(file).columns)[1:]
allS0, allReturns = get_data_stocks(file)

for company in BSECompanies:
    title = company+' (BSE)'
    arrA = np.arange(0.5, 1.51, 0.1).round(1)
    S0, returns = allS0[company], allReturns[company]
    n = len(returns)

    for A in arrA:
        df = pd.DataFrame()
        i = 1
        while i*25 < n:
            ret = returns[-i*25:]
            C, P, sigma = get_option_price(ret, S0, A)
            row = pd.DataFrame([[i, sigma, C, P]])
            df = df.append(row)
            i += 1
        # Rename the dictionary
        mapmaker = dict(
            zip([0, 1, 2, 3], ['Month(s)', 'Sigma', 'Call Option', 'Put Option']))
        df = df.rename(columns=mapmaker).reset_index(drop=True)
        print('\nData of {} with A = {}\n'.format(title, A))
        print(df)
        df.plot(x='Month(s)', y=['Sigma', 'Call Option', 'Put Option'],
                subplots=True, title='Plot of {} with A = {}'.format(title, A), figsize=(6, 10))
        plt.savefig('Plots/BSEStocks/{}_{}.png'.format(title, A))
    # plt.show()
    plt.close()

# FOR NSE Stocks
file = 'NSE/nsedata1.csv'
NSECompanies = np.array(pd.read_csv(file).columns)[1:]
allS0, allReturns = get_data_stocks(file)

for company in NSECompanies:
    title = company+' (NSE)'
    arrA = np.arange(0.5, 1.51, 0.1).round(1)
    S0, returns = allS0[company], allReturns[company]
    n = len(returns)

    for A in arrA:
        df = pd.DataFrame()
        i = 1
        while i*25 < n:
            ret = returns[-i*25:]
            C, P, sigma = get_option_price(ret, S0, A)
            row = pd.DataFrame([[i, sigma, C, P]])
            df = df.append(row)
            i += 1
        # Rename the dictionary
        mapmaker = dict(
            zip([0, 1, 2, 3], ['Month(s)', 'Sigma', 'Call Option', 'Put Option']))
        df = df.rename(columns=mapmaker).reset_index(drop=True)
        print('\nData of {} with A = {}\n'.format(title, A))
        print(df)
        df.plot(x='Month(s)', y=['Sigma', 'Call Option', 'Put Option'],
                subplots=True, title='Plot of {} with A = {}'.format(title, A), figsize=(6, 10))
        plt.savefig('Plots/NSEStocks/{}_{}.png'.format(title, A))
    # plt.show()
    plt.close()


# FOR BSE INDICES
file = 'BSE/bseindex1.csv'
title = 'BSE Index'
arrA = np.arange(0.5, 1.51, 0.1).round(1)
S0, returns = get_data_indices(file)
n = len(returns)

for A in arrA:
    df = pd.DataFrame()
    i = 1
    while i*25 < n:
        ret = returns[-i*25:]
        C, P, sigma = get_option_price(ret, S0, A)
        row = pd.DataFrame([[i, sigma, C, P]])
        df = df.append(row)
        i += 1
    # Rename the dictionary
    mapmaker = dict(
        zip([0, 1, 2, 3], ['Month(s)', 'Sigma', 'Call Option', 'Put Option']))
    df = df.rename(columns=mapmaker).reset_index(drop=True)
    print('\nData of {} with A = {}\n'.format(title, A))
    print(df)
    df.plot(x='Month(s)', y=['Sigma', 'Call Option', 'Put Option'],
            subplots=True, title='Plot of {} with A = {}'.format(title, A), figsize=(6, 10))
    plt.savefig('Plots/BSEIndices/{}_{}.png'.format(title, A))
# plt.show()
plt.close()


# FOR NSE INDICES
file = 'NSE/nseindex1.csv'
title = 'NSE Index'
arrA = np.arange(0.5, 1.51, 0.1).round(1)
S0, returns = get_data_indices(file)
n = len(returns)

for A in arrA:
    df = pd.DataFrame()
    i = 1
    while i*25 < n:
        ret = returns[-i*25:]
        C, P, sigma = get_option_price(ret, S0, A)
        row = pd.DataFrame([[i, sigma, C, P]])
        df = df.append(row)
        i += 1
    # Rename the dictionary
    mapmaker = dict(
        zip([0, 1, 2, 3], ['Month(s)', 'Sigma', 'Call Option', 'Put Option']))
    df = df.rename(columns=mapmaker).reset_index(drop=True)
    print('\nData of {} with A = {}\n'.format(title, A))
    print(df)
    df.plot(x='Month(s)', y=['Sigma', 'Call Option', 'Put Option'],
            subplots=True, title='Plot of {} with A = {}'.format(title, A), figsize=(6, 10))
    plt.savefig('Plots/NSEIndices/{}_{}.png'.format(title, A))
# plt.show()
plt.close()
