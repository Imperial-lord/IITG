import matplotlib.pyplot as plt
import math
import numpy as np 
import statistics
import random

def find_cri_x(alpha1, alpha2):
    x_star=(alpha1-1)/(alpha1+alpha2-2)
    return x_star

def find_fx(alpha1, alpha2,x):
    beta=(math.gamma(alpha1)*math.gamma(alpha2))/math.gamma(alpha1+alpha2)
    fx=(pow(x,alpha1-1)*pow(1-x,alpha2-1))/beta
    return fx

def acc_rej_for_betadist(alpha1, alpha2):
    Ran_list=[]
    c=find_fx(alpha1,alpha2,find_cri_x(alpha1,alpha2)) # the maxima pt value of PDF of Beta Dist.
    for i in range(0,100000): #generating 100000 values
        while(1):
            u1=random.uniform(0,1) #u1~U[0,1]
            u2=random.uniform(0,1) #u2~U[0,1]
            fu1=find_fx(alpha1,alpha2,u1) #f(u1) for u1~U[0,1]
            if(c*u2<=fu1):
                Ran_list.append(u1)
                break
    hist_for_ranlist(Ran_list)
    plt.show()
    
def hist_for_ranlist(l):
    l.sort()
    plt.title('RVs generated from Beta distribution function')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    counts,bins,_=plt.hist(l,bins=50,rwidth=0.2)
    bins=(bins[:-1]+bins[1:])/2
    plt.plot(bins,counts)
    
    
alpha1=[1,2,3,4,5]
alpha2=[5,4,3,2,1]

for i in range(0,5):
    acc_rej_for_betadist(alpha1[i],alpha2[i])
