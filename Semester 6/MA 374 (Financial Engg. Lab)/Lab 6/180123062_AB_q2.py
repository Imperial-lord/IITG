# Question 2, Lab 06
# AB Satyaprakash - 180123062

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

# functions


def N(x):
    # mean =0, var =1
    return (1/(np.sqrt(2*np.pi)))*(np.exp((-0.5*x*x)))


def getReturns(S):
    # To obtain returns use the formula
    # R(i) = (S(i+1)-S(i))/S(i)
    R = [0]
    for i in range(S.shape[0]-1):
        ret = (S[i+1]-S[i])/S[i]
        R.append(ret)
    return np.array(R)


def getNormalisedReturns(R):
    # To obtain normalised returns use the formula
    # R'(i) = (R(i)-μ)/σ
    meanReturn = statistics.mean(R)
    sdReturns = statistics.stdev(R)
    nR = (R-meanReturn)/sdReturns
    return nR


# program body
# For BSE
dfBSEDaily = pd.read_csv('BSE/dbsedata1.csv')
dfBSEWeekly = pd.read_csv('BSE/wbsedata1.csv')
dfBSEMonthly = pd.read_csv('BSE/mbsedata1.csv')

# For NSE
dfNSEDaily = pd.read_csv('NSE/dnsedata1.csv')
dfNSEWeekly = pd.read_csv('NSE/wnsedata1.csv')
dfNSEMonthly = pd.read_csv('NSE/mnsedata1.csv')

# Plots for BSE - For plots look at Plots/Question 2/BSE/
dfBSE = [dfBSEDaily, dfBSEWeekly, dfBSEMonthly]

columnHeaders = np.array(dfBSEDaily.columns)[1:]
intervals = ['Daily', 'Weekly', 'Monthly']
colors = ['orange', 'slateblue', 'salmon']

for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    for j in range(3):
        df = dfBSE[j]
        data = np.array(df[header])
        data = data[~np.isnan(data)]
        returns = getReturns(data)
        nomralisedReturns = getNormalisedReturns(returns)

        y, x, _ = plt.hist(nomralisedReturns, bins='auto',
                           color=colors[j], rwidth=0.85, label='Returns', density=1)

        # Obtain X and Y for N(0,1) plot
        X = np.arange(min(nomralisedReturns), max(nomralisedReturns), 1/10000)
        Y = N(X)
        plt.plot(X, Y, label='N(0,1)', color='black')
        plt.xlabel('Normalised Returns - {} basis'.format(intervals[j]))
        plt.ylabel('Frequency of Normalised Returns')
        plt.title('Histogram of Normalised Returns ({}) for BSE - {}'.format(
            intervals[j], header))
        plt.legend()
        # plt.savefig(
        #     'Plots/Question 2/BSE/{}/{}.png'.format(intervals[j], header))
        plt.show()


# Plots for NSE - For plots look at Plots/Question 2/NSE/
dfNSE = [dfNSEDaily, dfNSEWeekly, dfNSEMonthly]

columnHeaders = np.array(dfNSEDaily.columns)[1:]
intervals = ['Daily', 'Weekly', 'Monthly']
colors = ['orange', 'slateblue', 'salmon']

for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    for j in range(3):
        df = dfNSE[j]
        data = np.array(df[header])
        data = data[~np.isnan(data)]
        returns = getReturns(data)
        nomralisedReturns = getNormalisedReturns(returns)

        y, x, _ = plt.hist(nomralisedReturns, bins='auto',
                           color=colors[j], rwidth=0.85, label='Returns', density=1)

        # Obtain X and Y for N(0,1) plot
        X = np.arange(min(nomralisedReturns), max(nomralisedReturns), 1/10000)
        Y = N(X)
        plt.plot(X, Y, label='N(0,1)', color='black')
        plt.xlabel('Normalised Returns - {} basis'.format(intervals[j]))
        plt.ylabel('Frequency of Normalised Returns')
        plt.title('Histogram of Normalised Returns ({}) for NSE - {}'.format(
            intervals[j], header))
        plt.legend()
        # plt.savefig(
        #     'Plots/Question 2/NSE/{}/{}.png'.format(intervals[j], header))
        plt.show()
