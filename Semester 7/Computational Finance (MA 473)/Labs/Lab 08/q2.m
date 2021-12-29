function q2
	close all; clear; im_num = 1;
	x_min = 0;
	x_max = 1;
	N = 100;
	h = (x_max - x_min)/N;
	X = x_min:h:x_max;

	% Trapezoid Linear
	A = zeros(N+1, N+1);
	B = zeros(N+1, N+1);
	C = zeros(N+1, N+1);
	d = zeros(N+1, 1);

	for i = 1:N-1
	% For the basis/row of A
		for j = 0:N
		% For the Uj
			for k = 0:N-1
			% For integration interval
				A(i+1,j+1) = A(i+1,j+1) + (h/2) ...
					* (dphi1(x_min, x_max, N, i, X(k+1), 1)*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ dphi1(x_min, x_max, N, i, X(k+2), 0)*dphi1(x_min, x_max, N, j, X(k+2), 0));

				B(i+1,j+1) = B(i+1,j+1) + (h/2) ...
					* (bb(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ bb(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*dphi1(x_min, x_max, N, j, X(k+2), 0));

				C(i+1,j+1) = C(i+1,j+1) + (h/2) ...
					* (cc(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*phi1(x_min, x_max, N, j, X(k+1)) ...
					+ cc(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*phi1(x_min, x_max, N, j, X(k+2)));

				if j == 0
					d(i+1) = d(i+1) + (h/2) * (dd(X(k+1))*phi1(x_min, x_max, N, i, X(k+1)) ...
						+ dd(X(k+2))*phi1(x_min, x_max, N, i, X(k+2)));
				end
			end
		end
	end

	AA = A + B + C;
	AA(1,1) = 1;
	AA(N+1, N+1) = 1;

	% AA

	U = AA\d;
	figure; plot(X, U'); title('Piecewise-linear basis functions and trapezoidal rule');
	xlabel('X'); ylabel('Y'); 
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;

	% Simpson's Linear
	A = zeros(N+1, N+1);
	B = zeros(N+1, N+1);
	C = zeros(N+1, N+1);
	d = zeros(N+1, 1);

	for i = 1:N-1
	% For the basis/row of A
		for j = 0:N
		% For the Uj
			for k = 0:N-1
			% For integration interval
				A(i+1,j+1) = A(i+1,j+1) + (h/6) ...
					* (dphi1(x_min, x_max, N, i, X(k+1), 1)*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ dphi1(x_min, x_max, N, i, (X(k+1)+X(k+2))/2, 1)*dphi1(x_min, x_max, N, j, (X(k+1)+X(k+2))/2, 1) ...
					+ dphi1(x_min, x_max, N, i, X(k+2), 0)*dphi1(x_min, x_max, N, j, X(k+2), 0));

				B(i+1,j+1) = B(i+1,j+1) + (h/6) ...
					* (bb(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ bb((X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, i,(X(k+1)+X(k+2))/2)*dphi1(x_min, x_max, N, j, (X(k+1)+X(k+2))/2, 1) ...
					+ bb(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*dphi1(x_min, x_max, N, j, X(k+2), 0));

				C(i+1,j+1) = C(i+1,j+1) + (h/6) ...
					* (cc(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*phi1(x_min, x_max, N, j, X(k+1)) ...
					+ cc((X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, i, (X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, j, (X(k+1)+X(k+2))/2) ...
					+ cc(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*phi1(x_min, x_max, N, j, X(k+2)));

				if j == 0
					d(i+1) = d(i+1) + (h/6) * (dd(X(k+1))*phi1(x_min, x_max, N, i, X(k+1)) ...
						+ dd((X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, i, (X(k+1)+X(k+2))/2) ...
						+ dd(X(k+2))*phi1(x_min, x_max, N, i, X(k+2)));
				end
			end
		end
	end

	AA = A + B + C;
	AA(1,1) = 1;
	AA(N+1, N+1) = 1;

	% AA

	U = AA\d;
	figure; plot(X, U'); title('Piecewise-linear basis functions and Simpson’s rule');
	xlabel('X'); ylabel('Y'); 
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;

	% Trapezoid quadratic
	A = zeros(N+1, N+1);
	B = zeros(N+1, N+1);
	C = zeros(N+1, N+1);
	d = zeros(N+1, 1);

	for i = 1:N-1
	% For the basis/row of A
		for j = 0:N
		% For the Uj
			for k = 0:N-1
			% For integration interval
				A(i+1,j+1) = A(i+1,j+1) + (h/2) ...
					* (dphi1(x_min, x_max, N, i, X(k+1), 1)*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ dphi1(x_min, x_max, N, i, X(k+2), 0)*dphi1(x_min, x_max, N, j, X(k+2), 0));

				B(i+1,j+1) = B(i+1,j+1) + (h/2) ...
					* (bb(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ bb(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*dphi1(x_min, x_max, N, j, X(k+2), 0));

				C(i+1,j+1) = C(i+1,j+1) + (h/2) ...
					* (cc(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*phi1(x_min, x_max, N, j, X(k+1)) ...
					+ cc(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*phi1(x_min, x_max, N, j, X(k+2)));

				if j == 0
					d(i+1) = d(i+1) + (h/2) * (dd(X(k+1))*phi1(x_min, x_max, N, i, X(k+1)) ...
						+ dd(X(k+2))*phi1(x_min, x_max, N, i, X(k+2)));
				end
			end
		end
	end


	AA = A + B + C;
	AA(1,1) = 1;
	AA(N+1, N+1) = 1;

	% AA

	U = AA\d;
	figure; plot(X, U'); title('Piecewise-quadratic basis functions and trapezoidal rule');
	xlabel('X'); ylabel('Y'); 
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;

	% Simpson's quadratic
	A = zeros(N+1, N+1);
	B = zeros(N+1, N+1);
	C = zeros(N+1, N+1);
	d = zeros(N+1, 1);

	for i = 1:N-1
	% For the basis/row of A
		for j = 0:N
		% For the Uj
			for k = 0:N-1
			% For integration interval
				A(i+1,j+1) = A(i+1,j+1) + (h/6) ...
					* (dphi1(x_min, x_max, N, i, X(k+1), 1)*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ dphi1(x_min, x_max, N, i, (X(k+1)+X(k+2))/2, 1)*dphi1(x_min, x_max, N, j, (X(k+1)+X(k+2))/2, 1) ...
					+ dphi1(x_min, x_max, N, i, X(k+2), 0)*dphi1(x_min, x_max, N, j, X(k+2), 0));

				B(i+1,j+1) = B(i+1,j+1) + (h/6) ...
					* (bb(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*dphi1(x_min, x_max, N, j, X(k+1), 1) ...
					+ bb((X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, i,(X(k+1)+X(k+2))/2)*dphi1(x_min, x_max, N, j, (X(k+1)+X(k+2))/2, 1) ...
					+ bb(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*dphi1(x_min, x_max, N, j, X(k+2), 0));

				C(i+1,j+1) = C(i+1,j+1) + (h/6) ...
					* (cc(X(k+1))*phi1(x_min, x_max, N, i, X(k+1))*phi1(x_min, x_max, N, j, X(k+1)) ...
					+ cc((X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, i, (X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, j, (X(k+1)+X(k+2))/2) ...
					+ cc(X(k+2))*phi1(x_min, x_max, N, i, X(k+2))*phi1(x_min, x_max, N, j, X(k+2)));

				if j == 0
					d(i+1) = d(i+1) + (h/6) * (dd(X(k+1))*phi1(x_min, x_max, N, i, X(k+1)) ...
						+ dd((X(k+1)+X(k+2))/2)*phi1(x_min, x_max, N, i, (X(k+1)+X(k+2))/2) ...
						+ dd(X(k+2))*phi1(x_min, x_max, N, i, X(k+2)));
				end
			end
		end
	end

	AA = A + B + C;
	AA(1,1) = 1;
	AA(N+1, N+1) = 1;

	% AA

	U = AA\d;
	figure; plot(X, U'); title('Piecewise-quadratic basis functions and Simpson’s rule');
	xlabel('X'); ylabel('Y'); 
	saveas(gcf, sprintf('plots/q2_%d.png', im_num)); im_num = im_num + 1;
end

function [y] = bb(x)
	y = 0;
end

function [y] = cc(x)
	y = 2*x + 1;
end

function [y] = dd(x)
	y = sin(x);
end