N = 8:2:12;
format long e;
for n = N
   fprintf('<strong> n = %d </strong>\n\n',n);
   H =  hilb(n);
   HI = invhilb(n);
   x = rand(n,1);
   b = H*x;
   x1 = H\b;
   x2 = HI*b;
   x3 = geppsolve(H,b);
   fprintf('[x x1 x2 x3]\n');
   disp([x x1 x2 x3]);
   
   fprintf('[cond(H) norm(x - x1)/norm(x) norm(x - x2)/norm(x) norm(x - x3)/norm(x)]\n');
   fprintf('--------------------------------------------------------------------------\n')
   disp([cond(H) norm(x - x1)/norm(x) norm(x - x2)/norm(x) norm(x - x3)/norm(x)]);
   save("q2_workspace_N="+num2str(n));
end