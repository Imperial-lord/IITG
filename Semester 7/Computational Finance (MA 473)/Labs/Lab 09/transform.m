function [y] = transform(U, X, Tau, q, qd, K)
	y = zeros(size(U));
	if length(Tau) == 1
		for j = 1:length(X)
			y(j) = U(j) * K * exp(-0.5* (qd-1)*X(j) - (0.25*(qd-1)^2 + q)*Tau);
		end
	else
		for i = 1:length(Tau)
			for j = 1:length(X)
				y(i, j) = U(i, j) * K * exp(-0.5* (qd-1)*X(j) - (0.25*(qd-1)^2 + q)*Tau(i));
			end
		end
	end
end