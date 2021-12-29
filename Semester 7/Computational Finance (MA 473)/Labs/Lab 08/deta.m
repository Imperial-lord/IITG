function [y] = deta(deg, x_min, x_max, N, i, x)
	h = (x_max - x_min)/N;
	x1 = x_min + i*h;
	x2 = x_min + (i+deg)*h;

	if (x >= x1) && (x <= x2)
		y = 1/h;
	else
		y = 0;
end