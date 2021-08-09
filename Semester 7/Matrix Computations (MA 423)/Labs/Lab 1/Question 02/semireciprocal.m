function [s,scf,scb] = semireciprocal(m,k)
% Initialising the sums to 0
s = 0; scf = 0; scb = 0;

    for i=1:m
        s = s + 1/i;
        scf = chop(scf + chop(1/i,k),k);
        scb = chop(scb + chop(1/(m - i + 1),k),k);
    end
end