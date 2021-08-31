function [U] = FTCS(fun, f, g1, g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau)
	fprintf('\nRunning FTCS\n');
	lamda = k / h^2;
	U = zeros(n+1, m+1);

	U(1:end, 1) = g1(x_min, Tau, qd);
	U(1:end, end) = g2(x_max, Tau, qd);
	U(1, 1:end) = f(X, qd);

	for i = 2:n+1
		for j = 2:m
			U(i, j) = lamda*U(i-1,j-1) + (1-2*lamda)*U(i-1,j) + lamda*U(i-1,j+1);
		end
	end

	U = transform(U, X, Tau, q, qd, K);
end