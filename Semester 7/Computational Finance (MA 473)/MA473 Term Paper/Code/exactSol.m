function V_exact = exactSol(S, K, r, lambda, nu, eta, sigma, T)
% This function computes the exact solution of European Options with jumps

kappa = findKappa(nu, eta);
theta = lambda*(1+kappa);

V_exact = 0;

for m=1:100
    rm = r- lambda*kappa + m*log(1+kappa)/T;
    sigmam = sqrt(sigma*sigma + m*eta*eta/T);
    
    [CBS, ~] = blsprice(S,K,rm,T,sigmam);
    V_exact = V_exact + (exp(-theta*T)*power(theta*T,m)/factorial(m))*CBS;
end

end