# Question 2 Lab 04
# AB Satyaprakash 180123062

# imports ----------------------------------------------------------------------
from scipy.optimize import minimize
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

# Data given from question 1 ---------------------------------------------------
m = np.array([0.1, 0.2, 0.15])
C = np.array([[0.005, -0.010, 0.004],
              [-0.010, 0.040, -0.002],
              [0.004, -0.002, 0.023]])
riskFreeRate = 0.1


# functions --------------------------------------------------------------------
def getReturn(weights):
    returns = np.sum(weights*m)
    return returns


def getRisk(weights):
    std = sqrt(np.dot(weights.T, np.dot(C, weights)))
    return std


def weightConstraint(weights):
    return np.sum(weights)-1


def boundsConstraint(n):
    # Shorting has been taken false
    bounds = np.array([0, 1]*n).reshape(n, 2)
    bounds = tuple(map(tuple, bounds))
    return bounds


def efficientFrontierBounded(returns):
    risks = np.array([])
    weights = []
    for ret in returns:
        constraints = ({'type': 'eq', 'fun': weightConstraint}, {
                       'type': 'eq', 'fun': lambda w: getReturn(w) - ret})
        result = minimize(getRisk, np.array(
            [0.3, 0.3, 0.4]), method='SLSQP', bounds=boundsConstraint(3), constraints=constraints)
        risks = np.append(risks, result['fun'])
        weights.append(result['x'])
    weights = np.array(weights)
    return risks, weights


def minimumVarianceCurve(returns, k):
    risks = np.array([])
    weights = []
    for ret in returns:
        constraints = ({'type': 'eq', 'fun': weightConstraint}, {
                       'type': 'eq', 'fun': lambda w: getReturn(w) - ret}, {'type': 'eq', 'fun': lambda w: w[k]-0})
        result = minimize(getRisk, np.array(
            [0.3, 0.3, 0.4]), method='SLSQP', bounds=boundsConstraint(3), constraints=constraints)
        risks = np.append(risks, result['fun'])
        weights.append(result['x'])
    weights = np.array(weights)
    return risks, weights


def getMinimumVarianceCurve(low, high, step, k):
    returns = np.arange(low, high, step)
    risks, weights = minimumVarianceCurve(returns, k)
    return returns, risks, weights


def getfeasibleRegion():
    returns, risks = np.array([]), np.array([])
    for i in range(100000):
        w = np.random.random(3)
        wsum = np.sum(w)
        w = w/wsum
        ret = getReturn(w)
        risk = getRisk(w)
        returns = np.append(returns, ret)
        risks = np.append(risks, risk)
    return returns, risks

# ------------------------------------------------------------------------------


returnsEff = np.arange(0.1, 0.2, 0.0001)
risksEff, weightsEff = efficientFrontierBounded(returnsEff)

returns01, risks01, weights01 = getMinimumVarianceCurve(0.1, 0.2, 0.0001, 2)
returns12, risks12, weights12 = getMinimumVarianceCurve(0.15, 0.2, 0.0001, 0)
returns02, risks02, weights02 = getMinimumVarianceCurve(0.1, 0.15, 0.0001, 1)

returnsfr, risksfr = getfeasibleRegion()

plt.figure()
plt.plot(risksEff, returnsEff, label='Efficient Frontier')
plt.scatter(risksfr, returnsfr, s=6, label='Feasible Region', color='lightgoldenrodyellow')
plt.plot(risks01, returns01, label='MVC: 1 & 2')
plt.plot(risks12, returns12, label='MVC: 2 & 3')
plt.plot(risks02, returns02, label='MVC: 1 & 3')
plt.title('Efficient Frontier, Minimum Variance Curve, Feasible Region - no short selling')
plt.xlabel('Value of Risk (σ)')
plt.ylabel('Value of Return (μ)')
plt.legend()
plt.show()


w01 = weights01[:, [0, 1]]
w12 = weights12[:, [1, 2]]
w02 = weights02[:, [0, 2]]


plt.figure()
plt.plot(w01[:, 0], w01[:, 1], color='darkorange')
plt.title("Weights corresponding to MVC: 1 & 2")
plt.xlabel('Weights 1')
plt.ylabel('Weights 2')
plt.show()

plt.figure()
plt.plot(w12[:, 0], w12[:, 1], color='green')
plt.title("Weights corresponding to MVC: 2 & 3")
plt.xlabel('Weights 2')
plt.ylabel('Weights 3')
plt.show()

plt.figure()
plt.plot(w02[:, 0], w02[:, 1], color='maroon')
plt.title("Weights corresponding to MVC: 1 & 3")
plt.xlabel('Weights 1')
plt.ylabel('Weights 3')
plt.show()

print('Clearly the weights satisfy the equation : y=1-x for all the 3 cases')
