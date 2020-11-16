import pandas as pd;
import math;
import random;
import statistics;

#read and store
sbiData=pd.read_csv('SBIN.NS.csv')
stockPricesClosing=sbiData['Adj Close'].to_list() #taking the stock prices corresponding to the adjusted closing prices!

u=[] #will store the log-returns

def calLogReturns(): #function calculates the log returns using ln(s[i]/s[i-1])
    for i in range(1,len(stockPricesClosing)):
        s_i=stockPricesClosing[i]
        s_i_1=stockPricesClosing[i-1]
        u.append(math.log(s_i/s_i_1))

def calEstMuSigma(): #function calculates the estimated values of mu and sigma
    #calculate E(u)
    sumU=sum(u)
    n=len(u)
    eU=sumU/n
    
    #caculate estimated sigma-square
    diff=0
    for i in range (0,n):
        diff+=(u[i]-eU)**2
    sigmaSquare=diff/(n-1)
    
    #calculate estimated mu
    mu=eU+(sigmaSquare/2)
    return [mu,sigmaSquare]

def find_values_N01(): #this function uses the box-muller algorithm and generates 1000 values of N(0,1)
    n01_1000=[]
    for i in range(0,1000):
        u1=random.uniform(0,1)
        u2=random.uniform(0,1)
        r=-2*math.log(u1)
        v=2*math.pi*u2
        z1=math.sqrt(r)*math.cos(v)
        z2=math.sqrt(r)*math.sin(v)
        if(i%2==0):
            n01_1000.append(z1)
        else:
            n01_1000.append(z2)
    return n01_1000
    
calLogReturns()
[mu,sigmaSquare]=calEstMuSigma()

print("Estimated value of \u03BC (mean) = "+str(mu))
print("Estimated value of \u03C3 (standard deviation) = "+str(math.sqrt(sigmaSquare)))
print('\n')

t=[4,9,14] #the number of days from S(0) corresponding to 7th, 14th and 21st Oct.
days=['7th October 2020', '14th October 2020', '21st October 2020']
S0=185.40 #S(0) has been taken for 30th of September.

SActual=[190.70,200.05,203.75] #the actual adjusted closing stock price corresponding to 7th, 14th and 21st Oct.
percentError=[]

for i in range(0,3): # calculate expected Stock prices for 3 different dates
    Z=find_values_N01()
    S=[] #store 1000 possible values for stock prices
    for j in range(0,1000):
        expfact=(mu-sigmaSquare/2)*t[i]
        expfact+=math.sqrt(sigmaSquare*t[i])*Z[j]
        val=S0*math.exp(expfact)
        S.append(val)
    meanStockPrice=statistics.mean(S)
    diff=abs(meanStockPrice-SActual[i])
    error=diff/SActual[i]
    error*=100
    percentError.append(error)
    print("Expected Stock price S(t) on "+days[i]+" = "+str(meanStockPrice))
    
print('\n')

for i in range(0,3): #print the %error for 3 different dates
    print("Percentage error in expected Stock prices = "+str(percentError[i])+"%")
