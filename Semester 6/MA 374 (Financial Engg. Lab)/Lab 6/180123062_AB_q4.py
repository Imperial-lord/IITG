# Question 4, Lab 06
# AB Satyaprakash - 180123062

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

# functions


def getMuSigma(S):
    # To obtain log returns use the formula
    # R(i) = log(1+(S(i+1)-S(i))/S(i))
    R = [0]
    for i in range(S.shape[0]-1):
        ret = np.log(1 + (S[i+1]-S[i])/S[i])
        R.append(ret)
    mu = statistics.mean(R)
    sig = statistics.stdev(R)

    return mu, sig


def getNextPrice(lam, mu, sig, St):
    Xt = np.log(St)
    Z = np.random.normal(0, 1)
    dt = 1
    N = np.random.poisson(lam*dt)

    # calculate jump
    M = 0
    if(N != 0):
        for i in range(N):
            Y = np.random.lognormal(mu, sig)
            M += np.log(Y)

    Xt_ = Xt + (mu - (sig**2)/2)*dt + sig*Z*np.sqrt(dt) + M
    St_ = np.exp(Xt_)

    return St_


def getPredictedPrices(S):
    curPrice = S[-1]
    mu, sig = getMuSigma(S)

    predictedPrices = []
    for i in range(246):  # 246 = 1232 - 986 (number of future points to predict)
        nextPrice = getNextPrice(0.1, mu, sig, curPrice)
        predictedPrices.append(nextPrice)
        curPrice = nextPrice

    return np.array(predictedPrices)


# program body
# For BSE
dfBSEDaily = pd.read_csv('BSE/dbsedata1.csv')

# For NSE
dfNSEDaily = pd.read_csv('NSE/dnsedata1.csv')

# Plots for BSE - For plots look at Plots/Question 4/BSE/
columnHeaders = np.array(dfBSEDaily.columns)[1:]

for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    df = dfBSEDaily
    dataActual = np.array(df[header])
    dataTrain = dataActual[:986]  # Train data represents data till 31 Dec 2017
    # Remove nan from data
    dataActual = dataActual[~np.isnan(dataActual)]
    dataTrain = dataTrain[~np.isnan(dataTrain)]

    # Get Predicted Prices
    predictedData = getPredictedPrices(dataTrain)
    dataTrain = np.concatenate((dataTrain, predictedData))
    X = np.arange(0, 1230, 1)

    plt.plot(X, dataTrain, label='Predicted', color='green')
    plt.plot(X, dataActual, label='Actual', color='orange')
    plt.xlabel('Time points - Daily basis')
    plt.ylabel('Stock prices')
    plt.title('Stock Prices vs Time (Daily) for BSE - {}'.format(header))
    plt.legend()
    # plt.savefig(
    #     'Plots/Question 4/BSE/Daily/{}.png'.format(header))
    plt.show()

# Plots for NSE - For plots look at Plots/Question 4/NSE/
columnHeaders = np.array(dfNSEDaily.columns)[1:]

for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    df = dfNSEDaily
    dataActual = np.array(df[header])
    dataTrain = dataActual[:986]  # Train data represents data till 31 Dec 2017
    # Remove nan from data
    dataActual = dataActual[~np.isnan(dataActual)]
    dataTrain = dataTrain[~np.isnan(dataTrain)]

    # Get Predicted Prices
    predictedData = getPredictedPrices(dataTrain)
    dataTrain = np.concatenate((dataTrain, predictedData))
    X = np.arange(0, 1230, 1)

    plt.plot(X, dataTrain, label='Predicted', color='green')
    plt.plot(X, dataActual, label='Actual', color='orange')
    plt.xlabel('Time points - Daily basis')
    plt.ylabel('Stock prices')
    plt.title('Stock Prices vs Time (Daily) for NSE - {}'.format(header))
    plt.legend()
    # plt.savefig(
    #     'Plots/Question 4/NSE/Daily/{}.png'.format(header))
    plt.show()
