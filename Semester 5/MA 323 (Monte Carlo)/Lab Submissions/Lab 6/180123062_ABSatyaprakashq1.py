import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal
import matplotlib
import time
import random
import math

Z1=[]
Z2=[]

#------------generate 1000 values for Z1 and Z2 to get ~N(0,1)------------------------#
def Marsaglia_and_Bray(): 
    count_acc=0
    while(1):
        u1=random.uniform(0,1)
        u2=random.uniform(0,1)
        u1=2*u1-1
        u2=2*u2-1
        x=u1**2+u2**2
        if(x>1):
            continue
        else:
            count_acc=count_acc+1
            y=math.sqrt(-2*math.log(x)/x)
            z1=u1*y
            z2=u2*y
            Z1.append(z1)
            Z2.append(z2)
            if(count_acc==1000):
                break
#--------------------------------------------------------------------------------------#


#-------------------find the matrix A from sigma1, sigma2 and rho----------------------#
def return_A(sigma1, sigma2, rho):
    A=[]
    A.append(sigma1) #A11
    A.append(0) #A12
    A.append(rho*sigma2) #A21
    A.append(sigma2*(math.sqrt(1-rho**2))) #A22
    return A
    
#--------------------------------------------------------------------------------------#

#--------------------------- PDF for multivariate normal-------------------------------#
def return_multivariate_normal_pdf(x,det,inv,mean):
    d=2
    diff=x-mean
    denom=(((2*math.pi)**(1/2))*(det**(1/2)))
    power_quan=-0.5*np.matmul(diff.T,np.matmul(inv,diff))
    num=math.exp(power_quan)
    res=num/denom
    return res
#--------------------------------------------------------------------------------------#

#--------------------------- PDF for univariate normal-------------------------------#
def return_univariate_normal_pdf(x,mean,var):
    power_term = -(np.square(x-mean))/(2*var)
    num=np.exp(power_term)
    denom = np.sqrt(2*np.pi*var)
    res=num/denom
    return res
#--------------------------------------------------------------------------------------#

a_values=[-0.5,0,0.5,1] # allowed values of a as per q1.1

# -----------------------values obtained from the Covariance Matrix E-----------------#
MU=[5,8]
SIGMA1=1
SIGMA2=2
#-------------------------------------------------------------------------------------#

Marsaglia_and_Bray() # calling the function to generate 1000 N(0,1) values and store in Z1 and Z2

