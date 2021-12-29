A = randn(5);
m = 2;
u = randn(5,1);
v = randn(5,1);
x = randn(5,1);
b = A*x;

x_sol = SMsolve(A,u,v,m,b);
disp(x_sol);