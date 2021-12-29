% This script runs the entire codebase

% European Options

% A comparison between the approximate solution and the exact solution corresponding to
% the European call options under the Merton model with λ = 0

S = [90;100;110]; K = 100; 
b = 1.5; sigma = 0.15; T = 0.25; r = 0.05; eta = 0.45; nu = -0.9; lambda = 0;
X = log(S/K);

M = 128; N = 25;
kappa=findKappa(nu,eta);
alpha = findAlpha(r,lambda,sigma,kappa);
beta = findBeta(sigma,lambda,r,kappa);

CCD_Values_1 = zeros(3,1);
Sim_Values_1 = zeros(3,1);
Exact_Values_1 = [0.36646; 3.63507; 11.50588];

for j=1:3
    x = X(j);
    Sim_Values_1(j) = simSol(S(j),N, T, r, lambda, sigma, nu, eta);

    h = 2*b/M;
    u = findUInitial(b, h, K, nu, eta, r, sigma, lambda, "call");
    [v, w] = findVWInitial(u, h, M);
    
    for i=1:N
        disp(i)
        [u, v, w] = CCDScheme(u, v, w, N, M, b, T, r, lambda, sigma, nu, eta, i);
    end
    
    % option prices
    V = u*exp(alpha*x + beta*T);
    idx = round((x+b)/h)+1; 
    CCD_Values_1(j) = V(idx)/2;
end

T = table(S, CCD_Values_1, Sim_Values_1, Exact_Values_1, abs(CCD_Values_1 - Exact_Values_1), 'VariableNames',{'S', 'CCD Scheme', 'Simulated', 'Exact', 'L∞ error'});
disp(T);

% A comparison between the approximate solution and the exact solution corresponding to
% the European call options under the Merton model with λ = 0.1

S = [90;130;170]; K = 100; 
b = 1.5; sigma = 0.15; T = 0.25; r = 0.05; eta = 0.45; nu = -0.9; lambda = 0.1;
X = log(S/K);

M = 128; N = 25;
kappa=findKappa(nu,eta);
alpha = findAlpha(r,lambda,sigma,kappa);
beta = findBeta(sigma,lambda,r,kappa);

CCD_Values_2 = zeros(3,1);
Sim_Values_2 = zeros(3,1);
Exact_Values_2 = [0.52764; 32.28218; 71.96065];

for j=1:3
    x = X(j);
    Sim_Values_2(j) = simSol(S(j),N, T, r, lambda, sigma, nu, eta);

    h = 2*b/M;
    u = findUInitial(b, h, K, nu, eta, r, sigma, lambda, "call");
    [v, w] = findVWInitial(u, h, M);
    
    for i=1:N
        disp(i)
        [u, v, w] = CCDScheme(u, v, w, N, M, b, T, r, lambda, sigma, nu, eta, i);
    end
    
    % option prices
    V = u*exp(alpha*x + beta*T);
    idx = round((x+b)/h)+1; 
    CCD_Values_2(j) = V(idx)/2;
end

T = table(S, CCD_Values_2, Sim_Values_2, Exact_Values_2, abs(CCD_Values_2 - Exact_Values_2), 'VariableNames',{'S', 'CCD Scheme', 'Simulated', 'Exact', 'L∞ error'});
disp(T);


S = [60:10:130]'; K = 100; 
b = 1.5; sigma = 0.15; T = 0.25; r = 0.05; eta = 0.45; nu = -0.9; lambda = 0.1;
X = log(S/K);

M = 128; N = 25;
kappa=findKappa(nu,eta);
alpha = findAlpha(r,lambda,sigma,kappa);
beta = findBeta(sigma,lambda,r,kappa);

CCD_Values_3 = zeros(size(S,1),1);
Sim_Values_3 = zeros(size(S,1),1);

for j=1:size(S,1)
    x = X(j);
    Sim_Values_3(j) = simSol(S(j),N, T, r, lambda, sigma, nu, eta);
  
    h = 2*b/M;
    u = findUInitial(b, h, K, nu, eta, r, sigma, lambda, "call");
    [v, w] = findVWInitial(u, h, M);
    
    for i=1:N
        disp(i)
        [u, v, w] = CCDScheme(u, v, w, N, M, b, T, r, lambda, sigma, nu, eta, i);
    end
    
    % option prices
    V = u*exp(alpha*x + beta*T);
    idx = round((x+b)/h)+1; 
    CCD_Values_3(j) = V(idx)/2;
end

plot(S, CCD_Values_3, '->');
hold on;
plot(S, Sim_Values_3, '-<');
xlabel('Stock Price (S)');
ylabel('Option Price')
legend('Numer Sol', 'Simulated Sol');
hold off;

plot(S, abs(Sim_Values_3-CCD_Values_3));
xlabel('Stock Price (S)');
ylabel('Error');




