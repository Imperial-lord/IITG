function [L,U] = genp(A)
    % Function program to perform LU factorisation using GENP

    n = size(A,1);
    for k = 1:n-1
        if A(k,k) ~= 0
            A(k+1:n,k) = A(k+1:n,k)/A(k,k);
        else
            fprintf('Zero pivot encountered');
            exit;
        end
        A(k+1:n,k+1:n) = A(k+1:n,k+1:n) - A(k+1:n,k)*A(k,k+1:n);
    end
    L = tril(A) - diag(A).*eye(n) + eye(n);
    U = triu(A);
end