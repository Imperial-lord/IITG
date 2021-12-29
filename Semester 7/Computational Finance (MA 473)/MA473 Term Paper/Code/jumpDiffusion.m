function [S, t_arr] = jumpDiffusion(S0, r, sigma, nu, eta, lambda, dt, T)
%   This function generates stock prices following the Jump Diffusion Model
%Inputs:
%   S0      : Initial Stock Price
%   r       : Interest Rate
%   sigma   : std dev of Stock Prices
%   nu      : Mean of log normal jump ratios
%   eta     : Std Dev of log normal jump ratios
%   lambda  : Jump Frequency
%   T       : Time
%Outputs:
%   S       : Array of Stock Prices

    X0 = log(S0);
    X = [X0];
    S = [S0];
    t_arr = [0];
    t = 0;
    m = r-dt-lambda*findKappa(nu, eta);
    while(t < T)
        n = numjumps(lambda, dt);
        z = randn;
        y = 0;
        while(n)
            y1 = lognrnd(nu, eta);
            y = y+log(y1);
            n = n-1;
        end
        X_temp = X(end) + (m-sigma*sigma/2)*dt+z*sqrt(sigma*sigma*dt)+y;
        X = [X, X_temp];
        S = [S, exp(X_temp)];
        t = t+dt;
        t_arr = [t_arr, t];
    end
    %plot(t_arr, S);
end

function n = numjumps(lambda, dt)
    n = poissrnd(dt*lambda);
end