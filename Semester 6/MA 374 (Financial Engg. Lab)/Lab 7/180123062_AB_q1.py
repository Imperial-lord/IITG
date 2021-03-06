# Question 01, Lab 07
# AB Satyaprakash - 180123062

# imports
from math import sqrt, log, exp
from scipy.stats import norm

# functions


def calEurCallPutPrices(T, K, S, r, σ, t):
    if(T == t):
        putp = max(K-S, 0)
        callp = max(S-K, 0)
        return [callp, putp]

    d1 = (log(S/K)+(r+(σ**2/2))*(T-t))/(σ*sqrt(T-t))
    d2 = d1-σ*sqrt(T-t)

    putp = K*exp(-r*(T-t))*norm.cdf(-d2) - S*norm.cdf(-d1)
    callp = S*norm.cdf(d1)-K*norm.cdf(d2)*exp(-r*(T-t))
    return [callp, putp]
