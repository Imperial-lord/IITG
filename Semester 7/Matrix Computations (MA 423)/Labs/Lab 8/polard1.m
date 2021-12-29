function [W,R] = polard1(A)
    [U,S,V] = svd(A);
    W = U*V';
    R = V*S*V';
end