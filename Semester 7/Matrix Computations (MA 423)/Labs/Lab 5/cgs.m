function [Q,R]=cgs(V)
    %{
A function program [Q, R] = cgs(V) to orthonormalize the columns of an 
n × m matrix V, (n ≥ m) by the Classical Gram Schmidt procedure so that Q is an
isometry satisfying
    span{Q(:, 1)} = span{V (:, 1)}
    span{Q(:, 1), Q(:, 2)} = span{V (:, 1), V (:, 2)},
    .
    .
    .
    span{Q(:, 1), Q(:, 2), . . . , Q(:, m)} = span{V (:, 1), V (:, 2), . . . , V (:, m)}
and R is an upper triangular matrix such that R(i, j) = hV (:, j), Q(:, i)i.
    %}

    m = size(V,2);
    R=zeros(size(V,1),m);
    for i=1:m
        R(1:i-1,i)= V(:,1:i-1)'*V(:,i); % Inner product <Vk,Vi>
        for j=1:i-1
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