# Question 04, Lab 09
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

def get_data2(file, cols):

    df = pd.read_csv(file, index_col=0)
    df = df.astype(float)
    for i in range(len(df)-1):
        df.iloc[i, :] = (df.iloc[i+1, :] - df.iloc[i, :])/df.iloc[i, :]

    df = df[cols]
    S0 = df.iloc[-1]
    df = df.iloc[:-1]
    return df.values, S0


def get_sigma(returns):
    return np.sqrt(np.var(returns, axis=0)*252)


def get_historical_vol(file):
    cols = ['GAIL', 'IOC', 'ONGC', 'TATAMOTORS']

    I = [25, 50, 75]
    returns, S0 = get_data2(file, cols)
    arr = []
    for i in I:
        ret = returns[-i:]
        arr.append(get_sigma(ret))

    df = pd.DataFrame(arr, columns=cols, index=[
                      '1 months', '2 months', '3 months'])
    display(df)
    df.to_csv('HistoricalVolatility.csv')


get_historical_vol('nsedata1.csv')

df = pd.read_csv('HistoricalVolatility.csv')
duration = [1, 2, 3]
gail = np.array(df['GAIL'])
ioc = np.array(df['IOC'])
ongc = np.array(df['ONGC'])
tatamotors = np.array(df['TATAMOTORS'])

plt.plot(duration, gail)
plt.plot(duration, ioc)
plt.plot(duration, ongc)
plt.plot(duration, tatamotors)
plt.title('Plot of Historical Volatility vs Time in months')
plt.xlabel('Time in months')
plt.ylabel('Historical Volatility')
plt.show()
plt.savefig('Plots/Question 4/historicalvol.png')
