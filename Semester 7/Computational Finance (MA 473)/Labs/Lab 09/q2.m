close all; clear; clc; im_num = 1;

% Option Parameters
T = 1;
K = 10;
r = 0.06;
sig = 0.3;
delta = 0;

q = 2*r/sig^2;
qd = 2*(r-delta)/sig^2;

% Computational Parameters
x_min = -5;
x_max = 1;

h = 0.05;
k = h^2/2;
m = (x_max - x_min)/h;
n = ceil((T*sig^2/2)/k);

X = x_min:h:x_max;
Tau = 0:k:T*sig^2/2;

S = K*exp(X);
Time = T - 2*Tau/sig^2;

Methods = ['Trapezoidal rule with piecewise linear functions'; 'Simpson’s  rule  with piecewise linear functions'];
for i = 1:2
	U = Crank_Nicolson(@fun, @f, @g1, @g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau, Methods(i, :));
	figure; plot(S, U(end, :)); hold on; plot(S, U(1, :)); hold off;
	legend('Cost of option at t = 0', 'Cost of option at t = T'); xlabel('S'); ylabel('u(S, t)'); title(sprintf('Crank-Nicolson using \n %s method', Methods(i, :)));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	figure; surf(S, Time, U); xlabel('S'); ylabel('t'); zlabel('u(S,t)'); title(sprintf('Crank-Nicolson using \n %s method', Methods(i, :)));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
end

function [y] = fun(x, t)
	y = 0;
end

function [y] = f(x, qd)
	temp1 = zeros(size(x));
	temp2 = exp(x*(qd - 1)/2) - exp(x*(qd + 1)/2 );
	y = max([temp1; temp2]);
end

function [y] = g1(x, t, qd)
	y = exp(x.*(qd - 1)/2 + t.*(qd - 1)^2/4);
end

function [y] = g2(x, t, qd)
	y = 0;
end