import matplotlib.pyplot as plt #pip install matplotlib
import math
import numpy as np #pip install numpy
import statistics
theta=0.5 # mean of the function

u=[] #to fill with 100000 values from linear congruence generator
def gen_lincong_foru():
    #X(i+1)=X(i)A mod M and U(i+1)=X(i+1)/M -> Linear Congruence Generator
    x=23 # x0 value
    m=4096
    a=17
    for i in range(0,100000):
        u.append(x/m)
        t=(a*x+1)%m #b=1
        x=t

x=[] #to get x from the inverse of exponential distribution
def gen_xfromu():
    #X=-(theta)log(1-U) -> Inverse of exponential distribution
    for i in range(0,100000):
        t=(-theta)*(math.log(1-u[i]))
        x.append(t)

fx=[]
def gen_fx_fromx():
    #F(x)=1-e^(-x/theta)
    for i in range(0,100000):
        t=1-math.exp(-x[i]/theta)
        fx.append(t)
        
def plot_xvsu(l):
    #take 0.05 interval length and plot X vs [0,5]
    x_cor=[] #will have the midpoint of that interval 
    y_cor=[] #will have the freq of x belonging to that interval
    ini=0
    freq=0
    while(ini<=5):
        x_cor.append(ini+0.05/2)
        for i in range(0,len(l)):
            if(l[i]>=ini and l[i]<=ini+0.05):
                freq=freq+1
        y_cor.append(freq)
        ini+=0.05 
    s_mean='Sample mean= '+str(np.mean(l)) #sample mean
    s_var='Sample variance= '+str(statistics.variance(l)) #sample var
    plt.plot(x_cor,y_cor)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(s_mean+'\n'+s_var+'\nDistribution function for '+str(len(l))+' generated values of X')
    plt.show()

def plot_xvsu_fr(l):
    #take 0.05 interval length and plot X vs [0,5]
    x_cor=[] #will have the midpoint of that interval 
    y_cor=[] #will have the freq of x belonging to that interval
    ini=0
    while(ini<=5):
        freq=0
        x_cor.append(ini+0.05/2)
        for i in range(0,len(l)):
            if(l[i]>=ini and l[i]<=ini+0.05):
                freq=freq+1
        y_cor.append(freq)
        ini+=0.05 
    plt.plot(x_cor,y_cor)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Frequency vs Interval for '+str(len(l))+' generated values of X')
    plt.show()


def plot_fxvsx(no_values):
    x_cor=[] #will have the value of x generated 
    y_cor=[] #will have the corresponding value of fx
    for i in range(0,no_values):
        x_cor.append(x[i])
        y_cor.append(fx[i])
    plt.scatter(x_cor,y_cor)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Distribution function f(x) '+str(no_values)+' generated values of X')
    plt.show()


print('Actual Mean= '+str(theta))
print('Actual Variance= '+str(theta*theta))
gen_lincong_foru()
gen_xfromu()
gen_fx_fromx()
plot_xvsu(x[0:100])
plot_xvsu_fr(x[0:100])
plot_fxvsx(100)
plot_xvsu(x[0:1000])
plot_xvsu_fr(x[0:1000])
plot_fxvsx(1000)
plot_xvsu(x[0:10000])
plot_xvsu_fr(x[0:10000])
plot_fxvsx(10000)
plot_xvsu(x[0:100000])
plot_xvsu_fr(x[0:100000])
plot_fxvsx(100000)