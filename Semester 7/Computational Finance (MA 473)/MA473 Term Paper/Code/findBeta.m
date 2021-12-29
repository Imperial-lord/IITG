function beta = findBeta(sigma,lambda,r,kappa)
%This function calculates value of beta
%Input:
%   sigma   : Array of values of u_initial
%   lambda  : Possion arrival frequency
%   r       : Interest rate
%   kappa   : E[q(t)-1]
%Output:
%   beta   : xxx

alpha = findAlpha(r,lambda,sigma,kappa);
beta = (-1/2)*(alpha^2)*(sigma^2) - (lambda + r);

end