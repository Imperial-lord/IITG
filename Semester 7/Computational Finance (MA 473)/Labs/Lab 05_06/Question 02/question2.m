function q2
	close all; clear; im_num = 1;
	% Option Parameters
	T = 1;
	K = 10;
	r = 0.25;
	sig = 0.6;
	delta = 0.2;

	q = 2*r/sig^2;
	qd = 2*(r-delta)/sig^2;

	% Computational Parameters
	x_max = 2;
	x_min = -5;

	h = 0.01;
	k = 0.01;
	m = (x_max - x_min)/h;
	n = ceil((T*sig^2/2)/k);
	m_base = m;

	X = x_min:h:x_max;
	Tau = 0:k:T*sig^2/2;

	S = K*exp(X);
	indices = (1 < S) & (S < 30);
	Time = T - 2*Tau/sig^2;

	U = BTCS(@fun, @f, @g1, @g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau);
	figure; plot(S(indices), U(end, indices)); hold on; ttemp = transform(g(X, Time(end), q, qd), X, Time(end), q, qd, K); plot(S(indices), ttemp(indices)); hold off;
	legend('Price of option at t = 0', 'max(S-K, 0) at t = 0'); xlabel('S'); ylabel('u(S, t)'); title(sprintf('BTCS using PSOR method'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	figure; surf(S(indices), Time, U(:, indices)); xlabel('S'); ylabel('t'); zlabel('u(S,t)'); title(sprintf('BTCS using PSOR method'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	U1_real = U(end, :);

	U = Crank(@fun, @f, @g1, @g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau);
	figure; plot(S(indices), U(end, indices)); hold on; ttemp = transform(g(X, Time(end), q, qd), X, Time(end), q, qd, K); plot(S(indices), ttemp(indices)); hold off;
	legend('Price of option at t = 0', 'max(S-K, 0) at t = 0'); xlabel('S'); ylabel('u(S, t)'); title(sprintf('Crank-Nicolson using PSOR method'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	figure; surf(S(indices), Time, U(:, indices)); xlabel('S'); ylabel('t'); zlabel('u(S,t)'); title(sprintf('Crank-Nicolson using PSOR method'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	U2_real = U(end, :);
	Is = [1, 2, 5, 10, 12.5, 25];
	N1 = []; E1 = []; E2 = [];

	for iiii = 1:6
		h = 0.5/Is(iiii);
		k = 0.5/Is(iiii);
		m = (x_max - x_min)/h;
		n = floor((T*sig^2/2)/k);

		N1 = [N1, m];

		X = x_min:h:x_max;
		Tau = 0:k:T*sig^2/2;

		S = K*exp(X);
		Time = T - 2*Tau/sig^2;

		U = BTCS(@fun, @f, @g1, @g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau);
		U1_bad = U(end, :);
		E1 = [E1, max(abs(U1_bad - U1_real(1:(m_base/m):end)))];

		U = Crank(@fun, @f, @g1, @g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau);
		U2_bad = U(end, :);
		E2 = [E2, max(abs(U2_bad - U2_real(1:(m_base/m):end)))];
	end

	figure; plot(S, abs(U1_bad - U1_real(1:(m_base/m):end))); 
	legend('Error in U for (dx and dTau), and (dx/2 and dTau/2) at t = 0'); xlabel('S'); ylabel('Error');
	title(sprintf('BTCS Error in U for (δx and δτ), and (δx/2 and δτ/2) at t = 0'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;

	figure; plot(N1, E1); xlabel('N'); ylabel('Error');
	title(sprintf('BTCS. Max absolute Error vs N'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;

	figure; plot(S, abs(U2_bad - U2_real(1:(m_base/m):end))); 
	legend('Error in U for (dx and dTau), and (dx/2 and dTau/2) at t = 0'); xlabel('S'); ylabel('Error');
	title(sprintf('Crank-Nicolson Error in U for (δx and δτ), and (δx/2 and δτ/2) at t = 0'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;

	figure; plot(N1, E2); xlabel('N'); ylabel('Error');
	title(sprintf('Crank-Nicolson. Max absolute Error vs N'));
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
end

function [y] = g(x, t, q, qd)
	temp1 = zeros(size(x));
	temp2 = exp(x*(qd - 1)/2 ) - exp(x*(qd + 1)/2);

	y = exp(t*( (qd-1)^2 + 4*q )/4 ) .* max([temp1; temp2]);
end

function [y] = fun(x, t)
	y = 0;
end

function [y] = f(x, qd)
	temp1 = zeros(size(x));
	temp2 = exp(x*(qd - 1)/2 ) - exp(x*(qd + 1)/2);
	y = max([temp1; temp2]);
end

function [y] = g1(x, t, qd)
	y = exp(x.*(qd - 1)/2 + t.*(qd - 1)^2/4);
end

function [y] = g2(x, t, qd)
	y = 0;
end

function [y] = transform(U, X, Tau, q, qd, K)
	y = zeros(size(U));
	if length(Tau) == 1
		for j = 1:length(X)
			y(j) = U(j) * K * exp(-0.5* (qd-1)*X(j) - (0.25*(qd-1)^2 + q)*Tau);
		end
	else
		for i = 1:length(Tau)
			for j = 1:length(X)
				y(i, j) = U(i, j) * K * exp(-0.5* (qd-1)*X(j) - (0.25*(qd-1)^2 + q)*Tau(i));
			end
		end
	end
end

function [U] = BTCS(fun, f, g1, g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau)
	fprintf('\nRunning BTCS\n');
	fprintf('Using PSOR method\n');
	lamda = k / h^2;
	U = zeros(n+1, m+1);

	U(1:end, 1) = g1(x_min, Tau, qd);
	U(1:end, end) = g2(x_max, Tau, qd);
	U(1, 1:end) = f(X, qd);

	for i = 2:n+1
		A = zeros(m+1, m+1);
		b = zeros(m+1, 1);

		A(1:m+2:end) = 1 + 2*lamda;
		A(2:m+2:end) = -lamda;
		A(m+2:m+2:end) = -lamda;

		A(1,1) = 1;
		A(1,2) = 0;
		A(m+1,m+1) = 1;
		A(m+1,m) = 0;

		b(2:m) = U(i-1,2:m);
		b(1) = U(i,1);
		b(end) = U(i,end);

		GG = g(X, Tau(i), q, qd);
		U(i,:) = psor(A,b - A*GG',1000,1e-5)' + GG;
	end

	U = transform(U, X, Tau, q, qd, K);
end

function [U] = Crank(fun, f, g1, g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau)
	fprintf('\nRunning Crank Nicolson\n');
	fprintf('Using PSOR method\n');
	lamda = k / h^2;
	U = zeros(n+1, m+1);

	U(1:end, 1) = g1(x_min, Tau, qd);
	U(1:end, end) = g2(x_max, Tau, qd);
	U(1, 1:end) = f(X, qd);

	for i = 2:n+1
		A = zeros(m+1, m+1);
		b = zeros(m+1, 1);

		A(1:m+2:end) = 1 + lamda;
		A(2:m+2:end) = -lamda/2;
		A(m+2:m+2:end) = -lamda/2;

		A(1,1) = 1;
		A(1,2) = 0;
		A(m+1,m+1) = 1;
		A(m+1,m) = 0;

		b(2:m) = U(i-1,1:m-1)*lamda/2 + (1-lamda)*U(i-1,2:m) + U(i-1,3:m+1)*lamda/2;
		b(1) = U(i,1);
		b(end) = U(i,end);

		GG = g(X, Tau(i), q, qd);
		U(i,:) = psor(A,b - A*GG',1000,1e-5)' + GG;
	end

	U = transform(U, X, Tau, q, qd, K);
end