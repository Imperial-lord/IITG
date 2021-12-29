function b = rowforward(l,b)
    n = size(l,1);

    for k=1:n
        for j=1:k-1
            b(k) = b(k) - l(k,j)*b(j);
        end
        
        if l(k,k) ~= 0
            b(k) = b(k)/l(k,k);
        else
            disp('Matrix is singular');
            return;
        end
    end
end