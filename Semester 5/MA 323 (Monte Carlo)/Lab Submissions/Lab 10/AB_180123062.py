import math;
import random;
import statistics;

def genYis(M): #generate all the Yis from U(0,1)
    Y=[]
    for i in range (0,M):
        u=random.uniform(0,1)
        k=math.exp(math.sqrt(u))
        Y.append(k)
    return Y

def genYi_hats(M): #generate all the Y^is from U(0,1)
    Y1=[]
    for i in range (0,M):
        u=random.uniform(0,1)
        k=math.exp(math.sqrt(u))+math.exp(math.sqrt(1-u))
        k/=2
        Y1.append(k)
    return Y1

def getIandIhats(Y): #generate the I and I^s from Yis and Y^is
    return statistics.mean(Y)

def get95ConfInt(mu,sigma,M): #return the left and right limit of 95% confidence interval
    left=mu-(1.96*sigma/math.sqrt(M))
    right=mu+(1.96*sigma/math.sqrt(M))
    
    return [left,right]

print("Value of M\tIm\tI^m\t95% Conf_Int for Im\t95% conf_Int for I^m\tRatio")
    
m=[100,1000,10000,100000] #we have been asked to do this for 4 values of M
for i in range (0,4):
    M=m[i]
    
    #calling respective functions to populate variables
    Y=genYis(M)
    Y1=genYi_hats(M)
    I=getIandIhats(Y)
    I1=getIandIhats(Y1)
    
    
    Ysd=statistics.stdev(Y)
    Y1sd=statistics.stdev(Y1)
    
    
    [I95l,I95r]=get95ConfInt(I,Ysd,M)
    [I195l,I195r]=get95ConfInt(I1,Y1sd,M)
    ratio=(I95r-I95l)/(I195r-I195l)
    
    
    # making the confidence interval to the form, [left, right]
    I95="["+str(round(I95l,4))+", "+str(round(I95r,4))+"]"
    I195="["+str(round(I195l,4))+", "+str(round(I195r,4))+"]"
    
    
    #printing rows of the table for specific M values
    print(M,'\t     ',round(I,4),'',round(I1,4),'\t',I95,'\t',I195,'\t',round(ratio,4))
    
