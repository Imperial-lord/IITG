function A = condmat(n,kappa)
    % A function program A = condmat(n, kappa) that generates a random n × n 
    % positive definite matrix A with given condition number kappa
    
    D = [];
    for i=1:n
       D = [D;kappa^((i-1)/(n-1))]; 
    end
    D = diag(D);
    X = randn(n,n);
    [U,R] = qr(X);
    A = U*D*U';
end