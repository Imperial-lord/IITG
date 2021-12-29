function fin = simSol(S0, N, T, r, lambda, sigma, nu, eta)
 
    dt = T/N;
    K = 100; % strike price
    num_iter = 1000;

    fin = 0;
    for j=1:num_iter
        [S, ~] = jumpDiffusion(S0, r, sigma, nu, eta, lambda, dt, dt*N);
        C = max(S(end)-K, 0);
        fin = fin + C*exp(-r*dt*N);
    end
    fin = fin/num_iter;
end
