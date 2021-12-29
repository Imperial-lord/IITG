P1 = [];
P2 = [];
P3 = [];

N = [5,7,10,12];

for n = N
    H = hilb(n);
    R1 = mysqrt1(H);
    P1 = [P1 norm(H - R1*R1)/norm(H)];
    R2 = mysqrt2(H);
    P2 = [P2 norm(H - R2*R2)/norm(H)];
    R3 = sqrtm(H);
    P3 = [P3 norm(H - R3*R3)/norm(H)];
end

hold on;
plot(N,P1);
plot(N,P2);
plot(N,P3);
ylabel('norm(H - R*R)/norm(H)');
xlabel('N');
legend('mysqrt1','mysqrt2','sqrtm');
hold off