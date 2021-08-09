% Function program to find an LU factorization A=LU of an n-by-n matrix A 
% by performing Gaussian Elimination with no pivoting (GENP) 
function [L,U] = genp(A)
    n = size(A,1);
    for k = 1:n-1
        if A(k,k) ~= 0
            A(k+1:n,k) = A(k+1:n,k)/A(k,k);
        else
            fprintf('Matrix is singular');
            exit;
        end 
        A(k+1:n,k+1:n) = A(k+1:n,k+1:n) - A(k+1:n,k)*A(k,k+1:n);
    end
    L = tril(A) - diag(A).*eye(n) + eye(n);
    U = triu(A);
end


