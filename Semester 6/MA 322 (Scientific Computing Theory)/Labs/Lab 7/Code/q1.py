# Question 01, Lab 01
# AB Satyaprakash, 180123062

import pandas as pd

k = 6.22*(10**(-19))
n1 = 2000
n2 = 2000
n3 = 3000


def f(x, y):
    return k*((n1-y/2)**2)*((n2-y/2)**2)*((n3-3*y/4)**3)


def RungeKutta4(x0, x1, y0, h, f):
    x = x0
    y = y0

    while(x < x1):
        k1 = f(x, y)
        k2 = f(x+h/2, y+h*k1/2)
        k3 = f(x+h/2, y+h*k2/2)
        k4 = f(x+h, y+h*k3)
        y = y+h*(k1+2*k2+2*k3+k4)/6
        x = x+h

    return y


h_list = [0.0001, 0.00001, 0.000001, 0.0000001]
vals = []
for h in h_list:
    vals.append(RungeKutta4(0, 0.2, 0, h, f))

h_list = [str(h) for h in h_list]
df = pd.DataFrame({'Value of h': h_list, 'Units of KOH after 2 seconds': vals})

print()
print(df)
print()
