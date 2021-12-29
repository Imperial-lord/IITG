function y = g(x, r, lambda, sigma, nu, eta)
%This function finds the value of g(x) = e^(alpha*x)f(x)
%Input:
%   x       : Point at which function value has to be calculated
%   r       : Interest Rate
%   lambda  : Poisson rate of arrival of jumps
%   sigma   : std dev of Stock prices
%   nu      : mean of jump sizes
%   eta     : std dev of jump sizes
%   dt      : time step size
%Output:
%   y   : Value of function at point x
    kappa = findKappa(nu, eta);
    alpha = findAlpha(r, lambda, sigma, kappa);
    y = exp(alpha*x);
    %m = r-0.25/25-lambda*findKappa(nu, eta);
    %f = normpdf(x, m, sigma);
    f = normpdf(x, nu, eta);
    y = y*f;
end