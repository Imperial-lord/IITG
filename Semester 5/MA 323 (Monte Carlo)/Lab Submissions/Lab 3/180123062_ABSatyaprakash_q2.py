import matplotlib.pyplot as plt #pip3 install matplotlib
import math
import numpy as np #pip3 install numpy
import random
import statistics
import random


def get_iter_forx(num,c): # we are taking num random values at a time
    X_ran=[]
    itr_for_x=[]
    for i in range(0,num):
        count=1
        while(1):
            u=random.uniform(0,1) # represents U ~ U[0,1]
            x=random.uniform(0,1) #represents the X generated from g, which is U[0,1]
            fx=20*x*(pow(1-x,3)) # f(x) is calculated by 20*x*(1-x)^3
            if(u<=(fx/(c))):
                itr_for_x.append(count)
                X_ran.append(x)
                break
            else:
                count=count+1
        
    print('The mean value of count of number of iterations for '+str(num)+' random values is '+str(np.mean(itr_for_x)))
    (y,x,pat)=plt.hist(X_ran,density=True,bins=20)
    err=0.0
    for i in range(0,len(y)):
        err+=((20*x[i]*(pow(1-x[i],3)))-y[i])**2
    err=err/len(y)
    print('The error value is',err)


c=2.109375
print('The value of c used is '+str(c))
get_iter_forx(100,c)
get_iter_forx(1000,c)
get_iter_forx(10000,c)
get_iter_forx(100000,c)
c=[3.109375, 4.109375]
for i in range(0,2):
    print('\n')
    print('The value of c used is '+str(c[i]))
    get_iter_forx(100,c[i])
    get_iter_forx(1000,c[i])
    get_iter_forx(10000,c[i])
    get_iter_forx(100000,c[i])
plt.close()
