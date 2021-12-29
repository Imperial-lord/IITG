function [Q,R]=mgs(V)
    % A function program to implement Modified Gram Schmidt procedure for 
    % orthonormalizing the columns of V
    m = size(V,2);
    R = zeros(size(V,1),m);
    for i=1:m
        for j=1:i-1
            R(j,i)= V(:,j)'*V(:,i);
            V(:,i) = V(:,i)-V(:,j)*R(j,i);
        end
        R(i,i) = norm(V(:,i),2);
        if (R(i,i)==0)
            exit('v1,.....,vk are dependent');
        end
        V(:,i)=V(:,i)/R(i,i);
    end
    Q=V;
end