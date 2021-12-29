function R1 = mysqrt1(A)
    [X,D] = eig(A);
    D = D.^(0.5);
    R1 = X*D*(inv(X));    
end