# Question 5, Lab 06
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


def getPredictedPrices(S, futurePoints):
    curPrice = S[-1]
    mu, sig = getMuSigma(S)

    predictedPrices = []
    for i in range(futurePoints):  # 246 = 1232 - 986 (number of future points to predict)
        nextPrice = getNextPrice(0.1, mu, sig, curPrice)
        predictedPrices.append(nextPrice)
        curPrice = nextPrice

    return np.array(predictedPrices)


# program body
# For BSE
dfBSEWeekly = pd.read_csv('BSE/wbsedata1.csv')
dfBSEMonthly = pd.read_csv('BSE/mbsedata1.csv')

# For NSE
dfNSEWeekly = pd.read_csv('NSE/wnsedata1.csv')
dfNSEMonthly = pd.read_csv('NSE/mnsedata1.csv')

# Plots for BSE - For plots look at Plots/Question 5/BSE/
dfBSE = [dfBSEWeekly, dfBSEMonthly]

columnHeaders = np.array(dfBSEWeekly.columns)[1:]
intervals = ['Weekly', 'Monthly']
colors = ['blue', 'red']
trainPoints = [209, 48]
futurePoints = [52, 12]


for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    for j in range(2):
        df = dfBSE[j]
        dataActual = np.array(df[header])
        # Train data represents data till 31 Dec 2017
        dataTrain = dataActual[:trainPoints[j]]
        # Remove nan from data
        dataActual = dataActual[~np.isnan(dataActual)]
        dataTrain = dataTrain[~np.isnan(dataTrain)]

        # Get Predicted Prices
        predictedData = getPredictedPrices(dataTrain, futurePoints[j])
        dataTrain = np.concatenate((dataTrain, predictedData))
        X = np.arange(0, dataActual.shape[0], 1)

        plt.plot(X, dataTrain, label='Predicted', color='green')
        plt.plot(X, dataActual, label='Actual', color=colors[j])
        plt.xlabel('Time points - {} basis'.format(intervals[j]))
        plt.ylabel('Stock prices')
        plt.title(
            'Stock Prices vs Time ({}) for BSE - {}'.format(intervals[j], header))
        plt.legend()
        # plt.savefig(
        #     'Plots/Question 5/BSE/{}/{}.png'.format(intervals[j], header))
        plt.show()

# Plots for NSE - For plots look at Plots/Question 5/NSE/
dfNSE = [dfNSEWeekly, dfNSEMonthly]

columnHeaders = np.array(dfNSEWeekly.columns)[1:]
intervals = ['Weekly', 'Monthly']
colors = ['blue', 'red']
trainPoints = [209, 48]
futurePoints = [52, 12]


for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    for j in range(2):
        df = dfNSE[j]
        dataActual = np.array(df[header])
        # Train data represents data till 31 Dec 2017
        dataTrain = dataActual[:trainPoints[j]]
        # Remove nan from data
        dataActual = dataActual[~np.isnan(dataActual)]
        dataTrain = dataTrain[~np.isnan(dataTrain)]

        # Get Predicted Prices
        predictedData = getPredictedPrices(dataTrain, futurePoints[j])
        dataTrain = np.concatenate((dataTrain, predictedData))
        X = np.arange(0, dataActual.shape[0], 1)

        plt.plot(X, dataTrain, label='Predicted', color='green')
        plt.plot(X, dataActual, label='Actual', color=colors[j])
        plt.xlabel('Time points - {} basis'.format(intervals[j]))
        plt.ylabel('Stock prices')
        plt.title(
            'Stock Prices vs Time ({}) for NSE - {}'.format(intervals[j], header))
        plt.legend()
        # plt.savefig(
        #     'Plots/Question 5/NSE/{}/{}.png'.format(intervals[j], header))
        plt.show()
