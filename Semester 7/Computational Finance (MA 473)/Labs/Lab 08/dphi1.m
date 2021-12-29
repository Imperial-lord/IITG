function [y] = dphi1(x_min, x_max, N, i, x, lm)
	deg = 1;
	h = (x_max - x_min)/N;
	x0 = x_min + (i-1)*h;
	x1 = x_min + i*h;
	x2 = x_min + (i+1)*h;

	if lm == 0
		xx = x - h/3;
	else
		xx = x + h/3;
	end

	if i == 0
		y = -deta(deg, x_min, x_max, N, i, xx);
	elseif i == N
		y = deta(deg, x_min, x_max, N, i-1, xx);
	elseif (xx < x1)
		y = deta(deg, x_min, x_max, N, i-1, xx);
	else
		y = -deta(deg, x_min, x_max, N, i, xx);
	end

	if (xx < x0) || (xx > x2)
		y = 0;
end