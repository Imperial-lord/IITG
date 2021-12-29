function [iter,lambda] = Shiftinv(A,x,rho,k)
    q = [];
    q = [q x];
    n = size(A,1);
    [L,U,P] = lu(A - rho*eye(n));
    for j=1:k
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

end