function u = findUInitial(b, h, K, nu, eta, r, sigma, lambda, option)
%This function finds initial value of u
%Input:
%   b       : |x| <= b
%   h       : Spatial step size
%   K       : Strike Price
%Output:
%   u       

M = round(2*b/h);
h = 2*b/M;

x = -b:h:b;
SbyK = exp(x);
if option == "call"
    v = max(0, K*SbyK-K);
else
    v = max(0, K-K*SbyK);
end

kappa = findKappa(nu, eta);
alpha = findAlpha(r, lambda, sigma, kappa);

u = (v.*exp(-alpha*x))';
end