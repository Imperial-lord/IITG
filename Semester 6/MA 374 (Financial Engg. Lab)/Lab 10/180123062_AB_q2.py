# Question 02, Lab 10
# AB Satyaprakash, 180123062

# imports
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# functions


def getStockPrices(part, T, r, sigma):
    S1, S2 = np.ndarray(T+1), np.ndarray(T+1)
    S1[0], S2[0] = 100.0, 100.0
    for i in range(1, T+1):
        W = sqrt(delT)*np.random.randn()
        S1[i] = S1[i-1]*np.exp(sigma*W + (r-0.5*(sigma**2))*delT)
        if part == 'A':
            # return risk neutral and real world stock prices
            S2[i] = S2[i-1]*np.exp(sigma*(W) + (mu-0.5*(sigma**2))*delT)
        else:
            # return variance reduction stock prices
            S2[i] = S2[i-1]*np.exp(sigma*(-W) + (r-0.5*(sigma**2))*delT)
    return S1[1:], S2[1:]


def optionPrice(m, K, option, T, r, sigma):
    payoffSum1, payoffSum2 = 0, 0
    for i in range(m):
        Splus, Sminus = getStockPrices('B', T, r, sigma)
        Yplus = np.mean(Splus)
        Yminus = np.mean(Sminus)
        if option == 'Call':
            payoff1 = max(0, Yplus-K)
            payoff2 = 0.5*(max(0, Yplus-K) + max(0, Yminus-K))
        else:
            payoff1 = max(0, K-Yplus)
            payoff2 = 0.5*(max(0, K-Yplus) + max(0, K-Yminus))
        payoffSum1 = payoffSum1 + payoff1
        payoffSum2 = payoffSum2 + payoff2
    return np.exp(-r*delT*T)*(payoffSum1/m), np.exp(-r*delT*T)*(payoffSum2/m)


def optionPriceSensitivityAnalysis(option):
    T, r, sigma = 180, 0.05, 0.2
    for K in [90, 105, 110]:
        a1, a2, m = [], [], []
        for i in range(500, 3000, 500):
            without_var_red, with_var_red = optionPrice(
                i, K, option, T, r, sigma)
            a1.append(without_var_red)
            a2.append(with_var_red)
            m.append(i)

        print('Variance of '+option + ' option price without variance reduction for K = ' +
              str(K) + ' is ' + str(np.round(np.var(a1), 5)))
        print('Variance of '+option + ' option price with variance reduction for K = ' +
              str(K) + ' is ' + str(np.round(np.var(a2), 5)))
        plt.plot(a1, label='Without Variance Reduction')
        plt.plot(a2, label='With Variance Reduction')
        plt.xlabel('Number of simulations')
        plt.ylabel('Option price')
        plt.title(
            option + ' option price sensitivity analysis with K = {}'.format(K))
        plt.legend()
        plt.show()
        print('---------------------------------------------------------------------------')


# program body
mu = 0.1
delT = 1.0/365
S0 = 100  # asset price at t = 0 is S(0) = 100

optionPriceSensitivityAnalysis('Call')
optionPriceSensitivityAnalysis('Put')
