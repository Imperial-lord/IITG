function [y] = phi1(x_min, x_max, N, i, x)
	deg = 1;
	h = (x_max - x_min)/N;
	x0 = x_min + (i-1)*h;
	x1 = x_min + i*h;
	x2 = x_min + (i+1)*h;

	if i == 0
		y = 1 - eta(deg, x_min, x_max, N, i, x);
	elseif i == N
		y = eta(deg, x_min, x_max, N, i-1, x);
	elseif (x < x1)
		y = eta(deg, x_min, x_max, N, i-1, x);
	else
		y = 1 - eta(deg, x_min, x_max, N, i, x);
	end

	if (x < x0) || (x > x2)
		y = 0;
end