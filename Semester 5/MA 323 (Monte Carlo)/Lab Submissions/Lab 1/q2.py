import matplotlib.pyplot as plt 
import random
import numpy

def genetate_uis(m,x):
    u_values=[]
    v_values=[]
    
    #taking a=1597
    temp=x
    for y in range(0,m+1):
        a=1597 
        b=51749
        u_values.append(temp/m)
        temp1=temp
        temp=(temp1*a+b)%m
        if(temp==x):
            break
    u_values.sort()
    no_bins = numpy.linspace(0, 1, 20)
    plt.hist(u_values, no_bins, alpha=0.5, rwidth=0.8, label='a=1597')
    
    #taking a=51749
    temp=x
    for y in range(0,m+1):
        a=51749 
        b=1
        v_values.append(temp/m)
        temp1=temp
        temp=(temp1*a+b)%m
        if(temp==x):
            break
    v_values.sort()
    plt.hist(v_values, no_bins, rwidth=0.8, label='a=51749')
    plt.legend(loc='upper right')
    plt.title('x0 ='+str(x))
    plt.show()

m=244944
for i in range (0,5):
    x = random.randint(1,m)
    genetate_uis(m,x)

