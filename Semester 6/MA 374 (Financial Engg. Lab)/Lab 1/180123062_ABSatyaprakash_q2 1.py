# Q.2 How do the values of options at time t = 0 compare for various values of M? Compute and plot graphs (of the
# initial option prices) varying M in steps of 1 and in steps of 5. What do you observe about the convergence of
# option prices?

# Pandas : pip install pandas 
# Matplotlib: pip install matplotlib 
# Numpy: pip install numpy 
# Ipython: pip install ipython

import math
import numpy as np
import matplotlib.pyplot as plt

# Given data
S0=100
K=105
T=5
r=0.05
sig=0.3

# Function to get Option Price for a given M
def getOptionPrice(M):
    dt = T/M
    u = math.exp(sig*math.sqrt(dt)+(r-sig*sig/2)*dt)
    d = math.exp(-sig*math.sqrt(dt)+(r-sig*sig/2)*dt)
    p = (math.exp(r*dt)-d)/(u-d)
    
    # Check if No Arbitrage Principle has got violated
    if p < 0 or p > 1:
        print("No Arbitrage Principle has been Violated")
        return '-','-'
    
    callList = [0]*(M+1)
    putList = [0]*(M+1)
    
    for i in range(M+1):
        callList[i] = max(S0*(u**i)*(d**(M-i)) - K, 0)
        putList[i] = max(0, K - S0*(u**i)*(d**(M-i)))
        
    for i in range(M):
        for j in range(M-i):
            callList[j] = ((1-p)*callList[j] + p*callList[j+1])*math.exp(-r*T/M)
            putList[j] = ((1-p)*putList[j] + p*putList[j+1])*math.exp(-r*T/M)
    return callList[0], putList[0]

# Lists to store the option prices
callPrices = []
putPrices = []
M=0
# Compute initial option prices in steps of 1
while M < 400:
    M += 1
    call, put = getOptionPrice(M)
    callPrices.append(call)
    putPrices.append(put)
MList = np.linspace(1, 400, 400)

plt.plot(MList, callPrices)
plt.xlabel('Value of M')
plt.ylabel('Call Option Price')
plt.title('Varying Price of Call Option with Value of M (Step Size 1)')
plt.show()

plt.plot(MList, putPrices)
plt.xlabel('Value of M')
plt.ylabel('Price of Put Option')
plt.title('Varying Price of Put Option with Value of M (Step Size 1)')
plt.show()

# Lists to store the option prices
callPrices = []
putPrices = []

# Compute initial option prices in steps of 5
M=0
while M < 400:
    M += 5
    call, put = getOptionPrice(M)
    callPrices.append(call)
    putPrices.append(put)
MList = np.linspace(1, 400, 80)

plt.plot(MList, callPrices)
plt.xlabel('Value of M')
plt.ylabel('Call Option Price')
plt.title('Varying Call Option Price with Value of M (Step Size 5)')
plt.show()

plt.plot(MList, putPrices)
plt.xlabel('Value of M')
plt.ylabel('Price of Put Option')
plt.title('Varying Put Option Price with Value of M (Step Size 5)')
plt.show()
