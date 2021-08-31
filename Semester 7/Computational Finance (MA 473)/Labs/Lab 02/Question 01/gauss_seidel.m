function [x] = gauss_seidel(A, b, n_iter, tol)
	n = length(A);
	L = tril(A, -1);
	U = triu(A, 1);
	D = diag(A);

	x1 = ones(size(b));
	for i = 1:n_iter
		x0 = x1;
		for j = 1:n
			x1(j) = (b(j) - (L(j, :) + U(j, :))*x1) ./ D(j);
		end
		
		if norm(x1 - x0) < tol
			break;
		end
	end

	x = x1;
end