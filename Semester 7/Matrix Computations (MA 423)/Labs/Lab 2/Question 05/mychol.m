function [G] = mychol(A)
    
    % mychol - function that accepts a symmetric positive definite matrix A
    % and returns it's Cholesky factor G
    
    [~, n] = size(A); G = zeros(n,n);
    
    for j = 1:n
        sum = 0;
        for k = 1:j-1
            sum = sum + (G(j,k))^2;
        end
        
        % check if the term inside the square root is <=0 => exit
        if A(j,j)-sum <= 0
            fprintf("Non-positive term encountered");
            return;
        end
        
        G(j,j) = sqrt(A(j,j)-sum);
        for i = j+1:n
            sum = 0;
            for k = 1:j-1
                 sum = sum + G(i,k)*G(j,k);
            end
        G(i,j) = (A(i,j)-sum)/G(j,j);
        end
    end
    G = G';
end

