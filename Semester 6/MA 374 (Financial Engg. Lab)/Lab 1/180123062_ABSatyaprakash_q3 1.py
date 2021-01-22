# Q.3 Tabulate the values of the options at t = 0, 0.50, 1, 1.50, 3, 4.5 for the case M = 20.

# Pandas : pip install pandas 
# Matplotlib: pip install matplotlib 
# Numpy: pip install numpy 
# Ipython: pip install ipython

import pandas as pd
from IPython.display import display
import math

# Given data
S0=100
K=105
T=5
r=0.05
sig=0.3
callPrices = []
putPrices = []
timeSteps = [0, 2, 4, 6, 12, 18]

# Function to get Option Price for a given M
def getOptionPrice(M, timeSteps):
    dt = T/M
    u = math.exp(sig*math.sqrt(dt)+(r-sig*sig/2)*dt)
    d = math.exp(-sig*math.sqrt(dt)+(r-sig*sig/2)*dt)
    p = (math.exp(r*dt)-d)/(u-d)
    ptr = len(timeSteps)-1
    
    if p < 0 or p > 1:
        print("No Arbitrage Principle has been violated")
        return
    
    callList = [0]*(M+1)
    putList = [0]*(M+1)
    
    for i in range(M+1):
        callList[i] = max(S0*(u**(M-i))*(d**i) - K, 0)
        putList[i] = max(0, K - S0*(u**(M-i))*(d**i))
        
    for i in range(M):
        for j in range(M-i):
            callList[j] = ((1-p)*callList[j] + p*callList[j+1])*math.exp(-r*T/M)
            putList[j] = ((1-p)*putList[j] + p*putList[j+1])*math.exp(-r*T/M)
        if ptr>=0 and i+1 == M - timeSteps[ptr]:
            ptr-=1
            tempCall = callList[:(timeSteps[ptr+1]+1)]
            tempPut = putList[:(timeSteps[ptr+1]+1)]
            callPrices.append(tempCall)
            putPrices.append(tempPut)


getOptionPrice(20, timeSteps)

for i in range(len(timeSteps)):
    timeSteps[i] = timeSteps[i]*0.25

columns = []
for i in range(19):
    st = 'd'+str(i)
    columns.append(st)

df = pd.DataFrame(data=reversed(callPrices), index=timeSteps, columns = columns)
display(df)

df = pd.DataFrame(data=reversed(putPrices), index=timeSteps, columns = columns)
display(df)
