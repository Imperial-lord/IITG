# Question 07, Lab 07
# AB Satyaprakash, 180123062

# imports
import pandas as pd
import numpy as np

# functions


def f(t, y):
    return y - t**2 + 1


def F(t):
    return (t+1)**2 - 0.5*np.exp(t)


def RungeKutta4(t, y, h):
    k1 = f(t, y)
    k2 = f(t+h/2, y+h*k1/2)
    k3 = f(t+h/2, y+h*k2/2)
    k4 = f(t+h, y+h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6


def AdamsBashforth(t, y, h):
    return y[-1] + h*(55*f(t[-1], y[-1]) - 59*f(t[-2], y[-2]) + 37*f(t[-3], y[-3]) - 9*f(t[-4], y[-4]))/24


def AdasmMoulton(t, y, h):
    t1 = t[-1]+h
    y1 = AdamsBashforth(t, y, h)
    return y[-1] + h*(9*f(t1, y1) + 19*f(t[-1], y[-1]) - 5*f(t[-2], y[-2]) + f(t[-3], y[-3]))/24


# program body
t = [0]
y = [0.5]
h = 0.2
t.append(round(t[-1]+h, 1))
y.append(RungeKutta4(t[-1], y[-1], h))
t.append(round(t[-1]+h, 1))
y.append(RungeKutta4(t[-1], y[-1], h))
t.append(round(t[-1]+h, 1))
y.append(RungeKutta4(t[-1], y[-1], h))
yact = []

while t[-1] < 2:
    y.append(AdasmMoulton(t, y, h))
    t.append(round(t[-1]+h, 1))
for T in t:
    yact.append(F(T))

df = pd.DataFrame()
df["Adam's Predictor-Corrector Method"] = pd.Series(y)
df['Actual Value'] = pd.Series(yact)
df.set_index(pd.Series(t), inplace=True)
print(df)
