# Question 05, Lab 07
# AB Satyapraksh, 180123062

# imports
import numpy as np
import pandas as pd

# functions


def f(t, y):
    return y - t**2 + 1


def F(t):
    return (t+1)**2 - 0.5*np.exp(t)


def AdamsBashforth(t, y, h):
    return y[-1] + h*(55*f(t[-1], y[-1]) - 59*f(t[-2], y[-2]) + 37*f(t[-3], y[-3]) - 9*f(t[-4], y[-4]))/24


def AdasmMoulton(t, y, h):
    t1 = t[-1]+h
    y1 = AdamsBashforth(t, y, h)
    return y[-1] + h*(9*f(t1, y1) + 19*f(t[-1], y[-1]) - 5*f(t[-2], y[-2]) + f(t[-3], y[-3]))/24


# program body
# part (a)
t, y1, h = [0], [0.5], 0.2
for i in range(3):
    t.append(round(t[-1]+h, 1))
    y1.append(F(t[-1]))

while t[-1] < 2:
    t.append(round(t[-1]+h, 1))
    y1.append(AdamsBashforth(t, y1, h))

# part (b)
t, y2, h = [0], [0.5], 0.2
for i in range(3):
    t.append(round(t[-1]+h, 1))
    y2.append(F(t[-1]))

while t[-1] < 2:
    t.append(round(t[-1]+h, 1))
    y2.append(AdasmMoulton(t, y2, h))

y3 = []
for T in t:
    y3.append(F(T))

#  tabulate and print the results
df = pd.DataFrame()
df['Adams-Bashforth'] = pd.Series(y1)
df['Adams-Moulton'] = pd.Series(y2)
df['Actual Value'] = pd.Series(y3)
df.set_index(pd.Series(t), inplace=True)
print(df)
