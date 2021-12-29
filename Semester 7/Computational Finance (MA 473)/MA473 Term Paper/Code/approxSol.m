function x0 = approxSol(x, N, T, r, lambda, sigma, nu, eta, k_n)
 
    dt = T/N;
    [~,n] = size(x);
    x0 = zeros(n,1);
    K = 100; % strike price
    num_iter = 100;

    kappa=findKappa(nu,eta);
    alpha = findAlpha(r,lambda,sigma,kappa);
    beta = findBeta(sigma,lambda,r,kappa);

    for i=1:n
        S0 = K*exp(x(i));
        fin = 0;
        for j=1:num_iter
            [S, ~] = jumpDiffusion(S0, r, sigma, nu, eta, lambda, dt, dt*k_n);
            C = max(S(end)-K, 0);
            fin = fin + C*exp(-r*dt*k_n);
        end
        fin = fin/num_iter;
        x0(i) = fin*exp(-alpha*x(i)-beta*(dt*k_n));
    end
end