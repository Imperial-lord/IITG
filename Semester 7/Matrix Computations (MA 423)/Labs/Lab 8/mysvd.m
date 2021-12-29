function [U,S,V] = mysvd(A)
    [W,R] = polard2(A');
    [V,D] = eig(R,'vector');
    [D, p] = sort(D,'descend');
    V = V(:, p);
    U = W*V;
    S = diag(D);
end