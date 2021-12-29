from findKappa import findKappa
from findAlpha import findAlpha
import numpy as np
from scipy.stats import norm


def g(x, r, lambda_val, sigma, nu, eta):
    kappa = findKappa(nu, eta)
    alpha = findAlpha(r, lambda_val, sigma, kappa)

    y = np.exp(alpha*x)
    f = norm.pdf(x, nu, eta)
    y = y*f
    return y


# print(g(10, 0.05, 0.1, 0.15, -0.9, 0.45))
