import pandas as pd;
import math;
import random;
import statistics;

#-------------------------------------lab 7 work-------------------------------#
#read and store
sbiData=pd.read_csv('SBIN.NS.csv')
stockPricesClosing=sbiData['Adj Close'].to_list()

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
    return [eU,mu,sigmaSquare]

calLogReturns()
calEstMuSigma()
[eU,mu,sigmaSquare]=calEstMuSigma()

print("Estimated value of \u03BC (mean) = "+str(mu))
print("Estimated value of \u03C3 (standard deviation) = "+str(math.sqrt(sigmaSquare)))
print("The value of E(u) = "+str(eU))
print('\n')
S0=185.399994 #the stock price on 30th september
#------------------------------------------------------------------------------#

#-------------------------------------lab 8 work-------------------------------#

def generate_exp(λ):
    u=random.uniform(0,1)
    r=-math.log(u)/λ
    return r

def generate_norm(): #uses the Box Muller method to generate N(0,1)
    u1=random.uniform(0,1)
    u2=random.uniform(0,1)
    r=-2*math.log(u1)
    v=2*math.pi*u2
    z1=math.sqrt(r)*math.cos(v)
    z2=math.sqrt(r)*math.sin(v)
    if(u1<0.5):
        return z1
    return z2

#------------------------------------------------------------------------------#

def printInterval(start,end):
    return "["+str(start)+", "+str(end)+"]"

asian_list=[]
european_list=[]

K=1.1*S0 #strike price = 1.1S(0) as given in question
λ=0.2 #choose lambda to be 0.2 
N=300 #300 equal intervals
T=30 #30 days
dt=T/N 

#Run M=1000 simulations
for j in range (0,1000):
    S_list=[S0] #stores the values of S(ti), initialise with S(0)
    t_list=[0] #stores the time points, inititalise with 0
    
    for i in range(0,34): #we have used 34 and later used break to ensure that the value of 30 is included! 
        R=generate_exp(λ) # R here is the time gap
        Y=generate_norm() # Y ~ N(0,1)
        Z=mu+(math.sqrt(sigmaSquare)*generate_norm()) #Z ~ N(0,1)
        
        #Using Merton's Jump Diffusion Model
        Si=S_list[len(S_list)-1]
        t_list.append(t_list[i]+R)
        S=math.exp(math.log(Si)+eU*R+math.sqrt(R*sigmaSquare)*Y +Z)
        
        #Doing a linear interpolation
        dS=((S-Si)/R)*dt
        noTimePoints=R/dt
        for k in range(0,int(noTimePoints)):
            S_list.append(Si+(dS*(k-1)))
        
        if(len(t_list)>34):
            break
    if(len(S_list)>301):
        S_list=S_list[:301]
        
    asian_list.append(max(K-statistics.mean(S_list)-0,0))
    european_list.append(max(K-S_list[300],0))
    
#for question 1, calculating price, sampling variance, and 95% confidence interval
asian_price=statistics.mean(asian_list)
sampling_var=statistics.variance(asian_list)
cf95_start=asian_price-(1.96*sampling_var/math.sqrt(1000))
cf95_end=asian_price+(1.96*sampling_var/math.sqrt(1000))
interval=printInterval(cf95_start,cf95_end)
print("Part", "\t\t", "Option Price", "\t\t", "Sampling Variance", "\t", "95% Confidence Interval")
print("1-Without CV", "\t", asian_price, "\t", sampling_var, "\t", interval) #CV Represents control variates

#for question 2, using control variates = price of european option
european_mean=statistics.mean(european_list)
european_variance=statistics.variance(european_list)

#calculating value of optimal b
b=0
for i in range(0,len(asian_list)):
    b=b+(asian_list[i] - asian_price)*(european_list[i]-european_mean)/(1000*european_variance)

#making use of control variate
for i in range(0,len(asian_list)):
    asian_list[i]=asian_list[i]-b*(european_list[i]-european_mean)

#calculating price, sampling variance, and 95% confidence interval after using control variate
asian_price=statistics.mean(asian_list)
sampling_var=statistics.variance(asian_list)
cf95_start=asian_price-(1.96*sampling_var/math.sqrt(1000))
cf95_end=asian_price+(1.96*sampling_var/math.sqrt(1000))
interval=printInterval(cf95_start,cf95_end)
print("2-With CV", "\t", asian_price, "\t", sampling_var, "\t", interval) #CV Represents control variates

