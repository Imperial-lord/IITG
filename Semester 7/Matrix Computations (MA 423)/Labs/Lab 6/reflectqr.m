function [Q,R] = reflectqr(A)
    % function program [Q,R] =reflectqr(A) that computes the 
    % condensed QR-decomposition of A∈Rn×m, n≥m, via reflector
    
    [n,m] = size(A);    
    I = eye(n);
    
    g = zeros(m,1);
    Q = zeros(n,m);
    
    for i=1:m
        if(i~=n)   
            x = A(i:n,i);
            [u,gamma,t] = reflect(x);
            
            g(i) = gamma;
            A(i+1:n,i) = u(2:end);
            A(i:n,i+1:m) = applreflect(u,gamma,A(i:n,i+1:m));
            A(i,i)=-t;
        end
        
        temp = I(:,i);
        for j = i:-1:1
            u = [1,A(j+1:end, j)']';
            gamma = g(j);
            temp(j:end) = applreflect(u,gamma,temp(j:end));
        end
        Q(1:end,i) = temp;
    end
    R = triu(A);
    R = R(1:m,:);
end