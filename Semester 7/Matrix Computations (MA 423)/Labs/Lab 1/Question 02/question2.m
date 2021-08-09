% Sample script for running the function program.

[s,scf,scb] = semireciprocal(1000,5);
% (a) Sum up 1/n for n = 1, 2, . . . , 1000
fprintf("Sum of 1/n for n = 1,2 .. 1000: %f\n",s);
% (b) Round each number 1/n to 5 digits and simulate the summing of the resulting sequence for n = 1, 2, . . . , 1000 in 5-digit arithmetic.
fprintf("Sum of 1/n for n = 1,2 .. 1000 in 5 digit arithmetic in forward order: %f\n",scf);
% (c)  Sum up the same chopped (or rounded) numbers in (b) again in 5-digit arithmetic but in reverse order, that is, for n = 1000, . . . , 2, 1.
fprintf("Sum of 1/n for n = 1000, .. 2,1 in 5 digit arithmetic in reverse order: %f\n",scb);

% Which is closer to (a) - (b) or (c)?
diff_ab = abs(s-scf);
diff_ac = abs(s-scb);

if(diff_ab < diff_ac)
    fprintf('(b) is closer to (a)');
else
    fprintf('(c) is closer to (a)');
end