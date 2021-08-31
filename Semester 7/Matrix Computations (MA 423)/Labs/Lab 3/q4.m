N = 32:32:64;
for n = N
   fprintf('<strong> n = %d</strong>\n',n);
   x = randn(n,1);
   W = Wilkinson(n);
   b = W*x;
   xcap = geppsolve(W,b);
   r = W*xcap - b;
   fprintf('\nGEPP method\n');
   fprintf('forward error norm(x - xcap,inf)/norm(x,inf): %e\n',...
       norm(x - xcap,inf)/norm(x,inf));
   fprintf('cond(W): %e\n', cond(W));
   fprintf('norm(r,inf)/norm(b,inf): %e\n',norm(r,inf)/norm(b,inf));
   
   fprintf('\nQR method\n');
   [Q,R] = qr(W);
   xcap = colbackward(R,Q'*b);
   r = W*xcap - b;
   fprintf('forward error norm(x - xcap,inf)/norm(x,inf): %e\n',...
       norm(x - xcap,inf)/norm(x,inf));
   fprintf('cond(W): %e\n', cond(W));
   fprintf('norm(r,inf)/norm(b,inf): %e\n',norm(r,inf)/norm(b,inf));
   fprintf('-------------------------------------------------\n');
   
   save("q4_workspace_N="+num2str(n));
end