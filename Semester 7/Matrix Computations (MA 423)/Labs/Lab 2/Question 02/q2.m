% Setting the numeric format in the command window
format long e;

% Taking values of n from 5 to 10 and generating random matrices
for n=5:10
    A = randn(n);

    % Output of [L,U,p] = gepp(A)
    [L,U,p] = gepp(A);
    % disp('The values of L, U and p are');
    % disp(L); disp(U); disp(p);
    
    % Output of in-built [L,U,p] = lu(A)
    [L1,U1,p1] = lu(A, 'vector'); 
    
    % ||A(p, :) − LU||, and difference in 2 norm between 
    % output of gepp code with the corresponding outputs of the lu for different n values - 
    fprintf("For value of n = %d\n",n);
    disp("[norm(A(p,:) - L*U), norm(L-L1), norm(U-U1), norm(p-p1)]");
    disp([norm(A(p,:) - L*U), norm(L-L1), norm(U-U1), norm(p-p1)]);
end