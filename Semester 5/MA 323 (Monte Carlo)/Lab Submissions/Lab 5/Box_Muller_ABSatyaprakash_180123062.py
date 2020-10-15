#BOX MULLER METHOD 
import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np #pip install numpy
import random
import math
import statistics
import time

#each of this corresponds to a list where nxy_z is z values of N(x,y) distribution
n01_100=[] 
n01_10000=[]
n05_100=[]
n05_10000=[]
n55_100=[]
n55_10000=[]

def find_values_N01(): #this function uses the box-muller algorithm and generates 100 and 10000 values of N(0,1)
    for i in range(0,100):
        u1=random.uniform(0,1)
        u2=random.uniform(0,1)
        r=-2*math.log(u1)
        v=2*math.pi*u2
        z1=math.sqrt(r)*math.cos(v)
        z2=math.sqrt(r)*math.sin(v)
        if(i%2==0):
            n01_100.append(z1)
        else:
            n01_100.append(z2)
        
    for i in range(0,10000):
        u1=random.uniform(0,1)
        u2=random.uniform(0,1)
        r=-2*math.log(u1)
        v=2*math.pi*u2
        z1=math.sqrt(r)*math.cos(v)
        z2=math.sqrt(r)*math.sin(v)
        if(i%2==0):
            n01_10000.append(z1)
        else:
            n01_10000.append(z2)

def q1a_sample_meanvar(): #this function calculates and prints the sample mean and variance
    print('For 100 values')
    print('Sample mean=',statistics.mean(n01_100))
    print('Sample variance= {}\n'.format(statistics.variance(n01_100)))
    print('For 10000 values')
    print('Sample mean=',statistics.mean(n01_10000))
    print('Sample variance=',statistics.variance(n01_10000))

def q1b_plot_freqvsval(l): #this function prints the freq vs x histograms for N(0,1)
    l.sort()
    plt.title('Frequency vs sample values for N(0,1) for {} values'.format(len(l)))
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.hist(l,bins=50,rwidth=0.8)
    plt.show()

def q1c_find_n05_and_n55(): #this function finds the values of N(0,5) and N(5,5)
    for i in range(0,100):
        n05_100.append(n01_100[i]*math.sqrt(5))
        n55_100.append(n01_100[i]*math.sqrt(5)+5)
    for i in range(0,10000):
        n05_10000.append(n01_10000[i]*math.sqrt(5))
        n55_10000.append(n01_10000[i]*math.sqrt(5)+5)

def return_pdf_normal(x,neu,sigmasq,bw,lenl): #f(x)=(1/(sigma*sqrt(2*pi))*e^(-1/2*((x-neu)/sigma)^2))
    fx=[]
    for i in range(0,len(x)):
        power_term=-(((x[i]-neu)**2)/sigmasq)/2
        num=math.exp(power_term)
        den=math.sqrt(2*math.pi*sigmasq)
        fx.append(num*bw*lenl/den)
    return fx

def plotandcompare(l,typ): #this function plots the N(0,5) and N(5,5) and compares with the drawn histograms
    l.sort()
    distri=''
    _,bins,_=plt.hist(l,bins=50,rwidth=0.8,label='Observed')
    bw=bins[1]-bins[0]
    x=np.arange(bins[0]-0.5,bins[-1]+0.5,0.1)
    if(typ==0):
        distri='N(0,5)'
        y=return_pdf_normal(x,0,5,len(l),bw)
    else:
        distri='N(5,5)'
        y=return_pdf_normal(x,5,5,len(l),bw)
    plt.plot(x,y,label='Expected-'+distri)
    plt.title('Observed and Expected values for {} vs Sample values'.format(distri))
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

start=time.time() #start keeping a track of time

print('Box-Muller method')
#call all functions
find_values_N01()
q1a_sample_meanvar()
q1b_plot_freqvsval(n01_100)
q1b_plot_freqvsval(n01_10000)
q1c_find_n05_and_n55()
plotandcompare(n05_100,0)
plotandcompare(n05_10000,0)
plotandcompare(n55_100,5)
plotandcompare(n55_10000,5)

end=time.time() #end keeping track of time
print(f"Runtime of the program is {end - start}") #print the overall runtime
