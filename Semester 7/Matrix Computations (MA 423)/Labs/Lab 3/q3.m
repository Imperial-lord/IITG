n = 10;
H = hilb(n);
x = randn(n,1);
b = H*x;
xt = H\b;
r = H*xt - b;
fprintf('norm(r)/norm(b):%e\nnorm(x - xt)/norm(x):%e\n'...
        ,norm(r)/norm(b),norm(x - xt)/norm(x));