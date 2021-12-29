function [iter,lambda] = Rayleigh(A,x,k)
    q = [];
    [~,i] = max(abs(x));
    s = x(i);
    x = x/s;
    q = [q x];
    [Q,H] = hess(A);
    n = size(A,1);
    rho = q'*H*q/(q'*q);
    
    for j=1:k-1
        [L,U,P] = lu(H - rho*eye(n));
        b = P*x;
        y = rowforward(L,b);
        x = colbackward(U,y);
        
        [~,i] = max(abs(x));
        s = x(i);
        x = x/s;
        q = [q x];
    end
    iter = q;
    lambda = 1/s + rho;
    iter = Q*iter;
end