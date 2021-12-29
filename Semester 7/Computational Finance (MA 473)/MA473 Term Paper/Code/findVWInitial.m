function [v, w] = findVWInitial(u, h, M)
%This function calculates values of v = u' and w = u''
%Input:
%   u   : Array of values of u_initial
%   h   : Spatial step size
%Output:
%   v   : Array of values of v_initial
%   w   : Array of values of w_initial

    % Ax=b 
    b = zeros(2*M+2,1);
    A = zeros(2*M+2,2*M+2);
    
    for i = 1:2*M-2
        i1 = floor((i+1)/2);
        if mod(i,2) == 0
            b(i,1) = (-15/(16*h))*u(i1)+(15/(16*h))*u(i1+2);
        else
            b(i,1) = (3/(h*h))*u(i1) - (6/(h*h))*u(i1+1) + (3/(h*h))*u(i1+2);
        end
    end
    b(2*M-1,1) = (-1/h)*(31*u(1) - 32*u(2) + u(3));
    b(2*M,1) = (1/h)*(31*u(M+1) - 32*u(M) + u(M-1));
    b(2*M+1,1) = (-1/(2*h))*(7*u(1) - 8*u(2) + u(3));
    b(2*M+2,1) = (1/(2*h))*(7*u(M+1) - 8*u(M) + u(M-1));

    for i = 1:2*M-2
        i1 = floor((i+1)/2);
        if mod(i,2) == 0
            A(i,i1) = 7/16;
            A(i,i1+1) = 1;
            A(i,i1+2) = 7/16;
            A(i,M+1+i1) = h/16;
            A(i,M+1+i1+2) = -h/16;
        else
            A(i,i1) = -9/(8*h);
            A(i,i1+2) = 9/(8*h);
            A(i,M+1+i1) = -1/8;
            A(i,M+1+i1+1) = 1;
            A(i,M+1+i1+2) = -1/8;
        end
    end
    A(2*M-1,1) = 14; A(2*M-1,2) = 16; A(2*M-1,M+1+1) = 2*h; A(2*M-1,M+1+2) = -4*h;
    A(2*M,M+1) = 14; A(2*M,M) = 16; A(2*M,M+1+M+1) = -2*h; A(2*M,M+1+M) = 4*h;
    A(2*M+1,1) = 1; A(2*M+1,2) = 2; A(2*M+1,M+1+2) = -h;
    A(2*M+2,M+1) = 1; A(2*M+2,M) = 2; A(2*M+2,M+1+M) = h;

    x = A\b;
    v = x(1:M+1);
    w = x(M+2:end);
end