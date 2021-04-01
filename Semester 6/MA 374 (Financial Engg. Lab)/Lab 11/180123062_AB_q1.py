# AB Satyaprakash 180123062
# Question 01, Lab 10

# imports
import numpy as np
from numpy import exp, log
from matplotlib import pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 10, 5

# functions


def vasicek_yield(beta, mu, sigma, r, time_units):
    y = np.zeros(time_units+1)
    y[0] = r
    a, b = beta, beta*mu
    for T in range(1, time_units+1):
        B = (1-exp(-a*T))/a
        A = (B-T)*(a*b-0.5*sigma**2)/(a**2)-((a*B)**2)/(4*a)
        p = exp(A-B*r)
        y[T] = -1*log(p)/T
    return y


def yield_vs_time_plot(model, parameters, time_units):
    plt.figure()
    for p in parameters:
        beta, mu, sigma, r = p
        y = vasicek_yield(beta, mu, sigma, r, time_units)
        plt.plot(y, label=str(p))
    plt.title(model+' Model with given parameter sets')
    plt.xlabel('Time')
    plt.ylabel('Yield')
    plt.legend()
    plt.show()


def yield_vs_maturity_plot(model, parameters, time_units):
    for p in parameters:
        plt.figure()
        for r in np.arange(0.1, 1.1, 0.1):
            r = np.round_(r, 1)
            beta, mu, sigma, _ = p
            y = vasicek_yield(beta, mu, sigma, r, time_units)
            plt.plot(y, label='r = '+str(r))
        plt.title(model + " Model with beta, mu, sigma = " +
                  str(p[:-1])+" using 10 different values of r")
        plt.xlabel('Time')
        plt.ylabel('Yield')
        plt.legend()
        plt.show()


# program body
p1 = [5.9, 0.2, 0.3, 0.1]
p2 = [3.9, 0.1, 0.3, 0.2]
p3 = [0.1, 0.4, 0.11, 0.1]
yield_vs_time_plot('Vasicek', [p1, p2, p3], 10)
yield_vs_maturity_plot('Vasicek', [p1, p2, p3], 500)
