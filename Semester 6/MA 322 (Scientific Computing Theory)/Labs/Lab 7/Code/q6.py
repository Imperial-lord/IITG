# Question 06, Lab 07
# AB Satyaprakash, 180123062

# imports
import pandas as pd
import numpy as np

# functions


def f(t, y, part):
    if part == 'a':
        return (2-2*t*y)/(1+t**2)
    if part == 'b':
        return y**2/(1+t)
    else:
        return (y**2 + y)/t


def F(t, part):
    if part == 'a':
        return (2*t+1)/(t**2+1)
    if part == 'b':
        return -1/np.log(1+t)
    else:
        return 2*t/(1-2*t)


def AdamsBashforth(t, y, h, part):
    return y[-1] + h*(55*f(t[-1], y[-1], part) - 59*f(t[-2], y[-2], part) + 37*f(t[-3], y[-3], part) - 9*f(t[-4], y[-4], part))/24


def AdasmMoulton(t, y, h, part):
    t1 = t[-1]+h
    y1 = AdamsBashforth(t, y, h, part)
    return y[-1] + h*(9*f(t1, y1, part) + 19*f(t[-1], y[-1], part) - 5*f(t[-2], y[-2], part) + f(t[-3], y[-3], part))/24


def RungeKutta4(t, y, h, part):
    k1 = f(t, y, part)
    k2 = f(t+h/2, y+h*k1/2, part)
    k3 = f(t+h/2, y+h*k2/2, part)
    k4 = f(t+h, y+h*k3, part)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6


# program body
# part (a)
part = 'a'
t = [0]
y1 = [1]
h = 0.1
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
while t[-1] < 1:
    y1.append(AdamsBashforth(t, y1, h, part))
    t.append(round(t[-1]+h, 1))
t = [0]
y2 = [1]
h = 0.1
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
while t[-1] < 1:
    y2.append(AdasmMoulton(t, y2, h, part))
    t.append(round(t[-1]+h, 1))
y3 = []
for T in t:
    y3.append(F(T, part))

df = pd.DataFrame()
df['Adams-Bashforth'] = pd.Series(y1)
df['Adams-Moulton'] = pd.Series(y2)
df['Actual Values'] = pd.Series(y3)
df.set_index(pd.Series(t), inplace=True)
print('For part (a):')
print(df)
print('----------------------------------------------------------------')


# part (b)
part = 'b'
t = [1]
y1 = [-1/np.log(2)]
h = 0.1
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
while t[-1] < 2:
    y1.append(AdamsBashforth(t, y1, h, part))
    t.append(round(t[-1]+h, 1))
t = [1]
y2 = [-1/np.log(2)]
h = 0.1
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
while t[-1] < 2:
    y2.append(AdasmMoulton(t, y2, h, part))
    t.append(round(t[-1]+h, 1))
y3 = []
for T in t:
    y3.append(F(T, part))

df = pd.DataFrame()
df['Adams-Bashforth'] = pd.Series(y1)
df['Adams-Moulton'] = pd.Series(y2)
df['Actual Values'] = pd.Series(y3)
df.set_index(pd.Series(t), inplace=True)
print('For part (b):')
print(df)
print('----------------------------------------------------------------')


# part (c)
part = 'c'
t = [1]
y1 = [-2]
h = 0.2
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
t.append(round(t[-1]+h, 1))
y1.append(RungeKutta4(t[-1], y1[-1], h, part))
while t[-1] < 3:
    y1.append(AdamsBashforth(t, y1, h, part))
    t.append(round(t[-1]+h, 1))
t = [1]
y2 = [-2]
h = 0.2
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
t.append(round(t[-1]+h, 1))
y2.append(RungeKutta4(t[-1], y2[-1], h, part))
while t[-1] < 3:
    y2.append(AdasmMoulton(t, y2, h, part))
    t.append(round(t[-1]+h, 1))
y3 = []
for T in t:
    y3.append(F(T, part))

df = pd.DataFrame()
df['Adams-Bashforth'] = pd.Series(y1)
df['Adams-Moulton'] = pd.Series(y2)
df['Actual Values'] = pd.Series(y3)
df.set_index(pd.Series(t), inplace=True)
print('For part (c):')
print(df)
print('----------------------------------------------------------------')
