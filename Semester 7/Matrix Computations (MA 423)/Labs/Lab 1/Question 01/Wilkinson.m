% function to Generate a Wilkinson Matrix of size n
function WilkinsonMatrix = Wilkinson(n)
    A = -ones(n);
    W = tril(A,-1) + eye(n);
    W(1:n-1,n) = 1;
    WilkinsonMatrix = W;
end