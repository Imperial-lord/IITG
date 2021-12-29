function [x_sol] = SMsolve(A, u, v, m, b)
    % We will use GEPP for the following
    
    % Solving Ax = b
    x = geppsolve(A,b);
    
    % Solving Ay = u
    y = geppsolve(A,u);
    
    % The solution is given as x_sol = x - (vTx/(1+vTy))y
    x_sol = (x - ((transpose(v)*x) / (1+transpose(v)*y))*y)^m * b^(-(m-1));