function h = findh(b, M)
%This function returns the spatial step size
%Input:
%   b:  |x| <= b 
%   M:  Number of spatial data points
%Output:
%   h: spatial step size
h = 2*b/M;
end