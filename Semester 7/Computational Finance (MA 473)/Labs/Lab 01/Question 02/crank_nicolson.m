function [U] = crank_nicolson(h, k, m, n, fun, f, g1, g2)
% crank_nicolson - function to implement the crank-nicolson method
% @param - h, k, m, n, fun, f, g1, g2
% @returns - U

    fprintf('\nCrank-Nicolson running ...\n');
	lamda = k / h^2;
    
	U = zeros(n+1, m+1);

	U(1, 1:end) = f((0:m)*h);
	U(1:end, 1) = g1((0:n)*k);
	U(1:end, end) = g2((0:n)*k);

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

		b(2:m) = U(i-1,1:m-1)*lamda/2 + (1-lamda)*U(i-1,2:m) + U(i-1,3:m+1)*lamda/2 + k*fun((1:m-1)*h,(i-1)*k);
		b(1) = U(i,1);
		b(end) = U(i,end);

		U(i,:) = (A\b)';
	end

end

