function [u_n1, v_n1, w_n1] = CCDScheme(u_n, v_n, w_n, N, M, b, T, r, lambda, sigma, nu, eta, k_n)
%This function returns value of u, u' and u'' for
%time step n+1, given the values at time step n.
%Input:
%   u_n     : Array of values of u at time step n
%   v_n     : Array of values of u' at time step n
%   w_n     : Array of values of u'' at time step n
%   N       : Number of temporal steps
%   M       : Number of spatial steps
%   b       : |x| <= b
%   T       : Time to maturity
%   r       : Interest Rate
%   lambda  : Poisson rate of arrival of jumps
%   sigma   : std dev of Stock prices
%   nu      : mean of jump sizes
%   eta     : std dev of jump sizes
%   k_n     : iteration count       
%Output:
%   u_n1     : Array of values of u at time step n+1
%   v_n1     : Array of values of u' at time step n+1
%   w_n1     : Array of values of u'' at time step n+1
    
    %Calculating spatial and temporal step size and x
    h = (2*b)/M;
    k = T/N;
    x = -b:h:b;
    
    %Ax=B
    B=zeros(3*M+3,1);
    A=zeros(3*M+3,3*M+3);
    
    for i = 1:3*M-3
        i1 = floor((i+2)/3);
        if mod(i,3) == 0
            gamma = compositeBoole(u_n, M, b, r, lambda, sigma, nu, eta, i1+1);
            B(i) = u_n(i1+1)+(k*sigma*sigma/4)*w_n(i1+1)+(k*lambda/2)*gamma;
        elseif mod(i,3) == 1
            B(i) = -v_n(i1+1);
        else
            B(i) = 0;
        end
    end
    gamma = compositeBoole(u_n, M, b, r, lambda, sigma, nu, eta, 1);
    B(3*M-2) = u_n(1)+(k*sigma*sigma/4)*w_n(1)+(k*lambda/2)*gamma;
    gamma = compositeBoole(u_n, M, b, r, lambda, sigma, nu, eta, M+1);
    B(3*M-1) = u_n(M+1)+(k*sigma*sigma/4)*w_n(M+1)+(k*lambda/2)*gamma;
    %Last four values of B are zero because boundary conditions involve no
    %terms corresponding to n-th time step

    for i = 1:3*M-3
        i1 = floor((i+2)/3);
        if mod(i,3) == 0
            A(i, i1+1) = 1;
            A(i, 2*M+2+i1+1) = -k*sigma*sigma/4;
            A(i, 1) = A(i, 1) + (-k*h*lambda/45)*(7*g(-b-x(i1+1), r, lambda, sigma, nu, eta));
            A(i, M+1) = A(i, M+1) + (-k*h*lambda/45)*(7*g(b-x(i1+1), r, lambda, sigma, nu, eta));
          
            for j = 1 : M/4-1
                A(i, 4*j-2) = A(i, 4*j-2) + (-k*h*lambda/45)*32*g(x(4*j-2)-x(i1+1), r, lambda, sigma, nu, eta);
                A(i, 4*j-1) = A(i, 4*j-1) + (-k*h*lambda/45)*12*g(x(4*j-1)-x(i1+1), r, lambda, sigma, nu, eta);
                A(i, 4*j) = A(i, 4*j) + (-k*h*lambda/45)*32*g(x(4*j)-x(i1+1), r, lambda, sigma, nu, eta);
                A(i, 4*j+1) = A(i, 4*j+1) + (-k*h*lambda/45)*14*g(x(4*j+1)-x(i1+1), r, lambda, sigma, nu, eta);
            end
            
            A(i, M-2) = A(i, M-2) + (-k*h*lambda/45)*32*g(x(M-2)-x(i1+1), r, lambda, sigma, nu, eta);
            A(i, M-1) = A(i, M-1) + (-k*h*lambda/45)*12*g(x(M-1)-x(i1+1), r, lambda, sigma, nu, eta);
            A(i, M) = A(i, M) + (-k*h*lambda/45)*32*g(x(M)-x(i1+1), r, lambda, sigma, nu, eta);

        elseif mod(i,3) == 1
            A(i, i1) = 15/(16*h);
            A(i, i1+2) = -15/(16*h);
            A(i, M+1+i1) = 7/16;
            A(i, M+1+i1+2) = 7/16;
            A(i, 2*M+2+i1) = h/16;
            A(i, 2*M+2+i1+2) = -h/16;
        else
            A(i, i1) = 3/(h*h);
            A(i, i1+1) = -6/(h*h);
            A(i, i1+2) = 3/(h*h);
            A(i, M+1+i1) = 9/(8*h);
            A(i, M+1+i1+2) = -9/(8*h);
            A(i, 2*M+2+i1) = 1/8;
            A(i, 2*M+2+i1+1) = -1;
            A(i, 2*M+2+i1+2) = 1/8;
        end
    end

    %Equation 1 for j = 0
    A(3*M-2, 2*M+2+1) = -k*sigma*sigma/4;
    
    A(3*M-2, 1) = 1 + (-k*h*lambda/45)*(7*g(0, r, lambda, sigma, nu, eta));
    A(3*M-2, M+1) = A(3*M-2, M+1) + (-k*h*lambda/45)*(7*g(2*b, r, lambda, sigma, nu, eta));
  
    for j = 1 : M/4-1
        A(3*M-2, 4*j-2) = A(3*M-2, 4*j-2) + (-k*h*lambda/45)*32*g(x(4*j-2)+b, r, lambda, sigma, nu, eta);
        A(3*M-2, 4*j-1) = A(3*M-2, 4*j-1) + (-k*h*lambda/45)*12*g(x(4*j-1)+b, r, lambda, sigma, nu, eta);
        A(3*M-2, 4*j) = A(3*M-2, 4*j) + (-k*h*lambda/45)*32*g(x(4*j)+b, r, lambda, sigma, nu, eta);
        A(3*M-2, 4*j+1) = A(3*M-2, 4*j+1) + (-k*h*lambda/45)*14*g(x(4*j+1)+b, r, lambda, sigma, nu, eta);
    end
    
    A(3*M-2, M-2) = A(3*M-2, M-2) + (-k*h*lambda/45)*32*g(x(M-2)+b, r, lambda, sigma, nu, eta);
    A(3*M-2, M-1) = A(3*M-2, M-1) + (-k*h*lambda/45)*12*g(x(M-1)+b, r, lambda, sigma, nu, eta);
    A(3*M-2, M) = A(3*M-2, M) + (-k*h*lambda/45)*32*g(x(M)+b, r, lambda, sigma, nu, eta);

    %Equation 1 for j = M
    A(3*M-1, 3*M+3) = -k*sigma*sigma/4;
    A(3*M-1, 1) = A(3*M-1, 1) + (-k*h*lambda/45)*(7*g(-2*b, r, lambda, sigma, nu, eta));
    A(3*M-1, M+1) = 1 + (-k*h*lambda/45)*(7*g(0, r, lambda, sigma, nu, eta));
    for j = 1 : M/4-1
        A(3*M-1, 4*j-2) = A(3*M-1, 4*j-2) + (-k*h*lambda/45)*32*g(x(4*j-2)-b, r, lambda, sigma, nu, eta); 
        A(3*M-1, 4*j-1) = A(3*M-1, 4*j-1) + (-k*h*lambda/45)*12*g(x(4*j-1)-b, r, lambda, sigma, nu, eta);
        A(3*M-1, 4*j) = A(3*M-1, 4*j) + (-k*h*lambda/45)*32*g(x(4*j)-b, r, lambda, sigma, nu, eta);
        A(3*M-1, 4*j+1) = A(3*M-1, 4*j+1) + (-k*h*lambda/45)*14*g(x(4*j+1)-b, r, lambda, sigma, nu, eta);
    end
    
    A(3*M-1, M-2) = A(3*M-1, M-2) + (-k*h*lambda/45)*32*g(x(M-2)-b, r, lambda, sigma, nu, eta);
    A(3*M-1, M-1) = A(3*M-1, M-1) + (-k*h*lambda/45)*12*g(x(M-1)-b, r, lambda, sigma, nu, eta);
    A(3*M-1, M) = A(3*M-1, M) + (-k*h*lambda/45)*32*g(x(M)-b, r, lambda, sigma, nu, eta);

    %Equation 4
    A(3*M, 1) = 31/h; A(3*M, 2) = -32/h; A(3*M, 3) = 1/h; 
    A(3*M, M+1+1) = 14; A(3*M, M+1+2) = 16; 
    A(3*M, 2*M+2+1) = 2*h; A(3*M, 2*M+2+2) = -4*h;

    %Equation 5
    A(3*M+1, M+1) = -31/h; A(3*M+1, M) = 32/h; A(3*M+1, M-1) = -1/h; 
    A(3*M+1, M+1+M+1) = 14;A(3*M+1, M+1+M) = 16; 
    A(3*M+1, 2*M+2+M+1) = -2*h; A(3*M+1, 2*M+2+M) = 4*h;

    %Equation 6
    A(3*M+2, 1) = 7/(2*h); A(3*M+2, 2) = -4/h; A(3*M+2, 3) = 1/(2*h);
    A(3*M+2, M+1+1) = 1; A(3*M+2, M+1+2) = 2; 
    A(3*M+2, 2*M+2+2) = -h;

    %Equation 7
    A(3*M+3, M+1) = -7/(2*h); A(3*M+3, M) = 4/h; A(3*M+3, M-1) = -1/(2*h);
    A(3*M+3, M+1+M+1) = 1; A(3*M+3, M+1+M) = 2;
    A(3*M+3, 2*M+2+M) = h;
    
    u0 = approxSol(x, N, T, r, lambda, sigma, nu, eta, k_n);
    [v0, w0] = findVWInitial(u0,h,M);
    x0 = [u0;v0;w0];

    [sol, ~] = bicgstabl(A,B,1e-6,1000,[],[],x0);

    u_n1 = sol(1:M+1);
    v_n1 = sol(M+2:2*M+2);
    w_n1 = sol(2*M+3:end);
end