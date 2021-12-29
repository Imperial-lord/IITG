% Setting the numeric format in the command window
format long e;

% Generate the matrix A
matrix();

% Generate a random x (exact solution is known)
n = 5;
x = randn(n,1);
b = A*x;

% Solving using gepp
xc = geppsolve(A,b);

% residual r = b - Axc
r = b-A*xc;

relative_error = norm(xc-x,Inf)/norm(x,Inf);
disp(relative_error);

% The idea here is to push only into b, because A is already given and well
% represented by the IEEE floating point numbers

% Classic condition number upper bound -
kappa_a_inf = cond(A,Inf);
ub_classic = kappa_a_inf*(norm(r,Inf)/norm(b,Inf));
disp(ub_classic);

% Skeel condition number upper bound - 
skeel_a_inf = norm(abs(inv(A))*abs(A),Inf);
u = eps;
ub_skeel = u*skeel_a_inf;
disp(ub_skeel);

T = table(relative_error', ub_classic', ub_skeel', 'VariableNames', {'Relative Error', 'Classic Condition Number Bound', 'Skeel Condition Number Bound'});
disp(T);

%{
    We observe that relative error is bound by both classic and skeel upper
    bounds, and skeel upper bound < classic upper bound, which is in
    accordance with the theoritical result, i.e, skeel(A) <= k(A).
%}
