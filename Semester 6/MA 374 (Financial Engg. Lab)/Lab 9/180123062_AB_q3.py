# Question 03, Lab 09
# AB Satyaprkash, 180123062

# imports
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from IPython.display import display
import math
from scipy.stats import norm


# functions
def getData(file):
    df = pd.read_csv(file)
    df = df[['Expiry', 'Strike Price', 'Close']]
    mapper = dict(
        zip(df.columns, ['Maturity', 'Strike Price', 'Option Price']))
    df = df.rename(columns=mapper)
    return df


def plotGraphs(fileName):
    df = pd.read_csv(fileName)
    # extract and rename columns
    df = df[['Maturity', 'Strike Price', 'Volatility']]
    mapper = dict(
        zip(df.columns, ['Maturity', 'Strike Price', 'Volatility']))
    df = df.rename(columns=mapper)
    df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
    print(df)
    plotTitle = fileName.split('/')[-1][:-4]

    # 2D Plot of Volatility vs Maturity
    df.plot(x='Maturity', y='Volatility', kind='scatter',
            title=f'Volatility vs Maturity for {plotTitle}', figsize=(8, 8), color='blue')
    plt.savefig(f'Plots/Question 3/{plotTitle}_1.png')
    plt.show()

    # 2D Plot of Volatility vs Strike Price
    df.plot(x='Strike Price', y='Volatility', kind='scatter',
            title=f'Volatility vs Strike Price for {plotTitle}', figsize=(8, 8), color='red')
    plt.savefig(f'Plots/Question 3/{plotTitle}_2.png')
    plt.show()

    df['Maturity'] = df['Maturity'].astype('datetime64[ns]')
    fig = plt.figure(figsize=(10, 10))
    ax = Axes3D(fig)
    ax.plot_trisurf(df['Maturity'], df['Strike Price'],
                    df['Volatility'])
    ax.set_title(f'3D Plot for {plotTitle}')
    ax.set_xlabel('Maturity in Nanoseconds')
    ax.set_ylabel('Strike Price')
    ax.set_zlabel('Volatility')
    plt.savefig(f'Plots/Question 3/{plotTitle}_3.png')
    plt.show()


def N(x):
    return norm.cdf(x)


def BSM(x, sigma, K, t=0.5, r=0.05, option='call'):

    if t == 0:
        call = max(0, x - K)
        put = max(0, K - x)

    else:
        d1 = (math.log(x/K) + (r + sigma**2/2)*t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)

        call = N(d1)*x - N(d2)*K*math.exp(-r*t)
        put = call + K*math.exp(-r*t) - x

    if option == 'call':
        return call
    else:
        return put


def f(opt_price, stock_price, K, r, t, sigma, option='call'):
    return BSM(stock_price, sigma, K, t, r, option) - opt_price


def findRootNR(opt_price, stock_price, K, r, t, option='Call'):

    a = 0.1
    b = 0.2
    thresh = 0.00001
    num = 100
    alpha = 0.1

    for i in range(num):
        c = b - f(opt_price, stock_price, K, r, t, b, option)*(b-a)/(f(opt_price, stock_price,
                                                                       K, r, t, b, option)-f(opt_price, stock_price, K, r, t, a, option) + alpha)
        a = b
        b = c

        if abs(f(opt_price, stock_price, K, r, t, b, option)) < thresh:
            break

    return b


def getVolatility(file):

    option = file.split('/')[-1].split('_')[-1][:-4]

    if option == 'CE':
        option = 'call'
    else:
        option = 'put'

    name = file.split('/')[-1].split('_')[0]

    nse = pd.read_csv('nsedata1.csv', index_col=0)
    nse = nse[name]

    df = getData(file)

    stock_price = nse[-1]
    r = 0.05
    vols = []
    T = pd.to_datetime(df['Maturity']) - \
        pd.to_datetime(pd.Series('2018-12-31', index=df.index))

    for i, t in enumerate(T):
        t = t.days/365
        vols.append(
            findRootNR(df.iloc[i, 2], stock_price, df.iloc[i, 1], r, t, option))

    df['Volatility'] = pd.Series(vols)
    df.to_csv('Volatility/' + name + f'_{option}.csv', index=False)
    display(df)


fileNameArray = ['Stock Options/GAIL/GAIL_CE.csv', 'Stock Options/GAIL/GAIL_PE.csv',
                 'Stock Options/IOC/IOC_CE.csv', 'Stock Options/IOC/IOC_PE.csv', 'Stock Options/ONGC/ONGC_CE.csv', 'Stock Options/ONGC/ONGC_PE.csv', 'Stock Options/TATAMOTORS/TATAMOTORS_CE.csv',
                 'Stock Options/TATAMOTORS/TATAMOTORS_PE.csv']

for fileName in fileNameArray:
    getVolatility(fileName)


fileNameArray = ['Volatility/GAIL_call.csv', 'Volatility/GAIL_put.csv', 'Volatility/IOC_call.csv', 'Volatility/IOC_put.csv',
                 'Volatility/ONGC_call.csv', 'Volatility/ONGC_put.csv', 'Volatility/TATAMOTORS_call.csv', 'Volatility/TATAMOTORS_put.csv']

for fileName in fileNameArray:
    plotGraphs(fileName)
