function R2 = mysqrt2(A)
    G = chol(A);
    [U,S,V] = svd(G);
    R2 = V*S*V'; 
end