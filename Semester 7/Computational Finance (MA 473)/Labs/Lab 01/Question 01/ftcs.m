function [U] = ftcs(h, k, m, n, fun, f, g1, g2)
% ftcs - function to implement the forward-difference (explicit) method
% @param - h, k, m, n, fun, f, g1, g2
% @returns - U

    fprintf('\nFTCS running ...\n');
	lambda = k / h^2;
    
    % invoke ftcs_stability function to check for stability of FTCS scheme
    % throws an error if the scheme is unstable
    ftcs_stability(lambda);
    
	U = zeros(n+1, m+1);
	U(1, 1:end) = f((0:m)*h);
	U(1:end, 1) = g1((0:n)*k);
	U(1:end, end) = g2((0:n)*k);
    
    for i = 2:n+1
        for j = 2:m
            t = (i-1)*k;
			x = (j-1)*h;
			U(i, j) = lambda*U(i-1,j-1) + (1-2*lambda)*U(i-1,j) + lambda*U(i-1,j+1) + k*fun(x,t);
        end
    end
end

