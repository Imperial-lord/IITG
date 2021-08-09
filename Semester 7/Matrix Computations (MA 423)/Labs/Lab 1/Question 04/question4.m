% Sample script for running the function programs after requesting user input.

% (a)  x = colbackward(U,b) to solve an upper triangular system Ux = b by column oriented back substitution.
n = input('Input the size of Upper Triangular Matrix(n): ');
fprintf('Solution of the system system Ux = b\n');

U = triu(randn(n));
b = randn(n,1);
x = colbackward(U,b);

disp('U ='); disp(U);
disp('b ='); disp(b);
disp('x = '); disp(x);


% (b) x = rowforward(L,b) to solve a lower triangular system Lx = b by row oriented forward substitution.
n = input('Input size of Lower Triangular Matrix(n): ');
fprintf('Solve system Lx = b\n');

L = tril(randn(n));
b = randn(n,1);
x = rowforward(L,b);

disp('L ='); disp(L);
disp('b ='); disp(b);
disp('x = '); disp(x);

