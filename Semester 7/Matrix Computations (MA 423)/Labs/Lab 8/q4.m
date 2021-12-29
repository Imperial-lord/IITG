P1 = [];
P2 = [];
P3 = [];
P4 = [];

for j=1:15
   [U,S,V] = svd(randn(20));
   S = 10^(-j + 6)*eye(20);
   A = U*S*V';
   
   [U1,S1,V1] = mysvd(A);
   [U2,S2,V2] = svd(A);
   P1 = [P1 norm(V1'*V1 - eye(20))];
   P2 = [P2 norm(V2'*V2 - eye(20))];
   P3 = [P3 norm(U1'*U1 - eye(20))];
   P4 = [P4 norm(U2'*U2 - eye(20))];
end

figure;
hold on
plot([1:15],P1);
plot([1:15],P2);
xlabel('j');
ylabel("norm(I - V'V");
legend('mysvd','svd');
hold off

figure;
hold on
plot([1:15],P3);
plot([1:15],P4);
xlabel('j');
ylabel("norm(I - U'U");
legend('mysvd','svd');
hold off