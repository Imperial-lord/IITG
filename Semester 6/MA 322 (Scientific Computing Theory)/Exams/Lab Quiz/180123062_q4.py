# MA 322, Lab Quiz
# AB Satyaprakash, 180123062
# Question 4
# imports
from math import exp
import pandas as pd

# functions


def f(t, y):
    return 0.5*(t-y)


def RK2(t, y, h):
    return y + h*f(t+h/2, y+h*f(t, y)/2)


def RK4(t, y, h):
    k1 = f(t, y)
    k2 = f(t+h/2, y+h*k1/2)
    k3 = f(t+h/2, y+h*k2/2)
    k4 = f(t+h, y+h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6


def Euler(t, y, h):
    return y + h*f(t, y)


def S(x):
    return 3*exp(-x/2)+x-2


# program body
# given a list of h values
hList = [1, 1/2, 1/4, 1/8]

for h in hList:
    euler, rk2, rk4, sol = [1], [1], [1], [1]

    t = 0
    y = 1
    while t < 3:
        y = Euler(t, y, h)
        t = t+h
        euler.append(y)

    t = 0
    y = 1
    while t < 3:
        y = RK2(t, y, h)
        t = t+h
        rk2.append(y)

    t = 0
    y = 1
    while t < 3:
        y = RK4(t, y, h)
        t = t+h
        sol.append(S(t))
        rk4.append(y)

    df = pd.DataFrame()
    df['Euler'] = pd.Series(euler)
    df['Runge-Kutta Order 2'] = pd.Series(rk2)
    df['Runge-Kutta Order 4'] = pd.Series(rk4)
    df['Solution'] = pd.Series(sol)
    print(df)
    print()
