p = [1 -18 144 -672 2016 -4032 5376 -4608 2304 -512];

a = 1.95; b = 2; c=2.05;
R1 = a + (b-a).*rand(10,1);
R2 = b + (c-b).*rand(10,1);
tol = 10^-8;

for i=1:10
    r1 = min(R1(i), R2(i));
    r2 = max(R1(i), R2(i));
    
    root = bisect(p, r1, r2, tol);
    disp(root);
end