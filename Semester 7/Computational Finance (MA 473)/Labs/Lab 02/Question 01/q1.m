function q1
	close all; clear; im_num = 1;
	% Option Parameters
	T = 1;
	K = 10;
	r = 0.06;
	sig = 0.3;
	delta = 0;

	q = 2*r/sig^2;
	qd = 2*(r-delta)/sig^2;

	% Computational Parameters
	x_max = 1;
	x_min = -5;

	h = 0.05;
	k = h^2/2;
	m = (x_max - x_min)/h;
	n = ceil((T*sig^2/2)/k);

	X = x_min:h:x_max;
	Tau = 0:k:T*sig^2/2;

	S = K*exp(X);
	Time = T - 2*Tau/sig^2;

	
	U = FTCS(@fun, @f, @g1, @g2, T*sig^2/2, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau);
	% length(X), length(U(end, :))
	figure; plot(S, U(end, :)); hold on; plot(S, U(1, :)); hold off;
	legend('Cost of option at t = 0', 'Cost of option at t = T'); xlabel('S'); ylabel('u(S, t)'); title('FTCS');
	saveas(gcf, sprintf('plots/q1_%d.png', im_num)); im_num = im_num + 1;
	figure; surf(S, Time, U); xlabel('S'); ylabel('t'); zlabel('u(x,t)'); title('FTCS');
	saveas(gcf, sprintf('plots/q1_%d.png', im_num)); im_num = im_num + 1;
	
	Methods = ['Direct'; 'GaussS'; 'Jacobi'];%, 'SOR___'];
	for meth = 1:3
		U = BTCS(@fun, @f, @g1, @g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau, Methods(meth, :));
		figure; plot(S, U(end, :)); hold on; plot(S, U(1, :)); hold off;
		legend('Cost of option at t = 0', 'Cost of option at t = T'); xlabel('S'); ylabel('u(S, t)'); title(sprintf('BTCS using %s method', Methods(meth, :)));
		saveas(gcf, sprintf('plots/q1_%d.png', im_num)); im_num = im_num + 1;
		figure; surf(S, Time, U); xlabel('S'); ylabel('t'); zlabel('u(S,t)'); title(sprintf('BTCS using %s method', Methods(meth, :)));
		saveas(gcf, sprintf('plots/q1_%d.png', im_num)); im_num = im_num + 1;
	end

	for meth = 1:3
		U = Crank(@fun, @f, @g1, @g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau, Methods(meth, :));
		figure; plot(S, U(end, :)); hold on; plot(S, U(1, :)); hold off;
		legend('Cost of option at t = 0', 'Cost of option at t = T'); xlabel('S'); ylabel('u(S, t)'); title(sprintf('Crank-Nicolson using %s method', Methods(meth, :)));
		saveas(gcf, sprintf('plots/q1_%d.png', im_num)); im_num = im_num + 1;
		figure; surf(S, Time, U); xlabel('S'); ylabel('t'); zlabel('u(S,t)'); title(sprintf('Crank-Nicolson using %s method', Methods(meth, :)));
		saveas(gcf, sprintf('plots/q1_%d.png', im_num)); im_num = im_num + 1;
	end
end

function [y] = fun(x, t)
	y = 0;
end

function [y] = f(x, qd)
	temp1 = zeros(size(x));
	temp2 = exp(x*(qd + 1)/2 ) - exp(x*(qd - 1)/2);
	y = max([temp1; temp2]);
end

function [y] = g1(x, t, qd)
	y = 0;
end

function [y] = g2(x, t, qd)
	y = exp(x.*(qd + 1)/2 + t.*(qd + 1)^2/4);
end