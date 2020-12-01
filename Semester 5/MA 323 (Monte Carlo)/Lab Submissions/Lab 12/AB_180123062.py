import math
import matplotlib.pyplot as plt 

def gen_VanderCorput(N, base):
    VanderCorputseq=[]
    for i in range(N):
        num=i
        seqval=0
        p=-1
        while(num!=0):
            temp=num%base
            num=(int)(num/base)
            seqval=seqval+(temp*(base**p))
            p=p-1
        VanderCorputseq.append(seqval)
    return VanderCorputseq

def lcg(N):
    #seed for LCG
    x0=111
    a=1229
    b=11
    m=20489
    
    u_arr=[]
    for i in range(N):
        x1=(a*x0+b)%m
        u1=x1/m
        u_arr.append(u1)
        x0=x1
    return u_arr

#Question 1 - part A ---------------------------------------------------------------------
f25=gen_VanderCorput(25,2) #the first 25 values of the Van der Corput sequence
print(f25) #printing the values

#Question 1 - part B ---------------------------------------------------------------------
f1000=gen_VanderCorput(1000,2)
xi=f1000[0:999]
xi1=f1000[1:1000]
plt.scatter(xi,xi1) #plotting the (x(i),x(i+1)) points on a graph
plt.title('(x(i),x(i+1)) for 1000 values of Van der Corput sequence')
plt.xlabel('x(i) values')
plt.ylabel('x(i+1) values')
plt.show()

#Question 1 - part C ---------------------------------------------------------------------
#Taking 100 and 100000 values of the Van der Corput sequence
f100=gen_VanderCorput(100,2)
f100000=gen_VanderCorput(100000,2)

print('LCG used: x(i+1)=(1229*x(i)+11)%2048 with x(0)=111')
#Taking 100 and 100000 values from the LCG
lcg100=lcg(100)
lcg100000=lcg(100000)

fig = plt.figure(figsize= (15, 10))
plot_1 = fig.add_subplot(221)
plot_1.hist(f100,bins=25,rwidth=0.75)
plot_1.set_title('100 values of Van der Corput sequence')
plot_1.set_xlabel('values')
plot_1.set_ylabel('frequency')

plot_2 = fig.add_subplot(222)
plot_2.hist(lcg100,bins=25,rwidth=0.75)
plot_2.set_title('100 values of LCG')
plot_2.set_xlabel('values')
plot_2.set_ylabel('frequency')

plot_3 = fig.add_subplot(223)
plot_3.hist(f100000,bins=25,rwidth=0.75)
plot_3.set_title('100000 values of Van der Corput sequence')
plot_3.set_xlabel('values')
plot_3.set_ylabel('frequency')

plot_4 = fig.add_subplot(224)
plot_4.hist(lcg100000,bins=25,rwidth=0.75)
plot_4.set_title('100000 values of LCG')
plot_4.set_xlabel('values')
plot_4.set_ylabel('frequency')

plt.show()


#Question 2 --------------------------------------------------------------------------------
#Genrating the Halton sequence xi= (φ2(i), φ3(i)) for 100 and 100000 values and plotting

#Here φb_v means were generating a sequence with base 'b' and 'v' number of values  
φ2_100 = gen_VanderCorput(100,2)
φ2_100000 = gen_VanderCorput(100000,2)
φ3_100 = gen_VanderCorput(100,3)
φ3_100000 = gen_VanderCorput(100000,3)

plt.scatter(φ2_100, φ3_100) #plotting the (φ2(i), φ3(i)) points on a graph for 100 values
plt.title('(φ2(i), φ3(i)) for 100 values of Halton sequence')
plt.xlabel('φ2(i) values')
plt.ylabel('φ3(i) values')
plt.show()

plt.scatter(φ2_100000, φ3_100000) #plotting the (φ2(i), φ3(i)) points on a graph for 100000 values
plt.title('(φ2(i), φ3(i)) for 100000 values of Halton sequence')
plt.xlabel('φ2(i) values')
plt.ylabel('φ3(i) values')
plt.show()

