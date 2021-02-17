# Lab 05
# AB Satyaprakash - 180123062

# imports
from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# functions
def readCSV(filename):
    df = pd.read_csv(filename)
    return df


# body of program
# Read the data for 10 stocks from bsedata1.csv and nsedata1.csv
dataBSE = np.array(readCSV('./BSE/bsedata1.csv'))
dataNSE = np.array(readCSV('./NSE/nsedata1.csv'))

# Combine the dataNSE and dataBSE into 1 np 2-D array
data = []
for i in range(dataBSE.shape[0]):
    temp = np.concatenate((dataBSE[i], dataNSE[i]))
    data.append(temp)
data = np.array(data)

# Read the data of BSE (SENSEX) and NSE (NIFTY) index values from Jan 1, 2014 to Dec 31, 2018
# The data has been stored in BSE.csv and NSE.csv
bseIndex = np.array(readCSV('./BSE/BSE.csv').Close)
nseIndex = np.array(readCSV('./NSE/NSE.csv').Price)

# Obtain stock prices from closing prices using (S(i+1)-S(i))/S(i)
tempData, tempBSEIndex, tempNSEIndex = data.copy(), bseIndex.copy(), nseIndex.copy()

for i in range(1, tempData.shape[0]):
    data[i] = (tempData[i]-tempData[i-1])/tempData[i-1]
data[0] = np.zeros(tempData.shape[1])

for i in range(1, tempBSEIndex.shape[0]):
    bseIndex[i] = (tempBSEIndex[i]-tempBSEIndex[i-1])/tempBSEIndex[i-1]

for i in range(1, tempNSEIndex.shape[0]):
    nseIndex[i] = (tempNSEIndex[i]-tempNSEIndex[i-1])/tempNSEIndex[i-1]
bseIndex[0], nseIndex[0] = 0, 0

mu_m_bse = np.mean(bseIndex)
sigma_m_bse = sqrt(np.var(bseIndex))

mu_m_nse = np.mean(nseIndex)
sigma_m_nse = sqrt(np.var(nseIndex))

M = np.mean(data, axis=0)

# Given risk free rate = 5%
rf = 0.05

betaBSE = (M-rf)/(mu_m_bse-rf)
betaNSE = (M-rf)/(mu_m_nse-rf)

# Plotting SMLs
beta = np.arange(-1, 1.51, 0.01)
mu_v_bse = rf + (mu_m_bse-rf)*beta
mu_v_nse = rf + (mu_m_nse-rf)*beta
plt.plot(beta, mu_v_nse, label='NSE')
plt.plot(beta, mu_v_bse, label='BSE')
plt.scatter(1, mu_m_nse, label='NSE INDEX')
plt.scatter(1, mu_m_bse, label='BSE INDEX')
plt.xlabel('β')
plt.ylabel('μᵥ')
plt.title('Security Market lines')
plt.legend()
plt.show()

# Difference in SMLs
plt.plot(beta, mu_v_bse-mu_v_nse)
plt.xlabel('β')
plt.ylabel('β_BSE - β_NSE')
plt.title('Difference in SMLs')
plt.show()
