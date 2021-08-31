function x = geppsolve(A,b)
    [L,U,p] = gepp(A);
    % Ly = b
    % Ux = y
    b = b(p);
    y = rowforward(L,b);
    x = colbackward(U,y);
    
end