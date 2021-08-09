% Sample script for running the function program after requesting user input.

n = input('Enter size(n) of matrix A to be decomposed: ');
A = randn(n);
disp('A = '); disp(A);

[L,U] = genp(A);
disp('L = '); disp(L);
disp('U = '); disp(U);
disp('L*U = '); disp(L*U);