for i in range (len(a_values)):
    a=a_values[i]
    RHO=2*a/(SIGMA1*SIGMA2) #2a=rho*sigma1*sigma2
    A11,A12,A21,A22=return_A(SIGMA1,SIGMA2,RHO)
    COV_matrix=np.array([[1,2*a],[2*a,4]]) #making this an np array for later use (of transpose, inverse etc..)
    
    X1=[]
    X2=[]
    #--------------q1.1 done. In X1[], X2[] we have the generated values of X----------#
    for j in range (len(Z1)):
        X1.append(MU[0]+A11*Z1[j])
    for j in range (len(Z2)):
        X2.append(MU[1]+A21*Z1[j]+A22*Z2[j])
    #----------------------------------------------------------------------------------#   
    
    #drawing the histogram corresponding to the different values of a. 
    fig = plt.figure(figsize= (35, 50), frameon= True)
    
    hist, xedges, yedges = np.histogram2d(X1, X2, bins = (15, 15))
    xpos, ypos = np.meshgrid(xedges[:-1]+0.05, yedges[:-1]+0.05 , indexing = 'ij')
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    dx=dy=0.4
    dz = hist.ravel()
    
    #making a 4*1 plot and adding the first subplot at position 1 ---------q1.2 done---------#
    plot_1 = fig.add_subplot(321, projection='3d')
    plot_1.set_title('3D Histogram for Simulated X')
    plot_1.set_xlabel(r'$X_1$')
    plot_1.set_ylabel(r'$X_2$')
    plot_1.set_zlabel('Frequency')
    plot_1.bar3d(xpos, ypos, zpos, dx, dy, dz,  shade = True, zsort = 'max', cmap = 'inferno')
    
    
    #plotting the actual density for the above cases
    x1_range=np.linspace(2,10,200) #x1 has a range from 2 to 10 (plot1)
    x2_range=np.linspace(2,20,200) #x2 has a range from 2 to 20 (plot1)
    
    AX1, AX2 = np.meshgrid(x1_range, x2_range)
    AX = np.empty(AX1.shape + (2,))
    AX[:, :, 0] = AX1
    AX[:, :, 1] = AX2
    
    Z=[]
    detereminant_E=np.linalg.det(COV_matrix)
    if(detereminant_E==0):
        print('The determinant for COV matrix is 0 and PDF does not exist in case of a=1.0')
    else:
        inverse_E=np.linalg.inv(COV_matrix)
        for r in range(200):
            M=[]
            for s in range(200):
                x=np.array([AX[r,s,0],AX[r,s,1]])
                result=return_multivariate_normal_pdf(x,detereminant_E,inverse_E,np.array(MU))
                M.append(result)
            Z.append(M)
        Z=np.array(Z)
        Z=Z*200*2*(xedges[1]-xedges[0])*(yedges[1]-yedges[0])
        plot_2= fig.add_subplot(322, projection ='3d')
        plot_2.plot_surface(AX1, AX2, Z, cmap ='inferno', label = 'Actual')
        plot_2.set_title('Actual Density surface')
        plot_2.set_xlabel(r'$X_1$')
        plot_2.set_ylabel(r'$X_2$')
        plot_2.set_zlabel('PDF')
        
        #plotting the actual and generated densities in a common graph
        plot_3= fig.add_subplot(323, projection='3d')
        plot_3.bar3d(xpos, ypos, zpos, dx, dy, dz,  shade = True, zsort = 'max', cmap = 'inferno', alpha=0.3)
        plot_3.plot_surface(AX1, AX2, Z, cmap ='inferno', alpha=0.7)
        plot_3.set_title('Simulated histogram for X vs Actual surface')
        plot_3.set_xlabel(r'$X_1$')
        plot_3.set_ylabel(r'$X_2$')
        plot_3.set_zlabel('Frequency / PDF')
    
#     plotting for the marginal 1 dimensional cases!
    figpos1=325
    figpos2=326
    if(a==1):
        figpos1=323
        figpos2=324
    
    # plotting for X1-------------------------------------------------------------------------------
    plot_4 = fig.add_subplot(figpos1)
    counts, bins, _=plot_4.hist(X1, bins = 20, label = 'Simulated',rwidth=0.9)
    xaxis= np.arange(bins[0]-0.5, bins[-1]+0.5, 0.2)
    yaxis= return_univariate_normal_pdf(xaxis, MU[0], SIGMA1**2) * (bins[1] - bins[0]) * len(X1) 
    plot_4.plot(xaxis, yaxis, label='Actual')
    plot_4.set_title('X1 marginal distribution with \u03BC = {} and {} = {}'.format(round(np.mean(X1),4), r"$\sigma^{2}$", round(np.std(X1)**2,4)))
    plot_4.set_xlabel('Values')
    plot_4.set_ylabel('Frequency')
    plot_4.legend()

    # plotting for X2-------------------------------------------------------------------------------
    plot_5 = fig.add_subplot(figpos2)
    counts, bins, _ = plot_5.hist(X2, bins = 20, label = 'Simulated',rwidth=0.9)
    xaxis = np.arange(bins[0]-0.5, bins[-1]+0.5, 0.2)
    yaxis = return_univariate_normal_pdf(xaxis, MU[1], SIGMA2**2) * (bins[1] - bins[0]) * len(X2) 
    plot_5.plot(xaxis, yaxis, label = 'Actual')
    plot_5.set_title('X2 marginal distribution with \u03BC = {} and {} = {}'.format(round(np.mean(X2),4), r"$\sigma^{2}$", round(np.std(X2)**2),4))
    plot_5.set_xlabel('Values')
    plot_5.set_ylabel('Frequency')
    plot_5.legend()
        
        

    mu_array='['+str(np.mean(X1))+','+str(np.mean(X2))+']'
    print("Plots for a = {}".format(a)) 
    plt.show()
    #we have used a special character \u03BC for showing the greek alpha bet mu
