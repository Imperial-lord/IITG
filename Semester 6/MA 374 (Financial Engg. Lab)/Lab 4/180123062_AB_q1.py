# Question 1 Lab 04
# AB Satyaprakash 180123062

# imports ----------------------------------------------------------------------
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


# ------------------------------------------------------------------------------
# (a) Plotting the Markowitz efficient frontier and
# (b) Tabulating Return, Risk and Weights for 10 different values on the efficient frontier
# Given Mean vector and Covariance matrix
m = np.array([0.1, 0.2, 0.15])
C = np.array([[0.005, -0.010, 0.004],
              [-0.010, 0.040, -0.002],
              [0.004, -0.002, 0.023]])
u = np.array([1, 1, 1])

m_trans = m.transpose()
C_trans = C.transpose()
u_trans = u.transpose()
C_inv = np.linalg.inv(C)

ret, sig = np.zeros(100), np.zeros(100)
print(' Return - Risk   -   W1    -    W2    -    W3\n')

# Finding and tabulating the values
for i in range(1, 101):
    ret[i-1] = i*0.005
    y = np.array([[ret[i-1]], [1]])
    M = np.array([[m.dot(C_inv).dot(m_trans), u.dot(C_inv).dot(m_trans)],
                  [m.dot(C_inv).dot(u_trans), u.dot(C_inv).dot(u_trans)]])
    lam = 2*(np.linalg.inv(M).dot(y))
    w = (lam[0][0]*(m.dot(C_inv))+lam[1][0]*(u.dot(C_inv)))/2
    sig[i-1] = sqrt(w.dot(C).dot(w.transpose()))
    if i % 10 == 0:
        print('  {}   {}    {}    {}     {}  '.format(
            '%.2f' % ret[i-1], '%.4f' % sig[i-1], '%.4f' % w[0], '%.4f' % w[1], '%.4f' % w[2]))

# Plotting the efficient frontier
plt.plot(sig, ret, color='red')
plt.grid()
plt.title('Markowitz Efficient Frontier for the given data')
plt.xlabel('Value of Risk (σ)')
plt.ylabel('Value of Return (μ)')
plt.show()


# (c) risk = 15%, calculate the maximum and minimum return and corresponding portfolios
A = u.dot(C_inv).dot(u_trans)
B = u.dot(C_inv).dot(m_trans)
V = m.dot(C_inv).dot(m_trans)
d = A*V - B*B
risk = 0.15

# Maximum return
ret_max = (2*B+sqrt(4*B*B-4*A*(V-d*risk*risk)))/(2*A)
y = np.array([[ret_max], [1]])
M = np.array([[m.dot(C_inv).dot(m_trans), u.dot(C_inv).dot(m_trans)],
              [m.dot(C_inv).dot(u_trans), u.dot(C_inv).dot(u_trans)]])
lam = 2*(np.linalg.inv(M).dot(y))
w = (lam[0][0]*(m.dot(C_inv))+lam[1][0]*(u.dot(C_inv)))/2
print('\n\nMaximum Return Portfolio for 15% risk --')
print('Return = {}% and Weights : {},  {},  {}'.format('%.4f' %
                                                       (ret_max*100), '%.4f' % w[0], '%.4f' % w[1], '%.4f' % w[2]))


# Minimum return
ret_min = (2*B-sqrt(4*B*B-4*A*(V-d*risk*risk)))/(2*A)
y = np.array([[ret_min], [1]])
M = np.array([[m.dot(C_inv).dot(m_trans), u.dot(C_inv).dot(m_trans)],
              [m.dot(C_inv).dot(u_trans), u.dot(C_inv).dot(u_trans)]])
lam = 2*(np.linalg.inv(M).dot(y))
w = (lam[0][0]*(m.dot(C_inv))+lam[1][0]*(u.dot(C_inv)))/2
print('\n\nMinimum Return Portfolio for 15% risk --')
print('Return = {}% and Weights : {},  {},  {}'.format('%.4f' %
                                                       (ret_min*100), '%.4f' % w[0], '%.4f' % w[1], '%.4f' % w[2]))


# (d) return = 18%, calculate the minimum risk portfolio
y = np.array([[0.18], [1]])  # using return = 18%
M = np.array([[m.dot(C_inv).dot(m_trans), u.dot(C_inv).dot(m_trans)],
              [m.dot(C_inv).dot(u_trans), u.dot(C_inv).dot(u_trans)]])
lam = 2*(np.linalg.inv(M).dot(y))
w = (lam[0][0]*(m.dot(C_inv))+lam[1][0]*(u.dot(C_inv)))/2
risk = sqrt(w.dot(C).dot(w.transpose()))
print('\n\nMinimum Risk Portfolio for 18% return --')
print('Risk = {}% and Weights : {},  {},  {}'.format('%.4f' %
                                                     (risk*100), '%.4f' % w[0], '%.4f' % w[1], '%.4f' % w[2]))

# (e) Given µrf = 10%, compute the market portfolio and plot the CML
wm = ((m-0.1*u).dot(C_inv))/((m-0.1*u).dot(C_inv).dot(u_trans))
um = wm.dot(m_trans)
sigm = sqrt(wm.dot(C).dot(wm.transpose()))

print('\nFor 10% risk-free return --')
print('Weights : {},  {},  {}'.format('%.4f' % wm[0], '%.4f' % wm[1], '%.4f' % wm[2]))
print('Return on market portfolio = {}%'.format('%.4f' % (um*100)))
print('Risk on market portfolio = {}%\n'.format('%.4f' % (sigm*100)))

x = np.arange(0, 1.1, 0.1)
y = 0.1 + ((um-0.1)/sigm)*x
plt.scatter(sigm, um, marker=(5, 2), color='blue', label='Market Portfolio')
plt.scatter([0], [0.1], marker='o', color='green', label='Zero Risk Portfolio')
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


# (f) Find 2 portfolios (having both risky and risk free assets) with risk = 10% and 25%.
y = 0.1+(um-0.1)/sigm*0.1
rf = (y-um)/(0.1-um)
risked = (1-rf)*wm

print('\nPortfolio for 10% risk --')
print('Risk-Free Asset : {}'.format('%.4f' % rf))
print('Risky Assets Weights : {},  {},  {}'.format('%.4f' %
                                                   risked[0], '%.4f' % risked[1], '%.4f' % risked[2]))


y = 0.1+(um-0.1)/sigm*0.25
rf = (y-um)/(0.1-um)
risked = (1-rf)*wm

print('\nPortfolio for 25% risk --')
print('Risk-Free Asset : {}'.format('%.4f' % rf))
print('Risky Assets Weights : {},  {},  {}'.format('%.4f' %
                                                   risked[0], '%.4f' % risked[1], '%.4f' % risked[2]))

# Question 1 ends --------------------------------------------------------------
