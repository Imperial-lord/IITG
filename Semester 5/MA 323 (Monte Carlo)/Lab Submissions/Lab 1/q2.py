import matplotlib.pyplot as plt 
import random

def genetate_uis(a,b,m,x):
    u_values=[]
    temp=x
    for y in range(0,m+1):
        u_values.append(temp/m)
        temp1=temp
        temp=(temp1*a+b)%m
        if(temp==x):
            break
    u_values.sort()
    no_bins=int(1/0.05)
    plt.hist(u_values, bins=no_bins, rwidth=0.8)
    plt.show()

m=244944
a=1597 
b=51749
for i in range (0,5):
    x = random.randint(0,m)
    print(x)
    genetate_uis(a,b,m,x)

