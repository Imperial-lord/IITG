# Question 3 Algorithm 2 (efficient) Lab Assignment 03
# @AB Satyaprakash, 180123062

# imports
from math import exp, sqrt
import numpy as np
import time

# Initialising a dictionary -- C++ equivalent to map<>
Map = {}
# functions ---------------------------------------------------------------------------


def recursion(n, K, S, T, r, sig, M, u, d, p, q, dt, upCnt):
    if (n, upCnt) in Map:
        return Map[(n, upCnt)]

    if n == M:
        Map[(n, upCnt)] = max(S - K, 0)
        return max(S - K, 0)

    up = recursion(n + 1, K, S * u, T, r, sig, M, u, d, p, q, dt, upCnt+1)
    dn = recursion(n + 1, K, S * d, T, r, sig, M, u, d, p, q, dt, upCnt)
    pc = (exp(-r * dt)) * (p * up + q * dn)
    Map[(n, upCnt)] = pc
    return pc


# -------------------------------------------------------------------------------------
# Given Initial Values -- and taking K = 100
S0, K, T, r, sig = 100, 100, 1, 0.08, 0.2
# Can handle values of M as much as 500 ..
Mlist = [5, 10, 25, 50, 100, 500]

for M in Mlist:
    dt = T/M

    u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p = (exp(r*dt)-d)/(u-d)
    q = 1-p
    Map.clear()
    loopbackOptionPrice = recursion(0, S0, S0, T, r, sig, M, u, d, p, q, dt, 0)
    print('The initial european call option price for M = {} is {}'.format(M, loopbackOptionPrice))

# Test computation time for M = 15: -----------------------------------------------------
dt = T/M
u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
p = (exp(r*dt)-d)/(u-d)
q = 1-p
Map.clear()
start = time.time()
timeTempPrice = recursion(0, S0, S0, T, r, sig, M, u, d, p, q, dt, 0)
end = time.time()

print('Computational time for M = 15 is {}s'.format(end-start))

# Question 3 algorithm 2 ends -------------------------------------------------------------
