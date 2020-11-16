import pandas as pd;
import math;
import random;
import statistics;
import matplotlib.pyplot as plt;

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
    return [mu,sigmaSquare]

def find_values_N01(): #this function uses the box-muller algorithm and generates 1000 values of N(0,1) for Zj+1
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

def find_values_Yj(mu,sigmaSquare):#this function makes use of log normal distribution and then finds log Yj+1 again!
    st_normal=find_values_N01()
    log_normal=[]
    for i in range(0,1000):
        val=mu+math.sqrt(sigmaSquare)*st_normal[i]
        log_normal.append(math.exp(val))
    return log_normal
    

def find_values_R(λ): #this function uses U(0,1) to form Rj+1=-log(U)/λ
    exp_1000=[]
    for i in range(0,1000):
        u1=random.uniform(0,1)
        exp_1000.append(-math.log(u1)/λ)
    return exp_1000
            
calLogReturns()
[mu,sigmaSquare]=calEstMuSigma()

print("Estimated value of \u03BC (mean) = "+str(mu))
print("Estimated value of \u03C3 (standard deviation) = "+str(math.sqrt(sigmaSquare)))
print('\n')

S0=185.40 #S(0) has been taken for 30th of September.
λ =[0.01, 0.05, 0.1, 0.2] #The 4 different values of λ given in question

for i in range(0,4): # calculate expected Stock prices for 4 different values for λ
    Z=find_values_N01()
    R=find_values_R(λ[i])
    Y=find_values_Yj(mu, sigmaSquare)
    
    X0=math.log(S0)
    St=[S0]
    x_axis=[0]
    tau=0
    for j in range (0,1000):
        X1=X0+((mu-(sigmaSquare/2))*R[j])+(math.sqrt(sigmaSquare*R[j])*Z[j])+(math.log(Y[j]))
        St.append(math.exp(X1))
        X0=X1
        tau+=R[j]
        x_axis.append(tau)
        if(tau>1000):
            break
    
    plt.plot(x_axis,St,label='λ= '+str(λ[i]))
    plt.title('S(t) vs time points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend(loc='upper right')
    plt.show()
