% Setting the numeric format in the command window
format long e;

% (a) Find the factors L and U of an LU-decomposition of A = [10^−20 1; 1 1]. What is A−LU?
A = [10^-20,1;1,1];
[L,U] = genp(A);
disp('The factors L and U are: ');
disp(L); disp(U);

disp('A - L*U = ');
disp(A - L*U);

%(b) Solve  the  system  of  equations Ax=b
b = [1;0];

% Solve these 2 eqs using rowforward and colforward
% Ly = b
% Ux = y
y = rowforward(L,b);
x = colbackward(U,y);
disp('Solution using genp');
disp(x);

% Use x = A\b to find the exact solution
x_actual = A\b;
disp('Exact solution of Ax = b');
disp(x_actual);

% The difference of genp answer with the correct solution in the 2-norm
fprintf('2-norm of difference between exact solution and genp solution =  %f\n', norm(x_actual - x,2));