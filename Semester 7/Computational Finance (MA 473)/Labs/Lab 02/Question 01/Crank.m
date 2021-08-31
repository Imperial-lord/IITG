function [U] = Crank(fun, f, g1, g2, T, K, r, sig, delta, q, qd, x_min, x_max, h, k, m, n, X, Tau, method)
	fprintf('\nRunning Crank Nicolson\n');
	fprintf('Using %s method\n', method);
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

		if method == "Direct"
			U(i,:) = (A\b)';
		elseif method == "GaussS"
			U(i,:) = gauss_seidel(A,b,1000,1e-5);
		elseif method == "Jacobi"
			U(i,:) = jacobi(A,b,1000,1e-5);
		else
			""
		end	
	end

	U = transform(U, X, Tau, q, qd, K);
end