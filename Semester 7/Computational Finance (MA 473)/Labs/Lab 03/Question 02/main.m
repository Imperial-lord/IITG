function main
	close all; clear; im_num = 1;
	% Terminal Condition flag
	isTerminal = true;

	T = 1;
	K = 10;
	r = 0.06;
	sig = 0.3;
	delta = 0;

	% Boundary
	S_min = 0;
	S_max = 15;

	h = 1;
	k = h^2/50;
	m = (S_max - S_min)/h;
	n = ceil(T/k);

	S = S_min:h:S_max;
	Time = 0:k:T;

	% Tau = T - t
	U = FTCS(T, K, r, sig, delta, S, Time, h, k, isTerminal);
	% size(Time), size(S), size(U)
	figure; plot(S, U(1, :)); hold on; plot(S, U(end, :)); hold off;
	legend('Cost of option at t = 0', 'Cost of option at t = T'); xlabel('S'); ylabel('u(S, t)'); title('FTCS');
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	figure; surf(S, Time, U); xlabel('S'); ylabel('t'); zlabel('u(x,t)'); title('FTCS');
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	
	Methods = {'Matlab Back-Slash', 'Gauss-Seidel', 'Jacobi', 'SOR'};
	for meth = 1:4
		U = BTCS(T, K, r, sig, delta, S, Time, h, k, isTerminal, Methods{meth});
		figure; plot(S, U(1, :)); hold on; plot(S, U(end, :)); hold off;
		legend('Cost of option at t = 0', 'Cost of option at t = T'); xlabel('S'); ylabel('u(S, t)'); title(sprintf('BTCS using %s method', Methods{meth}));
		saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
		figure; surf(S, Time, U); xlabel('S'); ylabel('t'); zlabel('u(S,t)'); title(sprintf('BTCS using %s method', Methods{meth}));
		saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	end

	for meth = 1:4
		U = Crank(T, K, r, sig, delta, S, Time, h, k, isTerminal, Methods{meth});
		figure; plot(S, U(1, :)); hold on; plot(S, U(end, :)); hold off;
		legend('Cost of option at t = 0', 'Cost of option at t = T'); xlabel('S'); ylabel('u(S, t)'); title(sprintf('Crank-Nicolson using %s method', Methods{meth}));
		saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
		figure; surf(S, Time, U); xlabel('S'); ylabel('t'); zlabel('u(S,t)'); title(sprintf('Crank-Nicolson using %s method', Methods{meth}));
		saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
	end
end

function [y] = f(S, K)
	temp1 = zeros(size(S));
	temp2 = K - S;
	y = max([temp1; temp2]);
end

function [y] = g1(r, s, Tau, K)
	y = K*exp(-r.*Tau) - s;
end

function [y] = g2(r, s, Tau, K)
	y = 0;
end

function [y] = fa(sig, s)
	y = sig.^2 .* s.^2 / 2;
end

function [y] = fb(r, delta, s);
	y = (r - delta) .* s;
end

function [y] = fc(r)
	y = -r;
end

function [U] = FTCS(T, K, r, sig, delta, S, Tau, h, k, isTerminal)
	fprintf('\nRunning FTCS\n');
	m = length(S);
	n = length(Tau);
	U = zeros(n, m);

	if isTerminal
		k = -k;
	end

	U(1:end, 1) = g1(r, S(1), Tau, K);
	U(1:end, end) = g2(r, S(end), Tau, K);
	U(1, 1:end) = f(S, K);

	for i = 2:n
		for j = 2:m-1
			aa = fa(sig, S(j));
			bb = fb(r, delta, S(j));
			cc = fc(r);
			U(i, j) = (-aa*k/h^2 + 0.5*bb*k/h)*U(i-1,j-1) + (1 + 2*aa*k/h^2 - cc*k)*U(i-1,j) + (-aa*k/h^2 - 0.5*bb*k/h)*U(i-1,j+1);
		end
	end

	if isTerminal
		U = flipud(U);
	end
end

function [U] = BTCS(T, K, r, sig, delta, S, Tau, h, k, isTerminal, method)
	fprintf('\nRunning BTCS\n');
	fprintf('Using %s method\n', method);
	m = length(S);
	n = length(Tau);
	U = zeros(n, m);

	if isTerminal
		k = -k;
	end

	U(1:end, 1) = g1(r, S(1), Tau, K);
	U(1:end, end) = g2(r, S(end), Tau, K);
	U(1, 1:end) = f(S, K);

	for i = 2:n
		A = zeros(m, m);
		b = zeros(m, 1);

		aa = fa(sig, S);
		bb = fb(r, delta, S);
		cc = fc(r);

		A(1:m+1:end) = 1 - 2*aa*k/h^2 + cc*k;
		A(2:m+1:end) = aa(2:m)*k/h^2 - bb(2:m)*k/(2*h);
		A(m+1:m+1:end) = aa(1:m-1)*k/h^2 + bb(1:m-1)*k/(2*h);

		A(1,1) = 1;
		A(1,2) = 0;
		A(m,m) = 1;
		A(m,m-1) = 0;

		% norm(A)

		b(2:m-1) = U(i-1,2:m-1);
		b(1) = U(i,1);
		b(end) = U(i,end);

		if method(1) == 'B'
			U(i,:) = (A\b)';
		elseif method(1) == 'G'
			U(i,:) = gauss_seidel(A,b,1000,1e-5);
		elseif method(1) == 'J'
			U(i,:) = jacobi(A,b,1000,1e-5);
		else
			U(i,:) = sor(A,b,1000,1e-5);
		end			
			
	end

	if isTerminal
		U = flipud(U);
	end
end

function [U] = Crank(T, K, r, sig, delta, S, Tau, h, k, isTerminal, method)
	fprintf('\nRunning Crank Nicolson\n');
	fprintf('Using %s method\n', method);
	m = length(S);
	n = length(Tau);
	U = zeros(n, m);

	if isTerminal
		k = -k;
	end

	U(1:end, 1) = g1(r, S(1), Tau, K);
	U(1:end, end) = g2(r, S(end), Tau, K);
	U(1, 1:end) = f(S, K);

	for i = 2:n
		A = zeros(m, m);
		b = zeros(m, 1);

		aa = fa(sig, S);
		bb = fb(r, delta, S);
		cc = fc(r);

		A(1:m+1:end) = 2 - 2*aa*k/h^2 + cc*k;
		A(2:m+1:end) = aa(2:m)*k/h^2 - bb(2:m)*k/(2*h);
		A(m+1:m+1:end) = aa(1:m-1)*k/h^2 + bb(1:m-1)*k/(2*h);

		A(1,1) = 1;
		A(1,2) = 0;
		A(m,m) = 1;
		A(m,m-1) = 0;

		b(2:m-1) = (-aa(2:m-1)*k/h^2 + bb(2:m-1)*k/(2*h)) .* U(i-1,1:m-2) ...
					+ (2 + 2*aa(2:m-1)*k/h^2 - cc*k) .* U(i-1,2:m-1) ...
					+ (-aa(2:m-1)*k/h^2 - bb(2:m-1)*k/(2*h)) .* U(i-1,3:m);
		b(1) = U(i,1);
		b(end) = U(i,end);

		if method(1) == 'B'
			U(i,:) = (A\b)';
		elseif method(1) == 'G'
			U(i,:) = gauss_seidel(A,b,1000,1e-5);
		elseif method(1) == 'J'
			U(i,:) = jacobi(A,b,1000,1e-5);
		else
			U(i,:) = sor(A,b,1000,1e-5);
		end	
	end

	if isTerminal
		U = flipud(U);
	end
end