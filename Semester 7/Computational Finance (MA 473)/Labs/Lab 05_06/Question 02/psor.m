function [x] = psor(A, b, n_iter, tol)
	n = length(A);
	L = tril(A, -1);
	U = triu(A, 1);
	D = diag(A);

	Bj = - (eye(n) ./ D) * (L + U);
	w = 2 / (1 + sqrt(1 - norm(Bj)^2));

	x1 = ones(size(b));
	for i = 1:n_iter
		x0 = x1;
		for j = 1:n
			x1(j) = max(0, w * (b(j) - (L(j, :) + U(j, :))*x1) ./ D(j) + (1 - w) * x0(j));
		end
		
		if norm(x1 - x0) < tol
			break;
		end
	end

	x = x1;
end