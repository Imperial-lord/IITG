function [xc] = geppsolve(A,b)
    [L,U,p] = gepp(A);
    % Ly = Pb & Ux = y
    b = b(p);
    y = rowforward(L,b);
    xc = colbackward(U,y);
end

