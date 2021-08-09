% (b) Function program to solve a lower triangular system Lx=b by row oriented forward substitution
function b = rowforward(L,b)
    n = size(L,1);
    for k=1:n
        for j=1:k-1
            b(k) = b(k) - L(k,j)*b(j);
        end
  
        if L(k,k) ~= 0
            b(k) = b(k)/L(k,k);
        else
            fprintf('Matrix is singular');
            exit;
        end
    end
end