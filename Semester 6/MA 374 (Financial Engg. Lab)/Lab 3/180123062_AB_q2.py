# Question 2 Lab Assignment 03
# @AB Satyaprakash, 180123062

# imports
from math import exp, sqrt
import numpy as np
import time

# Initialising a dictionary -- C++ equivalent to map<>
Map = {}
# functions ---------------------------------------------------------------------------


def recursion(n, Smax, S, T, r, sig, M, u, d, p, q, dt):
    if (Smax, S) in Map:
        return Map[(Smax, S)]

    if n == M:
        Map[(Smax, S)] = Smax - S
        return Smax - S

    up = recursion(n + 1, max(Smax, S * u), S * u, T, r, sig, M, u, d, p, q, dt)
    dn = recursion(n + 1, max(Smax, S * d), S * d, T, r, sig, M, u, d, p, q, dt)
    pc = (exp(-r * dt)) * (p * up + q * dn)
    Map[(Smax, S)] = pc
    return pc


# -------------------------------------------------------------------------------------
# Given Initial Values
S0, T, r, sig = 100, 1, 0.08, 0.2
# M takes values [5, 10, 25, 50] -- we'll consider all of them here
Mlist = [5, 10, 25, 50]

for M in Mlist:
    dt = T/M

    u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
    d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
    p = (exp(r*dt)-d)/(u-d)
    q = 1-p
    Map.clear()
    loopbackOptionPrice = recursion(0, S0, S0, T, r, sig, M, u, d, p, q, dt)
    print('The initial loopback option price for M = {} is {}'.format(M, loopbackOptionPrice))

# Test computation time for M = 15: ------------------------------------------------
dt = T/M

u = exp(sig*sqrt(dt)+(r-sig*sig/2)*dt)
d = exp(-sig*sqrt(dt)+(r-sig*sig/2)*dt)
p = (exp(r*dt)-d)/(u-d)
q = 1-p
Map.clear()
start = time.time()
timeTempPrice = recursion(0, S0, S0, T, r, sig, 15, u, d, p, q, dt)
end = time.time()

print('Computational time for M = 15 is {}s'.format(end-start))

# Question 2 ends ---------------------------------------------------------------------
