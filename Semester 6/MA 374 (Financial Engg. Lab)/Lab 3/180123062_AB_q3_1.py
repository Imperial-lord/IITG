# Question 3 Algorithm 1 (inefficient) Lab Assignment 03
# @AB Satyaprakash, 180123062

# imports
from math import exp, sqrt
import numpy as np
import time

# functions ---------------------------------------------------------------------------


def recursion(n, K, S, T, r, sig, M, u, d, p, q, dt):

    if n == M:
        return max(S - K, 0)

    up = recursion(n + 1, K, S * u, T, r, sig, M, u, d, p, q, dt)
    dn = recursion(n + 1, K, S * d, T, r, sig, M, u, d, p, q, dt)
    pc = (exp(-r * dt)) * (p * up + q * dn)
    return pc


# -------------------------------------------------------------------------------------
# Given Initial Values -- and taking K = 100
S0, K, T, r, sig = 100, 100, 1, 0.08, 0.2
# Can't handle values of M beyond 20 ..
Mlist = [5, 10, 20]

for M in Mlist:
    dt = T/M

    u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p = (exp(r*dt)-d)/(u-d)
    q = 1-p
    loopbackOptionPrice = recursion(0, K, S0, T, r, sig, M, u, d, p, q, dt)
    print('The initial european call option price for M = {} is {}'.format(M, loopbackOptionPrice))

# Test computation time for M = 15: ------------------------------------------------
dt = T/M
u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
p = (exp(r*dt)-d)/(u-d)
q = 1-p
start = time.time()
timeTempPrice = recursion(0, K, S0, T, r, sig, M, u, d, p, q, dt)
end = time.time()

print('Computational time for M = 15 is {}s'.format(end-start))

# Question 3 algorithm 1 ends -------------------------------------------------------------
