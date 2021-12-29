function [x] = conjugate_gradient(A, b, n_iter, tol)
    % Function to implement Conjugate Gradient method
	n = length(A);
	x0 = ones(size(b));
    r0 = b - (A*x0);
    if(r0 < tol)
        x = x0;
    end
    p0 = r0;
	
    for i = 1:n_iter
        alp = (r0'*r0)/(p0'*A*p0);
        x0 = x0 + alp*p0;
        r1 = r0 - alp*A*p0;
        if(r1 < tol)
            break;
        end
        beta = (r1'*r1)/(r0'*r0);
		p0 = r1 + beta*p0;
        r0 = r1;
    end
	x = x0;
end