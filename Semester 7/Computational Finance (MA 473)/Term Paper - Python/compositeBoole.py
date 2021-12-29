import numpy as np
from g import g
from findUInitial import findUInitial


def compositeBool(u, M, b, r, lambda_val, sigma, nu, eta, j):
    h = 2*b/M
    x = np.arange(-b, b+h, h)

    gamma = 7 * u[0]*g(-b-x[j], r, lambda_val, sigma, nu, eta)

    for i in range(0, int(M/4)-1):
        gamma += 32*u[4*i+1] * g(x[4*i+1]-x[j], r, lambda_val, sigma, nu, eta)
        gamma += 12*u[4*i+2] * g(x[4*i+2]-x[j], r, lambda_val, sigma, nu, eta)
        gamma += 32*u[4*i+3] * g(x[4*i+3]-x[j], r, lambda_val, sigma, nu, eta)
        gamma += 14*u[4*i+4] * g(x[4*i+4]-x[j], r, lambda_val, sigma, nu, eta)

    gamma += 32*u[M-3] * g(x[M-3]-x[j], r, lambda_val, sigma, nu, eta)
    gamma += 12*u[M-2] * g(x[M-2]-x[j], r, lambda_val, sigma, nu, eta)
    gamma += 32*u[M-1] * g(x[M-1]-x[j], r, lambda_val, sigma, nu, eta)
    gamma += 7*u[M] * g(x[M]-x[j], r, lambda_val, sigma, nu, eta)

    gamma *= h*2/45
    return gamma


# u = findUInitial(1.5, 3/128, 100, -0.9, 0.45, 0.05, 0.15, 0.1, 'call')
# print(compositeBool(u, 128, 1.5, 0.05, 0.1, 0.15, -0.9, 0.45, 128))
