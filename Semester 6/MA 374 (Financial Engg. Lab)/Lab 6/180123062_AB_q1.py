# Question 1, Lab 06
# AB Satyaprakash - 180123062

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# functions

# program body
# For BSE
dfBSEDaily = pd.read_csv('BSE/dbsedata1.csv')
dfBSEWeekly = pd.read_csv('BSE/wbsedata1.csv')
dfBSEMonthly = pd.read_csv('BSE/mbsedata1.csv')

# For NSE
dfNSEDaily = pd.read_csv('NSE/dnsedata1.csv')
dfNSEWeekly = pd.read_csv('NSE/wnsedata1.csv')
dfNSEMonthly = pd.read_csv('NSE/mnsedata1.csv')

# Plots for BSE - For plots look at Plots/Question 1/BSE/
dfBSE = [dfBSEDaily, dfBSEWeekly, dfBSEMonthly]

columnHeaders = np.array(dfBSEDaily.columns)[1:]
intervals = ['Daily', 'Weekly', 'Monthly']
colors = ['orange', 'blue', 'red']

for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    for j in range(3):
        df = dfBSE[j]
        data = np.array(df[header])
        timeAxis = np.arange(0, data.shape[0], 1)
        plt.plot(timeAxis, data, color=colors[j])
        plt.xlabel('Time points - {} basis'.format(intervals[j]))
        plt.ylabel('Stock prices')
        plt.title('Stock Prices vs Time ({}) for BSE - {}'.format(
            intervals[j], header))
        # plt.savefig(
        #     'Plots/Question 1/BSE/{}/{}.png'.format(intervals[j], header))
        plt.show()


# Plots for NSE - For plots look at Plots/Question 1/NSE/
dfNSE = [dfNSEDaily, dfNSEWeekly, dfNSEMonthly]

columnHeaders = np.array(dfNSEDaily.columns)[1:]
intervals = ['Daily', 'Weekly', 'Monthly']
colors = ['orange', 'blue', 'red']

for i in range(columnHeaders.shape[0]):
    header = columnHeaders[i]
    for j in range(3):
        df = dfNSE[j]
        data = np.array(df[header])
        timeAxis = np.arange(0, data.shape[0], 1)
        plt.plot(timeAxis, data, color=colors[j])
        plt.xlabel('Time points - {} basis'.format(intervals[j]))
        plt.ylabel('Stock prices')
        plt.title('Stock Prices vs Time ({}) for NSE - {}'.format(
            intervals[j], header))
        # plt.savefig(
        #     'Plots/Question 1/NSE/{}/{}.png'.format(intervals[j], header))
        plt.show()
