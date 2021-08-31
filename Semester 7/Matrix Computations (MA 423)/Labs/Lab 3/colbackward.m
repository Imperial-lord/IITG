function b = colbackward(U,b)
    n = size(U,1);
    
    for j=n:-1:1
        if U(j,j) ~= 0
            b(j) = b(j)/U(j,j);
        else
            disp('Matrix is singular');
            return;
        end
        
        for i = j-1:-1:1
            b(i) = b(i) - U(i,j)*b(j);
        end
    end
        
end