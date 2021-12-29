function [y] = phi2(x_min, x_max, N, i, x)
	deg = 2;
	h = (x_max - x_min)/N;
	x0 = x_min + (i-2)*h;
	x1 = x_min + i*h;
	x2 = x_min + (i+2)*h;

	y = 0;
	if mod(i, 2) == 1
		y = 4*eta(deg, x_min, x_max, N, i-1, x) - 4*eta(deg, x_min, x_max, N, i-1, x)^2;
	elseif i == 0
		if x <= x2
			y = 1 - 3*eta(deg, x_min, x_max, N, i, x) + 2*eta(deg, x_min, x_max, N, i, x)^2;
		end
	elseif i == N
		if x >= x0
			y = -eta(deg, x_min, x_max, N, i-2, x) + 2*eta(deg, x_min, x_max, N, i-2, x)^2;
		end
	else
		if (x0 <= x) && (x <= x1)
			y = - eta(deg, x_min, x_max, N, i-2, x) + 2*eta(deg, x_min, x_max, N, i-2, x)^2;
		elseif (x1 <= x) && (x <= x2)
			y = 1 - 3*eta(deg, x_min, x_max, N, i, x) + 2*eta(deg, x_min, x_max, N, i, x)^2;
		end
			
	end

	if (x < x0) || (x > x2)
		y = 0;
end