import numpy as np

from findKappa import findKappa
from findAlpha import findAlpha


def findUInitial(b, h, K, nu, eta, r, sigma, lambda_val, option):
    M = round(2*b/h)
    h = 2*b/M

    x = np.arange(-b, b+h, h)
    SbyK = np.exp(x)

    if(option == 'call'):
        v = []
        val_arr = K*SbyK-K
        for val in val_arr:
            v.append(max(val, 0))
    else:
        v = []
        val_arr = K-K*SbyK
        for val in val_arr:
            v.append(max(val, 0))

    kappa = findKappa(nu, eta)
    alpha = findAlpha(r, lambda_val, sigma, kappa)

    u = np.multiply(v, np.exp(-alpha*x))

    # Testing stuff
    # print(v)
    # print(np.exp(-alpha*x))
    # print(u)

    # for i in range(0, len(u)):
    #     u_val = u[i]
    #     if(u_val != v[i]*np.exp(-alpha*x)[i]):
    #         print(i, 'omg')
    #         break

    return u


# print(findUInitial(1.5, 3/128, 100, -0.9, 0.45, 0.05, 0.15, 0.1, 'call'))
