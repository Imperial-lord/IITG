function x = geppsolve(A,b)
    % Function program to solve a system Ax=b via GEPP

    [L,U,p] = gepp(A);
    % Ly = b
    % Ux = y
    b = b(p);
    y = rowforward(L,b);
    x = colbackward(U,y);
end