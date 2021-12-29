P1 = [];
P2 = [];

for j=1:15
   [U,S,V] = svd(randn(20));
   S = 10^(-j + 6)*eye(20);
   A = U*S*V';
   [W,R] = polard1(A);
   [X,T] = polard2(A);
   P1 = [P1 norm(W'*W - eye(20))];
   P2 = [P2 norm(X'*X - eye(20))];
end

hold on
plot([1:15],P1);
plot([1:15],P2);
xlabel('j');
ylabel('norm');
legend('polard1','polard2');
hold off