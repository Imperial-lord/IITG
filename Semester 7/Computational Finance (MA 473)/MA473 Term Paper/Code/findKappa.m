function kappa = findKappa(nu, eta)
%This function finds value of kappa = E[q(t)-1]
%Input:
%   nu      : mean of the jump size
%   eta     : std dev of the jump size
%Output:
%   kappa   : E[q(t)-1]
    kappa = exp(nu+(eta*eta)/2)-1;
end