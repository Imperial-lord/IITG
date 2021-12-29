function M = findM(b, h)
%This function returns the spatial step size
%Input:
%   b:  |x| <= b 
%   h: spatial step size
%Output
%   M:  Number of spatial data points
M = round(2*b/h);
end