def findAlpha(r, lambda_val, sigma, kappa):
    alpha = -((r - lambda_val*kappa - (1/2)*(sigma*sigma))/(sigma*sigma))
    return alpha


# findAlpha(0.05, 0.1, 0.15, findKappa(-0.9, 0.45))
