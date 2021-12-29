function [y] = dphi2(x_min, x_max, N, i, x, lm)
	deg = 2;
	h = (x_max - x_min)/N;
	x0 = x_min + (i-2)*h;
	x1 = x_min + i*h;
	x2 = x_min + (i+2)*h;

	if lm == 0
		xx = x - h/6;
	else
		xx = x + h/6;
    end

	y = 0;
	if mod(i, 2) == 1
		y = 4*deta(deg, x_min, x_max, N, i-1, xx) ...
			 - 8*eta(deg, x_min, x_max, N, i-1, x)*deta(deg, x_min, x_max, N, i-1, xx);
	elseif i == 0
		if x <= x2
			y = -3*deta(deg, x_min, x_max, N, i, xx) ...
			 + 4*eta(deg, x_min, x_max, N, i, x)*deta(deg, x_min, x_max, N, i, xx);
		end
	elseif i == N
		if x >= x0
			y = -deta(deg, x_min, x_max, N, i-2, xx) ...
			 + 4*eta(deg, x_min, x_max, N, i-2, xx)*deta(deg, x_min, x_max, N, i-2, xx);
		end
	else
		if (x0 <= x) && (x <= x1)
			y = -deta(deg, x_min, x_max, N, i-2, xx) ...
			 + 4*eta(deg, x_min, x_max, N, i-2, x)*deta(deg, x_min, x_max, N, i-2, xx);
		elseif (x1 <= x) && (x <= x2)
			y = -3*deta(deg, x_min, x_max, N, i, xx) ...
			 + 4*eta(deg, x_min, x_max, N, i, x)*deta(deg, x_min, x_max, N, i, xx);
		end
			
	end

	if (xx < x0) || (xx > x2)
		y = 0;
end