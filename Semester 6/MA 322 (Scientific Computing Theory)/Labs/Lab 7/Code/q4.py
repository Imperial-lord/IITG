# Question 04, Lab 07
# AB Satyapraksh, 180123062

# imports
import pandas as pd

# functions


def f(t, y):
    return y - t**2 + 1


def RungeKutta2(t, y, h):
    return y + h*f(t+h/2, y+h*f(t, y)/2)


def RungeKutta4(t, y, h):
    k1 = f(t, y)
    k2 = f(t+h/2, y+h*k1/2)
    k3 = f(t+h/2, y+h*k2/2)
    k4 = f(t+h, y+h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6


def Euler(t, y, h):
    return y + h*f(t, y)


# program body
h1, h2, h3 = 0.025, 0.05, 0.1
euler, rk2, rk4 = [], [], []


t, y, i = 0, 0.5, 1
while t <= 2:
    y = Euler(t, y, h1)
    t = round(t+h1, 3)
    if t == round(0.1*i, 1):
        euler.append(y)
        i += 1
    if t == 0.5:
        break

t, y, i = 0, 0.5, 1
while t <= 2:
    y = RungeKutta2(t, y, h2)
    t = round(t+h2, 2)
    if t == round(0.1*i, 1):
        rk2.append(y)
        i += 1
    if t == 0.5:
        break

t, y, i = 0, 0.5, 1
while t <= 2:
    y = RungeKutta4(t, y, h3)
    t = round(t+h3, 1)
    if t == round(0.1*i, 1):
        rk4.append(y)
        i += 1
    if t == 0.5:
        break

# tabulate and print the results
df = pd.DataFrame()
df['Euler'] = pd.Series(euler)
df['Runge-Kutta O-2'] = pd.Series(rk2)
df['Runge-Kutta O-4'] = pd.Series(rk4)
df.set_index(pd.Series([0.1, 0.2, 0.3, 0.4, 0.5]), inplace=True)
print(df)
