x = [1;1;1];

% part (a)
A = [1 1 1;-1 9 2;0 -1 2];
fprintf("(a) ");
check_convergence(A,x,15);

% part (b)
A = [1 1 1;-1 9 2;-4 -1 2];
fprintf("(b) ");
check_convergence(A,x,15);

% part (c)
A = [1 1 1;-1 3 2;-4 -1 2];
fprintf("(c) ");
check_convergence(A,x,15);

function check_convergence(A,x,k)
    [V,D] = eig(A);    
    [D,P] = sort(diag(D),'descend');
    V = V(:,P);
    v = V(:,1);
    [~,i] = max(abs(v));
    s = v(i);
    v = v/s;
    lambda1 = D(1);
    lambda2 = D(2);

    [iter,lambda] = Powermethod(A,x,k);
    theoretical_conv = norm(iter(:,end) - v)/norm(iter(:,end - 1) - v);
    experimental_conv = abs(lambda2)/abs(lambda1);
    
    fprintf("Theoritical convergence rates = %f\n", theoretical_conv);
    fprintf("Experimental convergence rates = %f\n", experimental_conv);
    fprintf("Absolute Difference in convergence rates = %f\n", abs(theoretical_conv - experimental_conv))
end