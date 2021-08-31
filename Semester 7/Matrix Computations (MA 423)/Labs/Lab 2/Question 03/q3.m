% Setting the numeric format in the command window
format short e;

% Taking values of n from 5 to 10 and generating random matrices
for n=5:10
    fprintf("For value of n = %d\n",n);
    A = randn(n);
    b = randn(n,1);

    x = geppsolve(A,b);
    disp('Solution using geppsolve(A,b)');
    disp(x);

    x1 = A\b;
    disp('Solution using A\b');
    disp(x1);
end