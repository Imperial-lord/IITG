# Question 3 Lab 04
# AB Satyaprakash 180123062

# imports ----------------------------------------------------------------------
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ------------------------------------------------------------------------------
data = pd.read_csv('data.csv', usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

C = np.array(data.cov())
m = np.array(data.mean())
u = np.ones(10)
m_trans = m.transpose()
C_trans = C.transpose()
u_trans = u.transpose()
C_inv = np.linalg.inv(C)
ret, sig = np.zeros(200), np.zeros(200)

# (a) Construct and plot the Markowitz efficient frontier.
for i in range(1, 201):
    ret[i-1] = i*6
    y = np.array([[ret[i-1]], [1]])
    M = np.array([[m.dot(C_inv).dot(m_trans), u.dot(C_inv).dot(m_trans)],
                  [m.dot(C_inv).dot(u_trans), u.dot(C_inv).dot(u_trans)]])
    lam = 2*(np.linalg.inv(M).dot(y))
    w = (lam[0][0]*(m.dot(C_inv))+lam[1][0]*(u.dot(C_inv)))/2
    sig[i-1] = sqrt(w.dot(C).dot(w.transpose()))

plt.plot(sig, ret, color='red')
plt.grid()
plt.title('Markowitz Efficient Frontier for the historical data')
plt.xlabel('Value of Risk (σ)')
plt.ylabel('Value of Return (μ)')
plt.show()


# (b) Determine the market portfolio
wm = ((m-0.05*u).dot(C_inv))/((m-0.05*u).dot(C_inv).dot(u_trans))
um = wm.dot(m_trans)
sigm = sqrt(wm.dot(C).dot(wm.transpose()))

print('\nFor 5% risk-free return --')
print('Weights :', end=' ')
for weight in wm:
    if(weight != wm[-1]):
        print(round(weight, 4), end=", ")
    else:
        print(round(weight, 4))
print('Return on market portfolio = {}%'.format('%.4f' % (um*100)))
print('Risk on market portfolio = {}%\n'.format('%.4f' % (sigm*100)))


# (c) Determine and plot the Capital Market Line.
x = np.arange(-2, 80.1, 0.1)
y = 0.05 + ((um-0.05)/sigm)*x
plt.scatter(sigm, um, marker=(5, 2), color='blue', label='Market Portfolio')
plt.plot(x, y, color='green', label='CML')
plt.plot(sig, ret, color='red', label='Markowitz Efficient Frontier')
plt.title('Capital Market Line and Markowitz Efficient Frontier')
plt.xlabel('Value of Risk (σ)')
plt.ylabel('Value of Return (μ)')
plt.legend()
plt.grid()
plt.show()


plt.plot(x, y, color='green')
plt.title('Capital Market Line')
plt.xlabel('Value of Risk (σ)')
plt.ylabel('Value of Return (μ)')
plt.grid()
plt.show()


# (d) Determine and plot the Security Market Line for all the 10 assets.
beta = np.arange(-2, 2.1, 0.1)
for i in range(m.shape[0]):
    mean = m[i]
    muv = 0.05+(mean-0.05)*beta
    plt.plot(beta, muv, label=data.columns[i])
plt.title('Security Market Line for all the 10 assets of')
plt.xlabel('Beta coefficient (β)')
plt.ylabel('Value of Return (μ)')
plt.grid()
plt.legend()
plt.show()

# Question 3 ends --------------------------------------------------------------
