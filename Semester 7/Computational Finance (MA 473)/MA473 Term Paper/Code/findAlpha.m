function alpha = findAlpha(r, lambda, sigma, kappa)
%This function finds value of alpha for CCD scheme
%Input:
%   r       : Interest Rate
%   lambda  : Poisson Arrival Intensity
%   sigma   : std dev of stock prices
%   kappa   : E[q(t)-1]
%Output:
%   alpha
    alpha = -(r-lambda*kappa-sigma*sigma/2)/(sigma*sigma);
    
end