# Question 01, Lab 10
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


def stockSimulation():
    r = 0.05
    sigma = 0.2
    T = 180
    SrnArray, SArray = [], []
    for _ in range(10):
        Srn, S = getStockPrices('A', T, r, sigma)
        SrnArray.append(Srn)
        SArray.append(S)

    for Srn in SrnArray:
        plt.plot(Srn)
    plt.xlabel('Time Steps')
    plt.ylabel('Stock price')
    plt.title('10 stock simulation paths in Risk Neutral World')
    plt.show()

    for S in SArray:
        plt.plot(S)
    plt.xlabel('Time Steps')
    plt.ylabel('Stock price')
    plt.title('10 stock simulation paths in Real World')
    plt.show()


def stockSimulationCompare():
    r = 0.05
    sigma = 0.2
    T = 180
    Srn, S = getStockPrices('A', T, r, sigma)
    plt.figure()
    plt.plot(S)
    plt.plot(Srn)
    plt.legend(['real', 'risk neutral'])
    plt.xlabel('Time Steps')
    plt.ylabel('Stock price')
    plt.title('Comparison of stock price in real and risk neutral world')
    plt.show()


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

        print(option + ' Option price for K = ' + str(K) +
              ' is ' + str(np.round_(np.mean(a1), 5)))
        plt.plot(m,a1)
        plt.xlabel('# of simulations')
        plt.ylabel('Option price')
        plt.title(
            option + ' Option price sensitivity analysis with K = {}'.format(K))
        plt.show()

    T, r, sigma = 180, 0.05, 0.2
    KArr = np.arange(50, 150, 5)
    a1, a2 = [], []
    for K in KArr:
        without_var_red, with_var_red = optionPrice(
            100, K, option, T, r, sigma)
        a1.append(without_var_red)
        a2.append(with_var_red)
    plt.plot(KArr, a1, color='orange')
    plt.xlabel('Strike Price')
    plt.ylabel('Option price')
    plt.title(option + ' Option price sensitivity analysis')
    plt.show()

    K, T, r = 105, 180, 0.05
    sigmaArr = np.arange(0.02, 1.02, 0.02)
    a1, a2 = [], []
    for sigma in sigmaArr:
        without_var_red, with_var_red = optionPrice(
            100, K, option, T, r, sigma)
        a1.append(without_var_red)
        a2.append(with_var_red)
    plt.plot(sigmaArr, a1, color='lime')
    plt.xlabel('Volatility')
    plt.ylabel('Option price')
    plt.title(option + ' Option price sensitivity analysis')
    plt.show()

    K, T, sigma = 105, 180, 0.2
    rArr = np.arange(0.05, 1.05, 0.05)
    a1, a2 = [], []
    for r in rArr:
        without_var_red, with_var_red = optionPrice(
            100, K, option, T, r, sigma)
        a1.append(without_var_red)
        a2.append(with_var_red)
    plt.plot(rArr, a1, color='red')
    plt.xlabel('Risk-free rate')
    plt.ylabel('Option price')
    plt.title(option + ' Option price sensitivity analysis')
    plt.show()

    K, r, sigma = 105, 0.05, 0.2
    TArr = np.arange(30, 365, 1)
    a1, a2 = [], []
    for T in TArr:
        without_var_red, with_var_red = optionPrice(
            100, K, option, T, r, sigma)
        a1.append(without_var_red)
        a2.append(with_var_red)
    plt.plot(TArr, a1, color='blue')
    plt.xlabel('Maturity')
    plt.ylabel('Option price')
    plt.title(option + ' Option price sensitivity analysis')
    plt.show()


# program body
mu = 0.1
delT = 1.0/365
S0 = 100  # asset price at t = 0 is S(0) = 100

# 10 stock simulations in real and risk neutral worlds
stockSimulation()
stockSimulationCompare()
optionPriceSensitivityAnalysis('Call')
optionPriceSensitivityAnalysis('Put')