function [x] = jacobi(A, b, n_iter, tol)
	n = length(A);

	x1 = ones(size(b));
	for i = 1:n_iter
		x0 = x1;
		x1 = (b - (A - eye(n).*diag(A))*x0) ./ diag(A);
		if norm(x1 - x0) < tol
			break;
		end
	end

	x = x1;
end