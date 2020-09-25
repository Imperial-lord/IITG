import matplotlib.pyplot as plt #pip3 install matplotlib
import math
import numpy as np #pip3 install numpy
import random
import statistics


u=[] #to fill with 100 values from linear congruence generator
def gen_lincong_foru():
    #X(i+1)=X(i)A mod M and U(i+1)=X(i+1)/M -> Linear Congruence Generator
    x=23 # x0 value
    m=4096
    a=17
    for i in range(0,100):
        u.append(x/m)
        t=(a*x+1)%m #b=1
        x=t
        
c=[]
def fill_c_withvalues():
# {1,3,5,...,9999} -> This is the set to generate discrete uniform variables on.
    ini=1
    c.append(1)
    for i in range (1,5000):
        ini=ini+2;
        c.append(ini)
    
common_prob=1/5000
q=[]
def gen_q():
    q.append(0)
    for i in range(1,5000):
        q.append(q[i-1]+common_prob)
        

def find_final_ans(num):
    final_ans=[] #will print as per the number of values of u to be taken = num in our case
    for i in range(0,num):
        for j in range (1,5000):
            if(q[j-1]<u[i] and q[j]>=u[i]):
                final_ans.append(c[j])
    print('This is for the case of '+str(num)+' values of U \n')
    print(final_ans)
    print('\n')


gen_lincong_foru()
fill_c_withvalues()
gen_q()
find_final_ans(10)
find_final_ans(100)
