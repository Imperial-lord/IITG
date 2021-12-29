function gamma = compositeBoole(u, M, b, r, lambda, sigma, nu, eta, j)
%This function calculates composite boole's quadrature
%and returns value of gamma.
%Input:
%   u       : Array of values of u at n-th time step
%   M       : Number of spatial steps
%   b       : |x| <= b
%   gamma   : Interest rate
%   lambda  : Poisson rate of arrival of jumps
%   sigma   : std dev of Stock prices
%   nu      : mean of jump sizes
%   eta     : std dev of jump sizes
%   j       : j-th value of gamma (starts from 1 [NOT 0])
%Output:
%   gamma   : Value of Composite Boole's Quadrature
    
    h = (2*b)/(M);
    x = -b:h:b;
    s1 = u(1)*g(-b-x(j), r, lambda, sigma, nu, eta);
    gamma = 7*s1;
  
    for i = 1:M/4-1
        gamma = gamma + 32*u(4*i-2)*g(x(4*i-2)-x(j), r, lambda, sigma, nu, eta);
        gamma = gamma + 12*u(4*i-1)*g(x(4*i-1)-x(j), r, lambda, sigma, nu, eta);
        gamma = gamma + 32*u(4*i)*g(x(4*i)-x(j), r, lambda, sigma, nu, eta);
        gamma = gamma + 14*u(4*i+1)*g(x(4*i+1)-x(j), r, lambda, sigma, nu, eta);
    end
    
    gamma = gamma + 32*u(M-2)*g(x(M-2)-x(j), r, lambda, sigma, nu, eta);
    gamma = gamma + 12*u(M-1)*g(x(M-1)-x(j), r, lambda, sigma, nu, eta);
    gamma = gamma + 32*u(M)*g(x(M)-x(j), r, lambda, sigma, nu, eta);
    gamma = gamma + 7*u(M+1)*g(x(M+1)-x(j), r, lambda, sigma, nu, eta);
    gamma = gamma *h*2/45;
end