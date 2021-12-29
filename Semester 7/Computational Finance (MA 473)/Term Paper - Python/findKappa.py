import numpy as np


def findKappa(nu, eta):
    kappa = np.exp(nu+(eta*eta)/2) - 1
    return kappa


# findKappa(-0.9, 0.45)
