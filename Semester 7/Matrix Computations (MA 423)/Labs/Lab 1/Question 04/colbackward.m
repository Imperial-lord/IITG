% (a) Function program to solve an upper triangular system Ux=b by column oriented back substitution
function b = colbackward(U,b)
    n = size(U,1);
    for j=n:-1:1
        if U(j,j) ~= 0
            b(j) = b(j)/U(j,j);
        else
            fprintf('Matrix is singular')
            exit;
        end
        
        for i = j-1:-1:1
            b(i) = b(i) - U(i,j)*b(j);
        end
    end   
end