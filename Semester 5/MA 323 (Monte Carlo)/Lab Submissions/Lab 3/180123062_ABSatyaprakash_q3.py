import matplotlib.pyplot as plt #pip3 install matplotlib
import numpy as np #pip3 install numpy
import random

pmf_arr=[0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]

def gen_acc_rej(num,c): # A function for generating the random values as per the accept reject mechanism
    X_ran=[]
    itr_for_x=[]
    for i in range(0,num):
        count=1
        while(1):
            u=random.uniform(0,1) # represents U ~ U[0,1]
            x=1+int(random.uniform(0,1)*10) #represents the X generated from g
            fx=pmf_arr[x-1]*10 # since we are taking f(x)/g(x) and g(x)=0.1
            if(u<=(fx/c)):
                itr_for_x.append(count)
                X_ran.append(x)
                break
            else:
                count=count+1
    return X_ran, itr_for_x

num=100000 # the number of variables generated
c_values=[2,3] # this represents the values of c that were used. (minimum value was 1.2)

for i in range(0,2):
    X, counts_iter= gen_acc_rej(num,c_values[i])
    
    print('For the values of n='+str(num)+' and c='+str(c_values[i])+' \nWe have the mean='+str(np.mean(counts_iter)))
    #plotting the probability versus discrete values
    # getting the frequency array corresponding to each discrete value
    freq, _ = np.histogram(X)

    # scaling frequency array so as to compare with the discrete probability distribution
    freq = freq/num
    x_axis = np.arange(1,11,1)
    plt.plot(x_axis, pmf_arr, label = 'Actual probability')
    plt.plot(x_axis, freq, label = 'Scaled frequency')
    
    plt.title('Generating discrete variables with \nn = {} and c = {}'.format(num,c_values[i]))
    plt.xlabel('Permissible Discrete Values')
    plt.ylabel('Probability')
    plt.legend(frameon = 0)

    plt.scatter(x_axis, freq, color = 'orange')
    # plt.savefig('q3_{}.png'.format(c))
    plt.show()
